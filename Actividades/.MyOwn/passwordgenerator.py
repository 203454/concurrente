import random

CHARS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9',
            '.', '-', '+', '*', ',',   '.', '-', '+', '*', ',',   '.', '-', '+', '*', ','
            ]


q_list = [random.choice(CHARS) for i in range(15)]


passwordSecure = ""
for word in q_list:
    passwordSecure += str(word)
print(passwordSecure)


def verify_password(password):

    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    carac = ['.', '-', '+', '*', ',']

    caracteresCant = False
    numCant = False
    for i in range(len(carac)):
        if(password.count(carac[i]) == True):
            # print(
            #     "la contraseña tiene los siguientes caracteres especiales: \n" + carac[i])
            caracteresCant = caracteresCant + 1
            # print("cantidad de caracteres: ", caracteresCant)

    for i in range(len(numbers)):
        if(password.count(numbers[i]) == True):
            # print("la contraseña tiene los siguientes numeros: \n" + numbers[i])
            numCant = numCant + 1



    if(caracteresCant > 1 and numCant >= 1):
        print("la contraseña es segura")
    else:
        print("La contraseña no es segura")


print(q_list)
print(passwordSecure)
verify_password(passwordSecure)

