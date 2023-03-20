# str mmethod
prenom = "patrice"

print(prenom.capitalize()) # transfome le premier caractere en majuscule
print(prenom.upper()) # permet de mettre toute la chaine de caractere en majuscule
print(prenom.lower()) # c'est tout le contraire de upper
print(prenom.split()) # permet de convertir la chaine de caractere en tableau de caractere*
print(prenom.find("p")) # retourne -1 si le caracteres ou la chaine de caracteres n'exixte pas ou l'indice du caractere rechercher
print(prenom.replace("a","e")) # permet de remplacer un caractere par un autre
print(prenom.count("ice")) # permet de compter l'occurence d'une chaine de caractere
print(prenom.startswith("pa")) # retoune vrai si la variable commence par la chaine de caractere passé en parametre
print(prenom.endswith("ce")) # retoune vrai si la variable se termine par la chaine de caractere passé en parametre
print(prenom.index("i")) # retoune l'index si le caractere ou la chaine de caractere exixte
prenom1 = " patrice miguel "
print(prenom1.split()) 
print("".join(prenom1) ) # permet de joindre la variable à une chaine
print(prenom1)
print(prenom1.strip()) # spprime les espace exterieure a la chaine de carectere