# Invite de commande version 2 par Verdict # CG = Chat GPT 

# Import MCMD ;

import MFindnumber

# Import ;

import getpass
import os
import sys
import random
import time
import keyboard

from colorama import *

# Connexion ;

os.system("cls")
print("Bienvenue dans la version 2 de l'invite de commande par Atlaz.")
print('Avant chaque commande veuillez taper / (sauf clear).')
print('Saisir le bon mot de passe si dessous (5 essais).\n')

essais = 5

# Verification ;

while essais > 0:
    
    os.system('color a')
    mot_de_passe = getpass.getpass('Mot de passe > ')

    if mot_de_passe == 'zeroun':
        os.system('color f')
        print('Invite de commande actif !')
    
        while True:

            # Entré dans l'invite de commande ;

                # Fonction par ordre alphabétique, conditionnement des commandes ;
                
                def calculatrice():
                    
                    typecalculatrice = """
                    Physique chimie
                    Mathematique simple
                    Mathematique plus"""
                    print(typecalculatrice)
                    type = input("Entrez le type > ")
                    
                    if type == "Physique chimie":
                    
                        while True:

                            calc = """
                            La calculatrice peut comprendre > 
                            masse gravitationnelle"""
                            print(calc)
                            calcscience = input('\nType de calcul > ')
                            
                            if calcscience == 'masse gravitationnelle':
                                
                                while True:
                                
                                    G = 6.67e-11 # La notation 'e' désigne "fois 10 puissance"
                                    print('Entrez la première masse / kg')
                                    m1 = float(input('')) 
                                    
                                    print('Entrez la seconde masse / kg')
                                    m2 = float(input(''))
                                    
                                    print('Entrez la distance / mètre')
                                    r = float(input(''))

                                    force_gravitationnelle = G * (m1 * m2) / r**2
                                    print(f"La force gravitationnelle est de {force_gravitationnelle:.2e} N")

                                    break

                            else:
                                print("Type introuvable !")
                                break

                    elif type == "Mathematique simple":

                        number = float(input("Nombre 1 > "))
                        number_ = float(input("Nombre 2 > "))
                        methode = str(input("Méthode de calcul > "))

                        if methode == "+":
                            print(number + number_)

                        elif methode == "-":
                            print(number - number_)

                        elif methode == "*":
                            print(number * number_)
                                  
                        elif methode == "/":
                            print(number / number_)

                        else:
                            print("Méthode introuvable.")


                    # Mathématique plus...
                
                def color():
                    
                    color_help = """
                    0 = Noir     8 = Gris
                    1 = Bleu        9 = Bleu clair
                    2 = Vert        A = Vert clair
                    3 = Bleu-gris        B = Cyan
                    4 = Rouge      C = Rouge clair
                    5 = Violet     D = Violet clair
                    6 = Jaune        E = Jaune clair
                    7 = Blanc       F = Blanc brillant\n"""

                    print(color_help)
                    print('Saisir la couleur') 
                    color = input("")
                    os.system(f'color {color}')

                def create_dossier():
                    os.system('color 4')
                    print("Précision : Le dossier sera créé dans le répertoire ou est enregistré l'invite de commande.")
                    time.sleep(2)
                    os.system('color f')
                    print('Entrez le nom de votre dossier')
                    name_dossier = input("")
                    os.system(f'mkdir {name_dossier}')

                def create_fichier():
                    os.system('color 4')
                    print("Précision : Le dossier sera créé dans le répertoire ou est enregistré l'invite de commande.")
                    os.system('color f')
                    time.sleep(1.5)
                    print("Entrez le nom de votre fichier + l'extension")
                    name_fichier = input("")
                    os.system(f'type nul > {name_fichier}')
                                    
                def help():
                    affiche_help = """
                    clear           = supprimer ce qui est affiché à l'écran.
                    /quit           = quitter l'invite de commande.
                    /color          = choisir une couleur.
                    /calcul         = calculatrice a / s / d / m.
                    /calculatrice   = calculatrice plus complexe (scientifique).
                    /dossier        = Créer un dossier.
                    /fichier        = Créer un fichier.
                    /findnumber     = Jeu de nombre.
                    /randomcolor    = couleur attribuée aléatoirement.
                    /randomname     = imprimer un nom aléatoire.
                    /spam           = spammer la donnée entrée.
                    /taskkill       = Tuer un programme en cours.
                    /timer          = Timer.
                    """

                    print(affiche_help)
                
                def random_color():
                    liste_color = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
                    random.choice(liste_color)
                    os.system(f'color {liste_color}')

                def spam_text(text, count):
                    for _ in range(count):
                        keyboard.write(text)
                        keyboard.press_and_release('enter')

                # Paramètres
                texte_a_envoyer = input('Spam > ')
                nombre_de_messages = input('Combien de fois > ')

                def taskkill():
                    print("Entrez le nom de l'application à tuer + .exe")
                    kill_tache = input('')
                    os.system(f"TASKKILL /IM {kill_tache}")

                commande = input('> ')

                # Commande continuer, quitter, help, clear ; 

                if commande == '/quit':
                    os.system('color 4')
                    certain = input("Voulez-vous vraiment quitter l'invite de commande ? ")
                    
                    try:
                        certain = str(certain)
                    
                    except:
                        print('| erreur | Veuillez saisir une chêne de caractère | recommencer |')
                        continue
                    
                    else:
                        if certain == 'oui':
                            sys.exit()

                        else:
                            os.system('color f')
                            print("Retour vers l'invite de commande...")
                            time.sleep(2)

                elif commande == '/help':
                    help()

                elif commande == '':
                    continue
                     
                # Commande ; 

                elif commande == '/calculatrice':
                    calculatrice()
                
                elif commande == 'clear':
                    os.system('cls')
                
                elif commande == '/color':
                    color()

                elif commande == '/dossier':
                    create_dossier()

                elif commande == '/echo':
                    print("Message > ")
                    echo = input("")
                    os.system(f"echo {echo}")

                elif commande == '/easter':
                    print("")
                    # Not finish

                elif commande == '/fichier':
                    create_fichier()
                
                elif commande == '/findnumber':
                    MFindnumber.findnumber()

                elif commande == '/randomcolor':
                    random_color()

                elif commande == '/randomname':
                    # Lire les prénoms à partir du fichier texte
                    with open("prenoms.txt", "r") as file:
                        prenoms = file.read().splitlines()

                    # Choisir un prénom aléatoire
                    prenom_aleatoire = random.choice(prenoms)

                    # Afficher le prénom aléatoire
                    print("Prénom aléatoire choisi :", prenom_aleatoire)

                elif commande == "/spam":
                    spam_text(texte_a_envoyer, nombre_de_messages)

                elif commande == '/taskkill':
                    taskkill()
                
                elif commande == '/timer':
                    # CG
                    
                    class Timer:
                        def __init__(self, seconds):
                            self.seconds = seconds

                        def countdown(self):
                            seconds = self.seconds
                            while seconds:
                                mins, secs = divmod(seconds, 60)
                                timer = f'{mins:02d}:{secs:02d}'
                                print(timer, end="\r")
                                time.sleep(1)
                                seconds -= 1
                            print("Finish !")

                        @staticmethod
                        def main():
                            try:
                                total_seconds = int(input('Entrez le temps en secondes : '))
                                timer = Timer(total_seconds)
                                timer.countdown()
                            except ValueError:
                                print('Entrez un nombre valide.')

                    if __name__ == '__main__':
                        Timer.main()

                else:
                    print(Fore.RED + 'Commande introuvable.')
                    time.sleep(1)
                    continue

    else:
        essais -= 1
        if essais > 0:
            print(Fore.RED + 'Mauvais mot de passe, veuillez réessayer !')

        else:
            print("Nombre d'essais épuisé.")   