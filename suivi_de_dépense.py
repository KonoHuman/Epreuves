def suivi_de_dépenses():
    
    try:
    
        print('Voici vos dépenses hebdomadaires : ')
        
        nombre_de_semaine = 52
            
        semaine = 1
        
        total_des_dépenses = []
        
        while semaine != nombre_de_semaine:
            
            
            question = input("Voulez-vous rentrer de nouvelles dépenses ? : ").lower()
            
            if question == "oui":
        
                dépense_de_la_semaine = int(input('Combien avez-vous dépensé cette semaine ? : '))
                

                print('Cette semaine' + '(' + str(semaine) + ')' + 'vous avez dépensé : ' + str(dépense_de_la_semaine) + 'EUR')
                
                
                total_des_dépenses.append(dépense_de_la_semaine)
                
                somme_des_depenses = sum(total_des_dépenses)
                    
                print('Vous avez dépensé en tout : ', somme_des_depenses, 'EUR')
                
                semaine += 1
                
                
            elif question == 'non':
                print('Très bien.')
                
            elif question == 'fin':
                print('Au revoir')
                break
                
            else:
                print('Veuillez répondre par oui ou par non.')
                
    except ValueError:
        print("Erreur, vous jouez avec le feu")
        
    
suivi_de_dépenses()
