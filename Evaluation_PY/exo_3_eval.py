def powerManual(x, y):

    """
    Calculer la puissance d'un nombre

        Param:
            x (int) : nombre
            y (int) : puissance

        Return:
            result (int) 
    
    """
    result = x

    #Multiplication du nombre y fois, toujours positif
    for i in range (abs(y)-1):
        result *= x

    #Dans le cas ou la puissance est zéro = 1
    if y == 0:
        result = 1

    #Dans le cas ou la puissance est négative
    # on récupère la puissance positive pour la diviser
    elif y < 0:
        result = 1/result

    return result

print(powerManual(2,-3))
