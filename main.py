import string


class Chess:
	class Empty():
		def __init__(self):
				self.name = " "
			

	class White():
		class Pawn():
			def __init__(self, position, move):
				self.name = "Pawn"
				self.colour = "White"
				self.position= position
				self.ability=[1,2,11,-9]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece,self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							print(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)

				added = i
				
				if i > 88 or i < 11 or str(i)[1] == "9" or str(i)[1] == "0":
					return False
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False
					


		class Rook():
			def __init__(self, position, move):
				self.name = "Rook"
				self.colour = "White"
				self.position= position
				self.ability=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,-10,-20,-30,-40,-50,-60,-70,-80,-1,-2,-3,-4,-5,-6,-7,-8]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff < 10:
					for j in range(diff-1):
						checkerList.append(j+1)
				if diff >= 10:
					dividedTen = int(diff / 10)
					for j in range(dividedTen-1):
						j = j+1
						j = j*10
						checkerList.append(j)
				if diff < 0 and diff > -10:
					for j in range(abs(diff+1)):
						j= j+1
						j = -j
						checkerList.append(j)
				if diff <= -10:
					dividedTen = int(diff / 10)
					for j in range(abs(dividedTen+1)):
						j = j+1
						j = j*10
						j = -j
						checkerList.append(j)
				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False

		class Bishop():
			def __init__(self, position, move):
				self.name = "Bishop"
				self.colour = "White"
				self.position= position
				self.ability=[11,22,33,44,55,66,77,9,18,27,36,45,54,63,72,-11,-22,-33,-44,-55,-66,-77,-9,-18,-27,-36,-45,-54,-63,-72]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff % 11 == 0:
					howMany = int(diff / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(k)
				if diff > 0 and diff % 9 == 0:
					howMany = int(diff / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(k)
				if diff < 0 and abs(diff) % 9 == 0:
					howMany = int(abs(diff) / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(-k)
				if diff < 0 and diff % 11 == 0:
					print("yo")
					howMany = int(abs(diff) / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(-k)



				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False


		class Knight():
			def __init__(self, position, move):
				self.name = "Knight"
				self.colour = "White"
				self.position= position
				self.ability=[8,12,19,21,-8,-12,-19,-21]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
							
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False

		class Queen():
			def __init__(self, position, move):
				self.name = "Queen"
				self.colour = "White"
				self.position= position
				self.ability=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,-10,-20,-30,-40,-50,-60,-70,-80,-1,-2,-3,-4,-5,-6,-7,
							 -8,11,22,33,44,55,66,77,9,18,27,36,45,54,63,72,-11,-22,-33,-44,-55,-66,-77,-9,-18,-27,-36,-45,
							 -54,-63,-72]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff % 11 == 0:
					howMany = int(diff / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(k)
				if diff > 0 and diff % 9 == 0:
					howMany = int(diff / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(k)
				if diff < 0 and abs(diff) % 9 == 0:
					howMany = int(abs(diff) / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(-k)
				if diff < 0 and diff % 11 == 0:
					print("yo")
					howMany = int(abs(diff) / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(-k)

				if diff > 0 and diff < 9:
					for j in range(diff-1):
						checkerList.append(j+1)
				if diff >= 10 and diff % 10 == 0:
					dividedTen = int(diff / 10)
					for j in range(dividedTen-1):
						j = j+1
						j = j*10
						checkerList.append(j)
				if diff < 0 and diff > -9:
					for j in range(abs(diff+1)):
						j= j+1
						j = -j
						checkerList.append(j)
				if diff <= -10 and diff % 10 == 0:
					dividedTen = int(diff / 10)
					for j in range(abs(dividedTen+1)):
						j = j+1
						j = j*10
						j = -j
						checkerList.append(j)
				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False

		class King():
			def __init__(self, position, move):
				self.name = "+King"
				self.colour = "White"
				self.position= position
				self.ability=[1,9,10,11,-1,-9,-10,-11]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in blackPieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
							
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "Black":
						return True
						
					if board[i].colour == "White":
						print("Thats your piece")
						return False

	class Black():
		class Pawn():
			def __init__(self, position, move):
				self.name = "pawn"
				self.colour = "Black"
				self.position= position
				self.ability=[-1,-2,-11,9]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece,self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							print(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)

				added = i
				
				if i > 88 or i < 11 or str(i)[1] == "9" or str(i)[1] == "0":
					return False
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False
					


		class Rook():
			def __init__(self, position, move):
				self.name = "rook"
				self.colour = "Black"
				self.position= position
				self.ability=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,-10,-20,-30,-40,-50,-60,-70,-80,-1,-2,-3,-4,-5,-6,-7,-8]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff < 10:
					for j in range(diff-1):
						checkerList.append(j+1)
				if diff >= 10:
					dividedTen = int(diff / 10)
					for j in range(dividedTen-1):
						j = j+1
						j = j*10
						checkerList.append(j)
				if diff < 0 and diff > -10:
					for j in range(abs(diff+1)):
						j= j+1
						j = -j
						checkerList.append(j)
				if diff <= -10:
					dividedTen = int(diff / 10)
					for j in range(abs(dividedTen+1)):
						j = j+1
						j = j*10
						j = -j
						checkerList.append(j)
				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False

		class Bishop():
			def __init__(self, position, move):
				self.name = "bishop"
				self.colour = "Black"
				self.position= position
				self.ability=[11,22,33,44,55,66,77,9,18,27,36,45,54,63,72,-11,-22,-33,-44,-55,-66,-77,-9,-18,-27,-36,-45,-54,-63,-72]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff % 11 == 0:
					howMany = int(diff / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(k)
				if diff > 0 and diff % 9 == 0:
					howMany = int(diff / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(k)
				if diff < 0 and abs(diff) % 9 == 0:
					howMany = int(abs(diff) / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(-k)
				if diff < 0 and diff % 11 == 0:
					howMany = int(abs(diff) / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(-k)



				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False


		class Knight():
			def __init__(self, position, move):
				self.name = "knight"
				self.colour = "Black"
				self.position= position
				self.ability=[8,12,19,21,-8,-12,-19,-21]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
							
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False

		class Queen():
			def __init__(self, position, move):
				self.name = "queen"
				self.colour = "Black"
				self.position= position
				self.ability=[1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,70,80,-10,-20,-30,-40,-50,-60,-70,-80,-1,-2,-3,-4,-5,-6,-7,
							 -8,11,22,33,44,55,66,77,9,18,27,36,45,54,63,72,-11,-22,-33,-44,-55,-66,-77,-9,-18,-27,-36,-45,
							 -54,-63,-72]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
				if diff > 0 and diff % 11 == 0:
					howMany = int(diff / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(k)
				if diff > 0 and diff % 9 == 0:
					howMany = int(diff / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(k)
				if diff < 0 and abs(diff) % 9 == 0:
					howMany = int(abs(diff) / 9)
					for j in range(howMany-1):
						k = j+1
						k = k * 9
						checkerList.append(-k)
				if diff < 0 and diff % 11 == 0:
					print("yo")
					howMany = int(abs(diff) / 11)
					for j in range(howMany-1):
						k = j+1
						k = k * 11
						checkerList.append(-k)

				if diff > 0 and diff < 9:
					for j in range(diff-1):
						checkerList.append(j+1)
				if diff >= 10 and diff % 10 == 0:
					dividedTen = int(diff / 10)
					for j in range(dividedTen-1):
						j = j+1
						j = j*10
						checkerList.append(j)
				if diff < 0 and diff > -9:
					for j in range(abs(diff+1)):
						j= j+1
						j = -j
						checkerList.append(j)
				if diff <= -10 and diff % 10 == 0:
					dividedTen = int(diff / 10)
					for j in range(abs(dividedTen+1)):
						j = j+1
						j = j*10
						j = -j
						checkerList.append(j)
				if len(checkerList) != 0:
					for m in checkerList:
						n = position + m
						if board[n].name != " ":
							print("Piece in the way")
							return False				
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False

		class King():
			def __init__(self, position, move):
				self.name = "+king"
				self.colour = "Black"
				self.position= position
				self.ability=[1,9,10,11,-1,-9,-10,-11]
				self.alive=True

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece, board, whitePieces, blackPieces):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						if self.moveCheck(board, placePiece, self.position) == True:
							self.position=int(placePiece)
							placePiece = int(placePiece)
							for i,j in whitePieces.items():
								for h in j:
									if h.position == placePiece:
										j.remove(h)
						else:
							pass
						break

			def moveCheck(self, board, i, position):
				i = int(i)
				position = int(position)
				added = i
				if str(added)[0] == 9 or str(added)[1] == 9 or added > 88:
					return False
				diff = i - position
				print('diff',diff)
				checkerList = []
							
				
				if board[i].name == " ":
					board[i].position = ' '
					return True
				else:
					if board[i].colour == "White":
						return True
						
					if board[i].colour == "Black":
						print("Thats your piece")
						return False
					
				
	def startingPosition(White, Black):
		whitePieces = {}
		blackPieces = {}

		# PAWNS
		whitePawns = []
		for y in range(1, 9):
			position= "{y}2".format(y=y)
			position = int(position)
			whitePawns.append(White.Pawn(position, "0"))
		whitePieces["pawns"] = whitePawns

		blackPawns = []
		for y in range(1, 9):
			position= "{y}7".format(y=y)
			position = int(position)
			blackPawns.append(Black.Pawn(position, "0"))
		blackPieces["pawns"] = blackPawns

		# ROOKS
		whiteRooks = []
		whiteRooks.append(White.Rook(11, "0"))
		whiteRooks.append(White.Rook(81, "0"))
		whitePieces["rooks"] = whiteRooks

		blackRooks = []
		blackRooks.append(Black.Rook(18, "0"))
		blackRooks.append(Black.Rook(88, "0"))
		blackPieces["rooks"] = blackRooks

		# BISHOPS
		whiteBishops = []
		whiteBishops.append(White.Bishop(31, "0"))
		whiteBishops.append(White.Bishop(61, "0"))
		whitePieces["bishops"] = whiteBishops

		blackBishops = []
		blackBishops.append(Black.Bishop(38, "0"))
		blackBishops.append(Black.Bishop(68, "0"))
		blackPieces["bishops"] = blackBishops

		# KNIGHTS
		whiteKnights = []
		whiteKnights.append(White.Knight(21, "0"))
		whiteKnights.append(White.Knight(71, "0"))
		whitePieces["knights"] = whiteKnights

		blackKnights = []
		blackKnights.append(Black.Knight(28, "0"))
		blackKnights.append(Black.Knight(78, "0"))
		blackPieces["knights"] = blackKnights

		# QUEENS
		whiteQueen= []
		whiteKnights.append(White.Queen(41, "0"))
		whitePieces["queen"] = whiteQueen

		blackQueen= []
		blackKnights.append(Black.Queen(48, "0"))
		blackPieces["queen"] = blackQueen

		# KINGS
		whiteKing= []
		whiteKing.append(White.King(51, "0"))
		whitePieces["king"] = whiteKing

		blackKing= []
		blackKing.append(Black.King(58, "0"))
		blackPieces["king"] = blackKing


		return whitePieces, blackPieces

	
	def playGame(whitePieces, blackPieces, Empty):
		board = False
		
		def printBoard(whitePieces,blackPieces, board, Empty):

			if board == False:
				board = {
						18:' ',28:' ',38:' ',48:' ',58:' ',68:' ',78:' ',88:' ',
						17:' ',27:' ',37:' ',47:' ',57:' ',67:' ',77:' ',87:' ',
						16:' ',26:' ',36:' ',46:' ',56:' ',66:' ',76:' ',86:' ',
						15:' ',25:' ',35:' ',45:' ',55:' ',65:' ',75:' ',85:' ',
						14:' ',24:' ',34:' ',44:' ',54:' ',64:' ',74:' ',84:' ',
						13:' ',23:' ',33:' ',43:' ',53:' ',63:' ',73:' ',83:' ',
						12:' ',22:' ',32:' ',42:' ',52:' ',62:' ',72:' ',82:' ',
						11:' ',21:' ',31:' ',41:' ',51:' ',61:' ',71:' ',81:' ',
						}

			for pieces in board:
				board[pieces]= Empty()

			for i,j in whitePieces.items():
				for pieces in j:
					board[pieces.position] = pieces
			for i,j in blackPieces.items():
				for pieces in j:
					board[pieces.position] = pieces

			print('\n')
			print('  8 |{a8}|{b8}|{c8}|{d8}|{e8}|{f8}|{g8}|{h8}|'.format(a8=board[18].name[0], b8=board[28].name[0], c8=board[38].name[0], d8=board[48].name[0], e8=board[58].name[0], f8=board[68].name[0], g8=board[78].name[0], h8=board[88].name[0]))
			print('  7 |{a7}|{b7}|{c7}|{d7}|{e7}|{f7}|{g7}|{h7}|'.format(a7=board[17].name[0], b7=board[27].name[0], c7=board[37].name[0], d7=board[47].name[0], e7=board[57].name[0], f7=board[67].name[0], g7=board[77].name[0], h7=board[87].name[0]))
			print('  6 |{a6}|{b6}|{c6}|{d6}|{e6}|{f6}|{g6}|{h6}|'.format(a6=board[16].name[0], b6=board[26].name[0], c6=board[36].name[0], d6=board[46].name[0], e6=board[56].name[0], f6=board[66].name[0], g6=board[76].name[0], h6=board[86].name[0]))
			print('  5 |{a5}|{b5}|{c5}|{d5}|{e5}|{f5}|{g5}|{h5}|'.format(a5=board[15].name[0], b5=board[25].name[0], c5=board[35].name[0], d5=board[45].name[0], e5=board[55].name[0], f5=board[65].name[0], g5=board[75].name[0], h5=board[85].name[0]))
			print('  4 |{a4}|{b4}|{c4}|{d4}|{e4}|{f4}|{g4}|{h4}|'.format(a4=board[14].name[0], b4=board[24].name[0], c4=board[34].name[0], d4=board[44].name[0], e4=board[54].name[0], f4=board[64].name[0], g4=board[74].name[0], h4=board[84].name[0]))
			print('  3 |{a3}|{b3}|{c3}|{d3}|{e3}|{f3}|{g3}|{h3}|'.format(a3=board[13].name[0], b3=board[23].name[0], c3=board[33].name[0], d3=board[43].name[0], e3=board[53].name[0], f3=board[63].name[0], g3=board[73].name[0], h3=board[83].name[0]))
			print('  2 |{a2}|{b2}|{c2}|{d2}|{e2}|{f2}|{g2}|{h2}|'.format(a2=board[12].name[0], b2=board[22].name[0], c2=board[32].name[0], d2=board[42].name[0], e2=board[52].name[0], f2=board[62].name[0], g2=board[72].name[0], h2=board[82].name[0]))
			print('  1 |{a1}|{b1}|{c1}|{d1}|{e1}|{f1}|{g1}|{h1}|'.format(a1=board[11].name[0], b1=board[21].name[0], c1=board[31].name[0], d1=board[41].name[0], e1=board[51].name[0], f1=board[61].name[0], g1=board[71].name[0], h1=board[81].name[0]))
			print('     1 2 3 4 5 6 7 8 ')
			return board

		board = printBoard(whitePieces, blackPieces, board, Empty)

		play = True
		while play == True:
			print('\n')

			#pickPiece = 11
			Turn = True
			while Turn == True:
				print('White Turn')
				pickPiece = input("Pick a piece (xy) : ")
				for i,j in whitePieces.items():
					for k in j:
						if pickPiece == str(k.position):
							print("You picked:",k.name)
							placePiece = input("Put it where (xy) : ")
							k.makeMove(placePiece, board, whitePieces, blackPieces)
							print('New position', k.position)
							board = printBoard(whitePieces,blackPieces, board, Empty)
							if str(pickPiece) != str(k.position):
								Turn = False

			Turn = True
			while Turn == True:
				print('Black Turn')
				pickPiece = input("Pick a piece (xy) : ")
				
				for i,j in blackPieces.items():
					for k in j:
						if pickPiece == str(k.position):
							print("You picked:",k.name)
							placePiece = input("Put it where (xy) : ")
							k.makeMove(placePiece, board, whitePieces, blackPieces)
							print('New position', k.position)
							board = printBoard(whitePieces, blackPieces, board, Empty)
							if str(pickPiece) != str(k.position):
								Turn = False
					

			


	# Runs
	whitePieces, blackPieces = startingPosition(White, Black)	
	playGame(whitePieces, blackPieces, Empty)