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
res = mot1 if mot1 < mot2 else mot2
print(" est le plus petit est:", res)