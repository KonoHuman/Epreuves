import random

try:

    liste_de_citations = ["Un seul être vous manque et tout est dépeuplé  Lamartine","Aimer, ce n'est pas se regarder l'un l'autre, c'est regarder ensemble dans la même direction  Antoine De Saint-Exupéry","Les seuls beaux yeux sont ceux qui vous regardent avec tendresse  Coco Chanel","S'aimer soi-même est le début d'une histoire d'amour qui durera toute une vie  Oscar Wilde","La vie est un mystère qu'il faut vivre, et non un problème à résoudre  Gandhi","La vie, c'est comme une bicyclette, il faut avancer pour ne pas perdre l'équilibre  Albert Einstein","Je ne cherche pas à connaître les réponses, je cherche à comprendre les questions  Confucius","Choisissez un travail que vous aimez et vous n'aurez pas à travailler un seul jour de votre vie  Confucius","Le domaine de la liberté commence là où s'arrête le travail déterminé par la nécessité  Karl Marx","Le travail, c'est le refuge des gens qui n'ont rien de mieux à faire  Oscar Wilde","Il ne faut avoir aucun regret pour le passé, aucun remords pour le présent, et une confiance inébranlable pour l'avenir  Jean Jaurès"]

    question = str(input('Voulez-vous recevoir votre citation du jour ? :'))

    if question == 'oui':
        
        citation_du_jour = random.choice(liste_de_citations)
        
        print('Voici la citation du jour : ', citation_du_jour)
        
    elif question == 'non':
        
        print('Tres bien à demain')
        
    else:
        print('Veuillez répondre par oui ou par non')
        
except ValueError:
    print('Erreur')




