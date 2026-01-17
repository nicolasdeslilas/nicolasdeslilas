nombreA = input('Entrez un premier nombre: ')
nombreB = input('Entrez un deuxieme nombre: ')
resultat = (nombreA) + (nombreB)

if nombreA.isdigit() and nombreB.isdigit() == True:
    phrase =f"Le resultat de l\'addition {nombreA} avec {nombreB} est égale à {int(nombreA) + int(nombreB)}"
    print(phrase)
else:
    print('entrer un nombre')