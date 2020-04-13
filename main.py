import string

class Chess:
	class White():
		class Pawn():
			def __init__(self, position, move):
				self.name = "Pawn"
				self.position= position
				self.ability=[1,2]
				self.alive=True

			def movePiece(self):
				self.position= move

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						self.position=int(placePiece)
						break
		class Rook():
			def __init__(self, position, move):
				self.name = "Rook"
				self.position= position
				self.ability=[1,2,3,4,5,6,7,8,10,20,30,40,50,60,70,80]
				self.alive=True
			def movePiece(self):
				self.position= move

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						self.position=int(placePiece)
						break

	class Black():
		class Pawn():
			def __init__(self, position, move):
				self.name = "Pawn"
				self.position= position
				self.ability=[-1,-2]
				self.alive=True
				
			def movePiece(self):
				self.position= move

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						self.position=int(placePiece)
						break
		class Rook():
			def __init__(self, position, move):
				self.name = "Rook"
				self.position= position
				self.ability=[-1,-2,-3,-4,-5,-6,-7,-8,-10,-20,-30,-40,-50,-60,-70,-80]
				self.alive=True
			def movePiece(self):
				self.position= move

			def possibleMoves(self):
				possibleMove = []
				for abilities in self.ability:
						possibleMove.append(self.position + abilities)
				return possibleMove

			def makeMove(self, placePiece):
				abilities = self.possibleMoves()
				for i in abilities:
					if str(i) == str(placePiece):
						self.position=int(placePiece)
						break
					
				
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

		return whitePieces, blackPieces

	

		

	def playGame(whitePieces, blackPieces):
		board = False
		
		def printBoard(whitePieces,blackPieces, board):

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

			
			for i,j in whitePieces.items():
				for pieces in j:
					board[pieces.position] = pieces.name[0]
			for i,j in blackPieces.items():
				for pieces in j:
					board[pieces.position] = pieces.name[0]
			print('\n')
			print('  8 |{a8}|{b8}|{c8}|{d8}|{e8}|{f8}|{g8}|{h8}|'.format(a8=board[18], b8=board[28], c8=board[38], d8=board[48], e8=board[58], f8=board[68], g8=board[78], h8=board[88]))
			print('  7 |{a7}|{b7}|{c7}|{d7}|{e7}|{f7}|{g7}|{h7}|'.format(a7=board[17], b7=board[27], c7=board[37], d7=board[47], e7=board[57], f7=board[67], g7=board[77], h7=board[87]))
			print('  6 |{a6}|{b6}|{c6}|{d6}|{e6}|{f6}|{g6}|{h6}|'.format(a6=board[16], b6=board[26], c6=board[36], d6=board[46], e6=board[56], f6=board[66], g6=board[76], h6=board[86]))
			print('  5 |{a5}|{b5}|{c5}|{d5}|{e5}|{f5}|{g5}|{h5}|'.format(a5=board[15], b5=board[25], c5=board[35], d5=board[45], e5=board[55], f5=board[65], g5=board[75], h5=board[85]))
			print('  4 |{a4}|{b4}|{c4}|{d4}|{e4}|{f4}|{g4}|{h4}|'.format(a4=board[14], b4=board[24], c4=board[34], d4=board[44], e4=board[54], f4=board[64], g4=board[74], h4=board[84]))
			print('  3 |{a3}|{b3}|{c3}|{d3}|{e3}|{f3}|{g3}|{h3}|'.format(a3=board[13], b3=board[23], c3=board[33], d3=board[43], e3=board[53], f3=board[63], g3=board[73], h3=board[83]))
			print('  2 |{a2}|{b2}|{c2}|{d2}|{e2}|{f2}|{g2}|{h2}|'.format(a2=board[12], b2=board[22], c2=board[32], d2=board[42], e2=board[52], f2=board[62], g2=board[72], h2=board[82]))
			print('  1 |{a1}|{b1}|{c1}|{d1}|{e1}|{f1}|{g1}|{h1}|'.format(a1=board[11], b1=board[21], c1=board[31], d1=board[41], e1=board[51], f1=board[61], g1=board[71], h1=board[81]))
			print('     1 2 3 4 5 6 7 8 ')
			return board


		board = printBoard(whitePieces, blackPieces, board)

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
							
							board[k.position] = ' '

							k.makeMove(placePiece)

							print('New position', k.position)
							board = printBoard(whitePieces,blackPieces, board)
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
							
							board[k.position] = ' '

							k.makeMove(placePiece)

							print('New position', k.position)
							board = printBoard(whitePieces, blackPieces, board)
							if str(pickPiece) != str(k.position):
								Turn = False
					

			


	# Runs
	whitePieces, blackPieces = startingPosition(White, Black)	
	playGame(whitePieces, blackPieces)





			


	