with open("input.txt") as f:
	data = f.read()

pos = 0
steps = 0
numWords = data.split('\n')
numbers = []
for i in range(len(numWords)):
	numbers.append(int(numWords[i]))


while pos >= 0 and pos < len(numbers):
	oldPos = pos
	instruct = numbers[pos]
	pos = pos + instruct
	if instruct >= 3:
		instruct = instruct - 1
	else:
		instruct = instruct + 1
	numbers[oldPos] = instruct
	steps = steps + 1



print(steps)
