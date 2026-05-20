import csv
import io
import re
from pathlib import Path


def parse_sql_tuple_fields(tuple_bytes: bytes) -> list[str]:
    inner = tuple_bytes[1:-1]
    fields: list[str] = []
    i = 0
    n = len(inner)
    while i < n:
        while i < n and inner[i:i + 1] in b" \t":
            i += 1
        if i >= n:
            break
        if inner[i:i + 1] == b"'":
            i += 1
            val = bytearray()
            while i < n:
                if inner[i:i + 1] == b"\\" and i + 1 < n:
                    val.extend(inner[i + 1:i + 2])
                    i += 2
                elif inner[i:i + 1] == b"'":
                    i += 1
                    break
                else:
                    val.extend(inner[i:i + 1])
                    i += 1
            fields.append(val.decode("utf-8", errors="replace"))
        else:
            start = i
            while i < n and inner[i:i + 1] != b",":
                i += 1
            fields.append(inner[start:i].decode("utf-8", errors="replace").strip())
        while i < n and inner[i:i + 1] in b" \t":
            i += 1
        if i < n and inner[i:i + 1] == b",":
            i += 1
    return fields


def tuple_to_csv_line(tuple_bytes: bytes) -> str:
    buf = io.StringIO()
    csv.writer(buf).writerow(parse_sql_tuple_fields(tuple_bytes))
    return buf.getvalue().rstrip("\n")


src = Path.home() / "temp/diff/new/20-may-26/mws-2-1-uat.sql"
dst = Path.home() / "temp/diff/new/20-may-26/mws-2-1-uat.cleaned.sql"
dup = Path.home() / "temp/diff/new/20-may-26/mws-2-1-uat.duplicates.txt"
seen: dict[bytes, dict[str, object]] = {}
duplicate_count = 0
tuple_re = re.compile(rb"\((\d+),(?:[^'()]|'(?:\\.|[^'\\])*')*\)")
values_re = re.compile(rb"\bVALUES\s*", re.IGNORECASE)
with (
    src.open("rb") as fin,
    dst.open("wb") as fout,
    dup.open("wb") as dups,
):
    for line_number, line in enumerate(fin, start=1):
        if line.startswith(b"INSERT INTO `wp_postmeta`"):
            values_match = values_re.search(line)
            if values_match is None:
                fout.write(line)
                continue

            kept_tuples = []
            for match in tuple_re.finditer(line, values_match.end()):
                meta_id = match.group(1)
                if meta_id in seen:
                    duplicate_count += 1
                    meta_id_text = meta_id.decode("ascii")
                    first = seen[meta_id]
                    first_line = first["line"]
                    first_csv = tuple_to_csv_line(first["tuple"])
                    duplicate_csv = tuple_to_csv_line(match.group(0))
                    print(
                        f"Duplicate wp_postmeta meta_id={meta_id_text}: "
                        f"kept line {first_line}, duplicate line {line_number}"
                    )
                    print(f"kept,{first_csv}")
                    print(f"discarded,{duplicate_csv}")
                    print()
                    dups.write(
                        f"Duplicate wp_postmeta meta_id={meta_id_text}: "
                        f"kept line {first_line}, duplicate line {line_number}\n".encode("ascii")
                    )
                    dups.write(f"kept,{first_csv}\n".encode("utf-8"))
                    dups.write(f"discarded,{duplicate_csv}\n\n".encode("utf-8"))
                    continue

                seen[meta_id] = {"tuple": match.group(0), "line": line_number}
                kept_tuples.append(match.group(0))

            if kept_tuples:
                newline = b"\n" if line.endswith(b"\n") else b""
                line = line[:values_match.end()] + b",".join(kept_tuples) + b";" + newline
            else:
                print(f"All wp_postmeta tuples were duplicates at source line {line_number}; skipping line")
                continue

        fout.write(line)
print(f"Wrote {dst}")
print(f"Wrote duplicate report: {dup}")
print(f"Unique wp_postmeta meta_ids seen: {len(seen)}")
print(f"Duplicate wp_postmeta entries removed: {duplicate_count}")