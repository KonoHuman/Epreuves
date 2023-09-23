def evaluer_une_expression():
    """Évalue une expression arithmétique donnée par l'utilisateur."""

    # Demandez à l'utilisateur d'entrer une expression
    expression = input("Entrez une expression arithmétique : ")

    # Vous pouvez utiliser des opérateurs directement plutôt que des chaînes de caractères
    liste_operateurs = ["+", "-", "*", "/"]

    compteur_operateurs = 0

    # Parcourez la liste des opérateurs et comptez combien d'occurrences ils ont dans l'expression
    for operateur in liste_operateurs:
        compteur_operateurs += expression.count(operateur)

    # Vérifiez si le nombre d'opérateurs est supérieur ou égal à 5
    if compteur_operateurs >= 5:
        print("L'expression est valide.")
        resultat = eval(expression)  # Évaluez l'expression
        return resultat  # Retournez le résultat de l'évaluation
    else:
        print("Erreur : l'expression doit contenir au moins 5 opérateurs.")
        return None  # Retournez None en cas d'erreur

# Appelez la fonction et affichez le résultat si l'expression est valide
resultat = evaluer_une_expression()
if resultat is not None:
    print("Résultat de l'expression :", resultat)
