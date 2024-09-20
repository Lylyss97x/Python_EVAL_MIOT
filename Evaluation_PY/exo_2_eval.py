
def additionList(list1, list2):

    """
    Addition de deux listes

        Param:
            list1 ,list2 (List[Int])

        Return:
            result (List[Int])
    
    """

    somme = 0
    result = []

    for list in [list1, list2]:
        for element in list:
            #Je prend en compte leur position dans la liste afin 
            #d'ajouter la bonne unité (centaine, dizaine, etc...)
            somme += (element * (10**((len(list)-1) - list.index(element)) ))

    while somme > 0:
        #Division de la somme par 10 pour récupérer le dernier chiffre
        number = somme % 10  
        result.append(number)
        somme = somme // 10  

    result.reverse()

    return result

print(additionList([8,4,0],[8,3]))