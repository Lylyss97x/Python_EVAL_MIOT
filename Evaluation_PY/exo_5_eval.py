import random

def guessNumber():

    """
    Faire Deviner à l'algorithme le nombre en tête par des indications
    
    """

    userInput = None
    number_attempt = 0
    min_value = -1
    max_value = 100
    list_attempts = []

    while userInput != "G":
        
        #Choisir un nombre aléatoire qui n'a pas déjà été essayé
        # et qui est compris entre les valeurs déjà entré
        while number_attempt in list_attempts \
            or not min_value < number_attempt < max_value:
            number_attempt = random.randint(0,100)

        list_attempts.append(number_attempt)
        userInput = input(f"Le script propose {number_attempt} ... +, - ou G ?")

        if userInput == 'G':
            print("C'est gagné")
            break

        elif userInput == "+":
            min_value = number_attempt
            print (f"la valeur doit être comprise entre {min_value} et {max_value}")

        elif userInput =="-":
            max_value = number_attempt
            print (f"la valeur doit être comprise entre {min_value} et {max_value}")

        if max_value - min_value == 1 :
            raise ValueError ("Vous êtes en train de tricher stop")
        
guessNumber()
