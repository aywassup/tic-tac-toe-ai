from random import randint

class TicTacToe:
	def __init__(self):
		self.lst = []
		self.turn = True
		self.turns = 0
	#creates graph
	def create_graph(self):
		for i in range(3):
			row = []
			for j in range(3):
				row.append("")
			self.lst.append(row)
		return self.lst
	#print graph
	def print_graph(self):
		for i in self.lst:
			print(i)
	#check if spot is taken and make actual turn
	def spot_move(self, x, y):
		spot = self.lst[y][x]
		if spot != "":
			return "This spot is taken"
		else:
			if self.turn == True:
				self.lst[y][x] = "x"
			else:
				self.lst[y][x] = "o"

		self.turns += 1
		self.turn = not self.turn
		return self.lst
	#
	def row_win(self):
		for row in self.lst:
			row_count_x = 0
			row_count_y = 0
			for i in row:
				if i == "x":
					row_count_x += 1
				if i == "o":
					row_count_y += 1
				else:
					continue
			if row_count_x == 3:
				return 1
			if row_count_y == 3:
				return 0

	def column_win(self):
		for i in range(3):
			num_x = 0
			num_o = 0
			for row in self.lst:
				if row[i] == "x":
					num_x += 1
				elif row[i] == "o":
					num_o += 1
			if num_x == 3:
				return 1
			elif num_o == 3:
				return 0

	def priority(self):
		priority = [(1,1), (0,0), (2,0), (0,2), (2,2), (1,0),(2,1), (1,2), (0,2)]
		for tupl in priority:
			x, y = tupl[0], tupl[1]
			if self.lst[y][x] == "":
				return x,y

	def best_move(self):
		#row checks
		for i, row in enumerate(self.lst):
			num_x = 0
			num_o = 0
			for j, char in enumerate(row):
				print('.' + char)
				if char == "x":
					num_x += 1
				if char == "o":
					num_o += 1
				else:
					x = j
					y = i
			if num_o == 2:
				print(1)
				return x, y
			if num_x == 2:
				print(2)
				return x, y
		#column checks
		for j in range(3):
			num_x = 0
			num_o = 0
			for i, row in enumerate(self.lst):
				if row[j] == "x":
					num_x += 1
				elif row[j] == "o":
					num_o += 1
				else:
					x = j
					y = i
			if num_o == 2:
				print(3)
				return x, y
			elif num_x == 2:
				print(4)
				return x, y
		#diagonal checks

		num_x = 0
		num_o = 0

		x, y = None, None
		for i in range(3):
			if self.lst[i][i] == "o":
				num_o += 1
			if self.lst[i][i] == "x":
				num_x += 1
			else:
				x, y = i, i

		if num_o == 2:
			print(5)
			return x, y

		if num_x == 2:
			print(6)
			return x, y


		num_x = 0
		num_o = 0

		for i in range(3):
			if self.lst[i][-i-1] == "o":
				num_o += 1
			if self.lst[i][-i-1] == "x":
				num_x += 1
			else:
				x, y, = i, -i-1

		if num_o == 2:
			return x, y

		if num_x == 2:
			return x, y

			#winning is #1 priority
			#blocking is #2 priority
			#choose best spot.
		return self.priority()
	def possible_win(self):
		for i, row in enumerate(self.lst):
			num_o = 0
			for j, char in enumerate(row):
				print('.' + char)
				if char == "o":
					num_o += 1
				else:
					x = j
					y = i
			if num_o == 2:
				print(1)
				return x, y
		#column checks
		for j in range(3):
			num_o = 0
			for i, row in enumerate(self.lst):
				if row[j] == "o":
					num_o += 1
				else:
					x = j
					y = i
			if num_o == 2:
				print(3)
				return x, y
		#diagonal checks

		num_o = 0

		x, y = None, None
		for i in range(3):
			if self.lst[i][i] == "o":
				num_o += 1
			else:
				x, y = i, i

		if num_o == 2:
			print(5)
			return x, y

		num_o = 0

		for i in range(3):
			if self.lst[i][-i-1] == "o":
				num_o += 1
			else:
				x, y, = i, -i-1

		if num_o == 2:
			return x, y

	def diagonal_win(self):
		if (self.lst[0][0] == "x" and self.lst[1][1] == "x" and self.lst[2][2] == "x") or (self.lst[0][2] == "x" and self.lst[1][1] == "x" and self.lst[2][0] == "x"):
			return 1
		if (self.lst[0][0] == "o" and self.lst[1][1] == "o" and self.lst[2][2] == "o") or (self.lst[0][2] == "o" and self.lst[1][1] == "o" and self.lst[2][0] == "o"):
			return 0

tic = TicTacToe()
tic.create_graph()

win = False

while tic.turns < 9:
	# if player turn: 
	if tic.turn == True:
		x = int(input("x: ")) - 1
		y = int(input("y: ")) - 1

	# if ai turn: 
	else:
		x, y = tic.best_move() 
		#let the comptuer choose x and y
		#winning is #1 priority
		#blocking is #2 priority
		#choose best spot.
	# let the computer choose x and y
	status = tic.spot_move(x, y)
	if status == "This spot is taken":
		print("This spot is taken")
		print(x, y)
		exit()
	else:
		tic.print_graph()
	if tic.row_win() == 1 or tic.column_win() == 1 or tic.diagonal_win() == 1:
		print("Player 1 is the winner (x)")
		win = True
		break
	if tic.row_win() == 0 or tic.column_win() == 0 or tic.diagonal_win() == 0:
		print("Player 2 is the winner (y)")
		win = True
		break
	print()
if win == False:
	print("Draw!")

