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
		if int(numbers[num]) > max:
			max = int(numbers[num])
		if int(numbers[num]) < min:
			min = int(numbers[num])

	sum = sum + (max - min)
	
print(sum)



