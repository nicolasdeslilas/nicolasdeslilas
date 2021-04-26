import random

moi = 50
lui = 50
attaqueMoi = random.randint(5,10)
attaqueLui = random.randint(5,20)
potion = random.randint(15,50)
quotaPotion = 3

while moi >= 0 or lui >= 0:
    choix = input(f"Vous avez {moi} 💖 \nL'ennemi a {lui} 💖\n ------------------------------------------------\n Presse 🗡 (1) Presse 🧪(2)\n")
    if int(choix) == 1:
        lui = lui - attaqueMoi
       
    if int(choix) == 2 and quotaPotion > 0:
        moi = moi + potion
        quotaPotion = quotaPotion - 1
        print(f"il vous rèste {quotaPotion} 🧪")
       
    moi = moi - attaqueLui
    if moi <= 0:
        print("Vous Avez Perdu")
        break
    elif lui <= 0:
        print("👑 Vous Avez Gagner 👑")
        break
        

