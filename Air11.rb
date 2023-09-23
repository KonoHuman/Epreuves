# Demandez à l'utilisateur de choisir le caractère de l'escalier
caractere = input("Entrez le caractère pour l'escalier : ")

# Demandez à l'utilisateur de choisir le nombre d'étages
nombre_etages = int(input("Entrez le nombre d'étages de l'escalier : "))

# Boucle pour construire l'escalier
for etage in range(1, nombre_etages + 1):
    espaces = nombre_etages - etage  # Calcule le nombre d'espaces à gauche
    bloc = caractere * (2 * etage - 1)  # Construit le bloc de caractères
    ligne = ' ' * espaces + bloc  # Combine les espaces et le bloc
    print(ligne)
