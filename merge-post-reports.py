#!/usr/bin/env python3
"""Merge test/live post report CSVs into a single Excel workbook."""

from __future__ import annotations

import re
from pathlib import Path

import pandas as pd

REPORTS_DIR = Path("/Users/adiyen/lando-workspace/wp-migration-poc/scripts/post-reports")
OUTPUT_FILE = REPORTS_DIR / "post-reports.xlsx"

TEST_PREFIX = "mws-2-1-test-"
LIVE_PREFIX = "mwe-com-may27-liv-"
MISSING = "Missing Post"


def sheet_name_from_filename(filename: str) -> str | None:
    name = Path(filename).stem
    if name.startswith(TEST_PREFIX):
        return name[len(TEST_PREFIX) :]
    if name.startswith(LIVE_PREFIX):
        return name[len(LIVE_PREFIX) :]
    return None


def load_report(path: Path) -> pd.DataFrame:
    with path.open(encoding="utf-8") as handle:
        header_row = next(
            (idx for idx, line in enumerate(handle) if line.startswith("postid,")),
            None,
        )
    if header_row is None:
        raise ValueError(f"No CSV header found in {path}")

    df = pd.read_csv(path, skiprows=header_row, dtype={"postid": "Int64"})
    return df[["postid", "lang_code", "post-title", "permalink"]]


def merge_reports(test_df: pd.DataFrame | None, live_df: pd.DataFrame | None) -> pd.DataFrame:
    if test_df is None and live_df is None:
        return pd.DataFrame(
            columns=["postid", "lang_code", "post-title", "permalink(test)", "permalink(live)"]
        )

    if test_df is None:
        test_df = pd.DataFrame(columns=["postid", "lang_code", "post-title", "permalink"])
    if live_df is None:
        live_df = pd.DataFrame(columns=["postid", "lang_code", "post-title", "permalink"])

    merged = pd.merge(
        test_df,
        live_df,
        on="postid",
        how="outer",
        suffixes=("_test", "_live"),
    )

    merged["lang_code"] = merged["lang_code_test"].combine_first(merged["lang_code_live"])
    merged["post-title"] = merged["post-title_test"].combine_first(merged["post-title_live"])

    merged["permalink(test)"] = merged["permalink_test"].where(
        merged["permalink_test"].notna(),
        MISSING,
    )
    merged["permalink(live)"] = merged["permalink_live"].where(
        merged["permalink_live"].notna(),
        MISSING,
    )

    result = merged[["postid", "lang_code", "post-title", "permalink(test)", "permalink(live)"]]
    return result.sort_values("postid", kind="stable").reset_index(drop=True)


def main() -> None:
    by_sheet: dict[str, dict[str, Path]] = {}

    for csv_path in sorted(REPORTS_DIR.glob("*.csv")):
        sheet = sheet_name_from_filename(csv_path.name)
        if sheet is None:
            continue

        by_sheet.setdefault(sheet, {})
        if csv_path.name.startswith(TEST_PREFIX):
            by_sheet[sheet]["test"] = csv_path
        elif csv_path.name.startswith(LIVE_PREFIX):
            by_sheet[sheet]["live"] = csv_path

    with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
        for sheet in sorted(by_sheet.keys()):
            paths = by_sheet[sheet]
            test_df = load_report(paths["test"]) if "test" in paths else None
            live_df = load_report(paths["live"]) if "live" in paths else None
            merged = merge_reports(test_df, live_df)

            # Excel sheet names max 31 chars; truncate if needed
            safe_sheet = sheet[:31]
            merged.to_excel(writer, sheet_name=safe_sheet, index=False)

    print(f"Wrote {OUTPUT_FILE} with {len(by_sheet)} sheet(s)")


if __name__ == "__main__":
    main()
