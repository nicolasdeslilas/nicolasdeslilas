from random import randint

player1 = 50
boot = 50
potion = 3

while True:
    if boot <= 0 :
        print("Tu as gagné \n Fin du jeu.")
        exit()
    elif player1 <= 0:
        print("Vous avez perdu \n fin du jeu")
        exit()
    user_choice = input("Souhaitez vous attaquer (1) ou utiliser une potion (2): ")
    
    if not user_choice.isdigit():
        continue
    elif int(user_choice) > 2:
        continue
    elif int(user_choice) == 1:
        attaque_player1 = randint(5, 10)
        boot -= attaque_player1
        print(f"Vous avez infligé {attaque_player1} points de dégats")
        attaque_boot = randint(5, 15)
        player1 -= attaque_boot
        print(f"L'ennemi vous a infligé {attaque_boot} points de dégats")
        print(f"Il vous reste {player1} points de vie")
        print(f"Il reste {boot} points de vie à l'ennemi")
        print("-" * 50)
    elif int(user_choice) == 2:
        if potion == 0:
            print("Vous n'avez plus de potion...")
            continue
        else:
            bonus = randint(15, 50)
            player1 += bonus
            print(f"Vous avez récuperé {bonus} points de vie")
            potion -= 1
            attaque_boot = randint(5, 15)
            player1 -= attaque_boot
            print(f"L'ennemi vous a infligé {attaque_boot} points de dégats")
            print(f"Il vous reste {player1} points de vie")
            print(f"Il reste {boot} points de vie à l'ennemi")
            print("-" * 50)
        print("Vous passez votre tour...")
        attaque_boot = randint(5, 15)
        player1 -= attaque_boot
        print(f"L'ennemi vous a infligé {attaque_boot} points de dégats")
        print(f"Il vous reste {player1} points de vie")
        print(f"Il reste {boot} points de vie à l'ennemi")
        print("-" * 50)

