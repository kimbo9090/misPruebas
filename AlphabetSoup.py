ABC = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'
,'u','v','w','x','y','z']
inputS = 'hello'
output = 'ehllo'
def bubble_sort(some_list):
	is_sorted = False
	last_sorted_item = len(some_list) -1
	while not is_sorted:
		is_sorted = True

		for i in range(0,len(some_list)-1):
			if some_list[i] > some_list[i+1]:
				some_list[i],some_list[i+1] = some_list[i+1],some_list[i]
				is_sorted = False
		last_sorted_item -= 1		

	return some_list

def AlphabetSoup(inputS):
	array = []
	indexes = []
	array_sorted = []
	for a in inputS:
		array.append(a)
	for i in array:
		for index,a in enumerate(ABC):
			if i is a:
				indexes.append(int(index))
	indexes_sorted = bubble_sort(indexes)
	for i in indexes_sorted:
		array_sorted.append(ABC[i])
	str1 = ''.join(array_sorted)
	return str1
print AlphabetSoup('hooplah')



