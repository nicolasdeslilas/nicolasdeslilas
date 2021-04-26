from pathlib import Path
import os
p = Path.home() / "Documents/python/dir"


d = {"Films": ["Le seigneur des anneaux",
               "Harry Potter",
               "Moon",
               "Forrest Gump"],
     "Employes": ["Paul",
                  "Pierre",
                  "Marie"],
     "Exercices": ["les_variables",
                   "les_fichiers",
                   "les_boucles"]}

for key, value in d.items():
    for dossier in value:
        p = os.path.join(p, key, dossier)
        os.makedirs(p, exist_ok=True)

