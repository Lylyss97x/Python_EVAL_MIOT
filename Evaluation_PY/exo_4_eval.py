def generateList(sentence):

    """
    Générer deux liste utilisant des séparateurs

        Param:
            sentence(string)

        Return:
            final_list(List[List[string]])
    
    """

    final_list = []
    #Utilisation de split pour récupérér les éléments entre espaces
    list_word = sentence.split(' ')

    final_list.append(list_word)
    list_separated = list_word[::]

    for i in range (len(list_separated)):
        #Si l'élément contient une virgule on le remplace par une virgule
        if list_separated[i].__contains__(","):
            list_separated[i] = ","
        else:
            list_separated[i] = " "

    final_list.append(list_separated)
    return final_list


print(generateList("J'ai découvert python cette semaine"))
print(generateList("J'ai découvert, python, cette, semaine"))

