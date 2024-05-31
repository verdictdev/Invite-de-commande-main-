import random

def findnumber():
    nombre = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    random.choice(nombre)

    nombre_a_trouver = int(input('Nomrbe : '))
    essais = 5
    while essais > 5:

        if nombre_a_trouver == nombre:
            print('Bien joué !')
                            
            refaire = input('Voulez-vous refaire ?')

            if refaire == 'oui':
                continue

            else:
                break

        elif nombre_a_trouver > nombre:
            print('Plus petit !')
            essais -= 1
            continue

        elif nombre_a_trouver < nombre:
            print('Plus grand !')
            essais -= 1
            continue