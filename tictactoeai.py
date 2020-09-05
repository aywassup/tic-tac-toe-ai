class tictactoe:

	def __init__(self):
		self.array = self.graph()
		self.turn = True

	def graph(self):
		self.array = []
		for i in range(3):
			row = []
			for j in range(3):
				row.append('')
			self.array.append(row)
		return self.array

	def print_graph(self, graph):
		for i in graph:
			print(str(i))

	def piece_place(self, x, y, graph):
		value = graph[int(y)][int(x)]
		if value != "":
			return "Invalid location"
		else:
			if self.turn == True:
				graph[int(y)][int(x)] = 'x'
			else:
				graph[int(y)][int(x)] = 'o'

		self.turn = not self.turn
		return graph
	def winner
tic = tictactoe()
#print(tic.print_graph())

while True:
	graph = tic.piece_place(input("x"),input("y"),tic.graph())
	tic.print_graph(graph)
