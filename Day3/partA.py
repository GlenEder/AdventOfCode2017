input = 277678

x = 0
y = 0
step = 0
maxSteps = 1
direction = 6		#6 right, 8 up, 4 left, 2 down like on num pad
lastStepInc = 6 	#last increase direction 

for i in range(input - 1):
	if direction == 6:
		x = x + 1
	elif direction == 8:
		y = y + 1
	elif direction == 4:
		x = x - 1
	elif direction == 2:
		y = y - 1

	step = step + 1

	print(x, y, i)

	if step == maxSteps:
		if direction == 2:
			direction = 6
		elif direction == 6:
			direction = 8
		elif direction == 8:
			direction = 4
		elif direction == 4:
			direction = 2

		if lastStepInc == 6 and direction == 4:
			maxSteps = maxSteps + 1
			lastStepInc = 4
		elif lastStepInc == 4 and direction == 6:
			maxSteps = maxSteps + 1
			lastStepInc = 6

		step = 0
			
print(abs(x) + abs(y))
