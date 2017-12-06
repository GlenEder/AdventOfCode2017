class Cord:

	def __init__(self, x, y, num):
		self.x = x
		self.y = y
		self.num = num

	def getX(self): 
		return self.x

	def getY(self):
		return self.y

	def getNum(self):
		return self.num



input = 277678

origin = Cord(0, 0, 1)
cords = [origin]

def getNumber(x, y):
	for i in range(len(cords)):
		if cords[i].getX() == x and cords[i].getY() == y:
			return cords[i].getNum()

	return 0


x = 0
y = 0
number = 0
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

	for k in range(-1, 2):
		for j in range(-1, 2):
			number = number + getNumber(x + k, y + j)

	cords.append(Cord(x, y, number))
	
	if number > input:
		print(number)
		break
	number = 0

	step = step + 1

	#print(x, y, i)

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
			