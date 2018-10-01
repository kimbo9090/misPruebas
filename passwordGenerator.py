<<<<<<< HEAD
# -*- coding: utf-8 -*-
#!/usr/bin/env python
=======
>>>>>>> 13af3378232822f6e7541552c69705025761cec9
import random
import string
numbers = [1,2,3,4,5,6,7,8,9,0]
abc = string.ascii_lowercase
ABC = string.ascii_uppercase

def passGen():
    password = []
<<<<<<< HEAD
    for i in range(0,12):
        number_or_letter = random.randrange(0,2)
        if number_or_letter == 1:
            # Si es 1, asigna una letra aleatoria
            upper_or_lower = random.randrange(0,2)
                # Se asigna otro numero aleatorio para elegir entre mayusculas o minuscula
            if upper_or_lower == 1:
                    #Si es 1, sera minuscula.
                password.append(random.choice(abc))
            else:
                    #Si es 2, sera mayúscula.
                password.append(random.choice(ABC))
            # Si es 2, asigna un numero aleatorio
        else:
            password.append(random.choice(numbers))
    #El resultado se une en un String
=======
    for i in range(0,9):
        number_or_letter = random.randrange(0,2)
        if number_or_letter == 1:
            upper_or_lower = random.randrange(0,2)
            if upper_or_lower == 1:
                password.append(random.choice(abc))
            else:
                password.append(random.choice(ABC))
        else:
            password.append(random.choice(numbers))
>>>>>>> 13af3378232822f6e7541552c69705025761cec9
    password = ''.join(map(str,password))
    return password

generated_passwords = []
for i in range(0,5):
<<<<<<< HEAD
    # Generamos 5 contraseñas aleatorias
=======
>>>>>>> 13af3378232822f6e7541552c69705025761cec9
    generated_passwords.append(passGen())
print generated_passwords
