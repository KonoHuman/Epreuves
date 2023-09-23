def h_min_12_to_24(h, min):
    """Convertit un temps de 12 heures en 24 heures."""
    if h == 12:
        h = 0
    h = h + 12
    return h, min

h = int(input("Entrez l'heure (format 12 heures): "))
min = int(input("Entrez les minutes: "))
print(h_min_12_to_24(h, min))