import random

nombreX = random.randint(0,100)
print(nombreX)
print('Trouver le nomnbre mystère entre 0 - 100 \n il vous rèste 5 tentative')
for i in range(5):
    user = input("Rentrer un nombre: ")
    print(f"il vous rèste {5-i} tentative")
    if int(user) == nombreX:
        print('bravo')
        break
    elif int(user) > nombreX:
        print("le nombre X est plus petit")
    elif int(user) < nombreX:
        print("le bombre X est plus grand")    
else:
    print('vasi tue pue')
       
  


