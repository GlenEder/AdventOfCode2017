from collections import Counter

with open("input.txt") as f:
	data = f.read()

isVaild = True
totalValid = 0
lines = data.split('\n')
linesLength = len(lines)

for l in range(linesLength):
	isVaild = True
	words = lines[l].split(" ")
	for i in range(len(words)):
		for k in range(len(words)):
			if i != k and Counter(words[i]) == Counter(words[k]):
				isVaild = False

	if isVaild:
		totalValid = totalValid + 1



print(totalValid)