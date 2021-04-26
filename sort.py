import shutil
from pathlib import Path
import glob
d = {".mp3" : "Musique",
     ".wav" : "Musique",
     ".mp4" : "Video",
     ".mov" : "Video",
     ".mkv" : "Video",
     ".doc": "Document",
     ".pdf": "Document",
     ".csv": "Document",
     ".txt" : "Document",
     ".zip" : "Archive",
     ".7z" : "Archive",  
     ".py" : "code",
     ".sh" : "code",
     ".jpeg" : "Photo",
     ".jpg" : "Photo",
     ".png" : "Photo",
     ".dmg": "Application",
     ".iso": "Application",
     ".exe" : "Application",
     ".pkg" : "Application",
     ".torrent" : "Torrent"}


p = Path.home() / input("choissisez votre Dossier à classer par exemple -Documents : \n")
fichier = [f for f in p.iterdir() if f.is_file()]
for f in fichier:
    dossier = p / d.get(f.suffix, 'Autres')
    dossier.mkdir(exist_ok=True)
    f.rename(dossier / f.name)