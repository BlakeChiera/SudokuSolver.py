string = ""
var = 0

class Setup():
    board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]

def Solve():

	for i in range(9):
		if 0 in Setup.board[i]:
			string = Setup.board[i] 
			
			for i in range(9):
				if string[i] == 0:
					if 1 not in string:
						string[i] = 1
					elif 2 not in string:
						string[i] = 2
					elif 3 not in string:
						string[i] = 3
					elif 4 not in string:
						string[i] = 4
					elif 5 not in string:
						string[i] = 5
					elif 6 not in string:
						string[i] = 6
					elif 7 not in string:
						st ring[i] = 7
					elif 8 not in string:
						string[i] = 8
					elif 9 not in string:
						string[i] = 9

			print(string)
Solve()
