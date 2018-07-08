exp = 'Mtomas s adadsadsadsads'
def longestWord(sen):
	newMaxi = ''
	maxi = ''
	newString = sen.replace('&','').replace('!','').split()
	for i in newString:
		for j in newString:
			if len(i) > len(j):
				maxi = i
		if len(maxi) > len(newMaxi):
			newMaxi = maxi
	return newMaxi
print longestWord(exp)