# Python 2.7
# coding = UTF-8
string = "Hello world!"
def FirstReverse(string):

	array = []
	arrayBack = []

	if not isinstance(string,str):
		return 'Thats not a String'

	if string is None:		
		return 'It cant be null'

	if len(string) == 0:
		return 'It cant be  0'

	if len(string) == 1:
		return 'min 2 chars'

	for i in string:
		array.append(i)

	for i in range(len(string)-1,-1,-1):
		arrayBack.append(array[i])

	str1 = ''.join(arrayBack)
	return str1
# Some tests
print FirstReverse('Copy copy hi hi hi hello')
print FirstReverse(string)
print FirstReverse(None)
print FirstReverse('')
print FirstReverse('a')
print FirstReverse(1)
