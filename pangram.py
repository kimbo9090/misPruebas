import string
# 26
# my cat is big
def is_pangram(sentence):
    myList = (map(chr, range(97, 123)))
    dictABC = { i : 0 for i in myList }
    for i in sentence:
    	if i in dictABC.keys():
    		dictABC[i] = 1
    a = sum(dictABC.values())
    if a == 26:
    	print "Es un pangrama."
    else:
    	print "No es un pangrama."
text = "Two driven jocks help fax my big quiz"
print is_pangram(text.lower())
