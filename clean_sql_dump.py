import re
from pathlib import Path
src = Path.home() / "temp/diff/new/mws-2-1-uat.sql"
dst = Path.home() / "temp/diff/new/mws-2-1-uat.cleaned.sql"
dup = Path.home() / "temp/diff/new/mws-2-1-uat.duplicates.txt"
seen = set()
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
                    print(f"Duplicate wp_postmeta meta_id={meta_id_text} at source line {line_number}")
                    dups.write(f"Duplicate wp_postmeta meta_id={meta_id_text} at source line {line_number}\n".encode("ascii"))
                    dups.write(match.group(0))
                    dups.write(b"\n\n")
                    continue

                seen.add(meta_id)
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