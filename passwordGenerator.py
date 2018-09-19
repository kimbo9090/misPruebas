import random
import string
numbers = [1,2,3,4,5,6,7,8,9,0]
abc = string.ascii_lowercase
ABC = string.ascii_uppercase

def passGen():
    password = []
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
    password = ''.join(map(str,password))
    return password

generated_passwords = []
for i in range(0,5):
    generated_passwords.append(passGen())
print generated_passwords
