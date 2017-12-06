import copy


def hasHappened(listA, fullList):
	for i in fullList:
		if listA == i:
			return True
	return False

    

with open("input.txt") as f:
		data = f.read()

numberWords = data.split('\t')
numbers = []
for i in range(len(numberWords)):
	numbers.append(int(numberWords[i]))

steps = 0
previousPatterens = [numbers]


while True:
	steps = steps + 1
	newNumbers = copy.copy(previousPatterens[len(previousPatterens) - 1])
	max = newNumbers[0]
	posOfMax = 0
	pos = 0
	#find highest block
	for i in newNumbers:
		pos = pos + 1
		if i > max:
			max = i 
			posOfMax = pos

	#distrubite block
	posOfMax = posOfMax - 1	#acount for starting at index 0
	if(posOfMax < 0):
		posOfMax = 0

	newNumbers[posOfMax] = 0
	while max > 0:
		posOfMax = posOfMax + 1
		if(posOfMax >= len(newNumbers)):
			posOfMax = posOfMax - len(newNumbers)
		newNumbers[posOfMax] = newNumbers[posOfMax] + 1
		max = max - 1

	if hasHappened(newNumbers, previousPatterens):
		print(steps)
		exit(0)
	else:
		print(newNumbers)
		previousPatterens.append(newNumbers)



