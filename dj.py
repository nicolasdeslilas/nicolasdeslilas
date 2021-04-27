from pathlib import Path

p = Path.home()
p = p / "Documents/python/dir/readme.txt"

p.touch()
p.write_text("salut les gas")
p.read_text()

