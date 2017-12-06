with open("input.txt") as f:
		data = f.read()


max = 0;
min = 0;
sum = 0;

for lines in data.split('\n'):
	numbers = lines.split('\t')
	length = len(numbers)
	max = min = int(numbers[0])
	for num in range(length):
		for inner in range(length):
			if num != inner:
				if int(numbers[num]) % int(numbers[inner]) == 0:
					sum = sum + (int(numbers[num]) / int(numbers[inner]))

	
print(sum)