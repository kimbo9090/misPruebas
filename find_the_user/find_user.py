'Find out which non-existing username was attempted to log in the most, and therefore has the more invalid login attempts'
'Failed password for invalid user test from 117.144.172.46 port 37574 ssh2 --> An example for what we are looking for'
import re

my_answer = {}
max_val = 0
#Catches anything between user and from.
regex = '(?<=user )(.*)(?=from )'

with open ('input.txt') as handle:
    #Reads input.txt line by line
    inputT = handle.readlines()
for i in range(len(inputT)):
    #We check for the failed error in every line of the input.txt
    if 'Failed password for invalid user' in inputT[i]:
        #If matches, we use the regex to take the user
        match = re.search(regex,inputT[i])
        #If it's the first time we get this user, it's added to a dictionary with value 1.
        if match.group(0) not in my_answer:
            my_answer.update({match.group(0):1})
        #If we already have this user, it's searched in the dict and the value gets incremented by 1
        elif match.group(0) in my_answer:
           my_answer[match.group(0)] += 1
#We print the user with the max value, in this case, stack user.           
print (max(my_answer, key=my_answer.get))

       




