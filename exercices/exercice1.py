temps = 6.892
distance = 19.7
vitesse = distance / temps
print("la vitesse est de :{}".format(vitesse))
print("La vitesse est de : {:.1f}".format(vitesse))


# questions 2

nom = input("Entrez votre nom : ")
age = input("Entrez votre âge : ")
print("Nom : ", nom)
print("Âge : ", age)

nom = input("Entrez votre nom : ") 
print("Nom : ", nom)

# Exemple de transtypage des saisies avec raw_input()
nom = str(input("Entrez votre nom : "))
age = int(input("Entrez votre âge : "))
print("Nom : ", nom)
print("Âge : ", age)