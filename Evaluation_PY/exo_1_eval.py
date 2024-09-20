import itertools


def pairsThreeEqualsZero(list_number):

    """
    Retourne les combinaisons de trois chiffres permettants d'obtenir
    la somme de zéro

        Param:
            list_number (List[Int])

        Return:
            soluce (List[Tuple])
    
    """

    soluce = []

    #Récupère toutes les combinaisons de trois possibles à partir de la liste
    combinaisons = itertools.combinations(list_number, 3)
    for combinaison in combinaisons:
        result = 0
        for i in range(len(combinaison)):
            result += combinaison[i]

        if result == 0:
            soluce.append(combinaison)

    return soluce

print(pairsThreeEqualsZero([-33,-10,-8,-2,1,4,9,10]))