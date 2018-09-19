from pwn import *
import re

ip = "34.216.132.109"
port = 9093
context.log_level = "critical"

b = remote(ip,port)
response = b.recv()
print response
regex =  re.findall(r"'(\w)' (\d+)",response)
print '------------------'
first = regex[0][0]
second = int(regex[0][1])

third = regex[1][0]
fourth = int(regex[1][1])

answer = []
answer.append(first * second)
answer.append(third * fourth)
answer.append(str(ord(first) + ord(third)))
answer = ''.join(answer)

print 'Submitting the answer \n'+ answer
print '------------------'

b.sendline(answer)
print b.recv()

b.close()
