import math

nombre = float(input("Entrez un nombre : "))

if nombre >= 0:
  racine = math.sqrt(nombre)
  print("La racine carrée de {} est {}".format(nombre, racine))
else:
  print("Erreur : le nombre doit être positif ou nul.")
  
  
  mot1 = input("Entrez un premier mot : ")
  mot2 = input("Entrez un deuxième mot : ")

if mot1 < mot2:
  print(mot1 + " est plus petit que " + mot2)
else:
  print(mot2 + " est plus petit que " + mot1)

# Avec l'instruction ternaire
resultat = mot1 if mot1<mot2 else mot2
Print(" le plus petit mot est :", résultat )
# question 3
pSeuil = 2.3
vSeuil = 7.41

pCourant = float(input("Entrez la pression courante : "))
vCourant = float(input("Entrez le volume courant : "))

if pCourant > pSeuil and vCourant > vSeuil:
    print("Arrêt immédiat !")
elif pCourant > pSeuil:
    print("La pression est trop élevée. Veuillez augmenter le volume de l'enceinte.")
elif vCourant > vSeuil:
    print("Le volume est trop élevé. Veuillez diminuer le volume de l'enceinte.")
else:
    print("Tout va bien !")
# question 4
a = 0
b = 10

# Boucle pour afficher et incrémenter la valeur de a
while a < b:
    print(a)
    a += 1

# Boucle pour décrémenter b et afficher sa valeur si elle est impaire
while b > 0:
    if b % 2 == 1:
        print(b)
    b -= 1
# question 5 et 6
# Afficher chaque caractère d'une chaîne
chaine = "Hello World!"
for c in chaine:
    print(c)

# Afficher chaque élément d'une liste
liste = [1, 2, 3, 4, 5]
for element in liste:
    print(element)
# question 7
for i in range(0, 15, 3):
    print(i)
# question 8
for i in range(1, 11):
    print(i)
    if i == 5:
        break
# question 9
for i in range(1, 11):
    if i == 5:
        continue
    print(i)
# question 10
import math

for x in range(-3, 4):
    try:
        y = math.sin(x) / x
        print(f"sin({x})/{x} = {y}")
    except ZeroDivisionError:
        print(f"sin({x})/{x} = indéfini")
# question 11

import easygui

# initialise une liste avec 5 entiers
liste_entiers = [2, 4, 6, 8, 10]

# saisit un entier avec integerbox et sauvegarde la valeur dans la variable 'entier_saisi'
entier_saisi = easygui.integerbox(msg="Saisissez un entier:", title="Entier saisi", lowerbound=1)

# initialise la variable 'entier_trouve' à None (aucun entier trouvé pour le moment)
entier_trouve = None

# parcourt chaque entier de la liste
for entier in liste_entiers:
    # si l'entier saisi est trouvé dans la liste, sauvegarde sa valeur dans 'entier_trouve' et interrompt la boucle
    if entier_saisi == entier:
        entier_trouve = entier
        break

# si aucun entier n'a été trouvé, affiche un message
else:
    easygui.msgbox("L'entier saisi n'a pas été trouvé dans la liste.")
# saisit un entier positif avec intergerbox et sauvegarde la valeur dans la variable 'entier_positif'
    entier_positif = easygui.integerbox(msg="saisissez un entier positif:", title="entier positif",lowerbound=1)
# initialise la variable 'est_premier' à true (l'entier est considéré premier jusqu'à preuve de contraire)
    est_premier = True

# initialise la variable 'diviseur' à None (aucun diviseur trouvé pour le moment)
diviseur = None

# parcourt chaque entier de 2 à la valeur de 'entier_positif' exclue (car un nombre n'est jamais divisible par lui-même)
for i in range(2, entier_positif):
    # si 'entier_positif' est divisible par i, sauvegarde la valeur de 'i' dans 'diviseur' et interrompt la boucle
    if entier_positif % i == 0:
        diviseur = i
        est_premier = False
        break

# si 'est_premier' est True (aucun diviseur n'a été trouvé), affiche l'entier saisi
if est_premier:
    easygui.msgbox(f"L'entier {entier_positif} est premier.")
# sinon, affiche le premier diviseur trouvé
else:
    easygui.msgbox(f"L'entier {entier_positif} n'est pas premier. Son premier diviseur est {diviseur}.")
