def heuresminutes24to12():
    """Convertit un temps de 24 heures en 12 heures."""
    heure24 = int(input("Entrez l'heure (format 24 heures): "))
    minute = int(input("Entrez les minutes: "))
    
    if heure24 == 0 or heure24 == 24:
        heure12 = 00
        print("L'heure est", heure12, ":", minute, "AM")
    elif heure24 > 12:
        heure12 = heure24 - 12
        print("L'heure est", heure12, ":", minute, "PM")
    else:
        print("L'heure est", heure24, ":", minute, "AM")
        
heuresminutes24to12()
    