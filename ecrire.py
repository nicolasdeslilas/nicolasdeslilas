from pathlib import Path

p = Path.home() / "Music/3615Radio/"
mp3 = p.rglob("*.mp3")
s = p.touch("mp3.txt")
fille = p / "mp3.txt"
name = [""]
for f in mp3:
    name = f({name} + (f.name))

print(name)
    



