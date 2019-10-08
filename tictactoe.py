import random
import sys
"""This is the simple well-known game. Tic tac toe. First you will be asked to pick a number from 1 to 20, and if your number will be greater than computer's number you will start the game. 'X' always starts. You are choosing the field on the board by entering number from 1 to 9."""

def printBoard(board):
	
	"""Prints the game board"""
	
	print(board[1] + '|' + board[2] + '|' + board[3])
	print('-+-+-')
	print(board[4] + '|' + board[5] + '|' + board[6])
	print('-+-+-')	
	print(board[7] + '|' + board[8] + '|' + board[9] + "\n\n")
	
def fullBoard(board):
	
	"""Checks if there are still empty fields on the board"""
	
	
	if ' ' not in board.values():
		print("The board is full. It's a tie!")
		return True
	else:
		return False
		
def cleanBoard(board):
	for field in board:
		board[field] = ' '
	
	

def turnChoice():
	
	"""Invites user to pick the number to start the game"""
	
	comp_choice = random.randint(1, 20)
	human_choice = int(input("Please input number from 1 to 20: "))
	while human_choice not in range(1, 21):
		human_choice = int(input("You should pick number from 1 to 20. Please input correct one: "))
	if human_choice > comp_choice:
		return "X"
	else: 
		return "O"

def Victory(board):
	
	"Checks if user or computer won"""
	
	if board[1] == board[2] == board[3] != ' ' or board [4] == board[5] == board[6] != ' ' or board[7] == board[8] == board[9] != ' '  or board[1] == board[4] == board[7] != ' ' or board[2] == board[5] == board[8] != ' ' or board[3] == board[6] == board[9] != ' ' or board[1] == board[5] == board[9] != ' ' or board[3] == board[5] == board[7] != ' ':
		return True

def Opponent_Victory(board, field):
	
	"""Checks if user can won in next turn"""
	
	if turn == "X":
		board[field] = "O"
		if Victory(board):
			board[field] = ' '
			return True
		else:
			board[field] = ' '
			return False
	elif turn == "O":
		board[field] = "X"
		if Victory(board):
			board[field] = ' '
			return True
		else:
			board[field] = ' '
			return False
def five_is_free(board, turn):
	
	"Checks if field number 5 is free"""
	
	if 5 in possible_moves:
		board[5] = turn
		possible_moves.remove(5)
		return True
	
def corner_free(board, turn):
	
	"Checks if corner fields are free"""
	
	for field in (1, 3, 7, 9):
		if field in possible_moves:
			board[field] = turn
			possible_moves.remove(field)
			return field
	else:
		return False
	
def middle_free(board, turn):
	
	"Checks if middle fields(2,4,6,8) are free"""
	
	for field in (2, 4, 6, 8):
		if field in possible_moves:
			board[field] = turn
			possible_moves.remove(field)
			return field
	else:
		return False
		
def computer(turn, possible_moves):
	
	"""Computer's turn. First it checks whether victory is possible in this turn, then it checks whether user's victory is possible in next turn. Then it checks if field number 5 is still free. Then checks the corners and then middle fields"""
	
	for field in possible_moves:
		board[field] = turn
		if Victory(board):
			if turn == "X":
				turn = "O"
			else:
				turn = "X"
			possible_moves.remove(field)
			return turn					
			
		else:
			board[field] = ' '
			
	for field in possible_moves:
		board[field] = turn			
		if Opponent_Victory(board, field):
			board[field] = turn
			if turn == "X":
				turn = "O"
			else:
				turn = "X"
			possible_moves.remove(field)
			return turn				
		else:
			board[field] = ' '
			
	if corner_free(board, turn):
		if turn == "X":
			turn = "O"
		else:
			turn = "X"
		return turn
	
	elif five_is_free(board, turn):
		if turn == "X":
			turn = "O"
		else:
			turn = "X"
		return turn
	elif middle_free(board, turn):
		if turn == "X":
			turn = "O"
		else:
			turn = "X"
		return turn		
			
	
		
	if turn == "X":
		turn = "O"
	else:
		turn = "X"
	
	return turn


def User(turn, possible_moves):
	move = int(input("Please enter number of field: "))
	while move not in range(1, 10):
		move = int(input("Please enter number only from 1 to 9: "))
	while move not in possible_moves:
		move = int(input("The field you have chosen is taken. Please enter another one: "))
	else:
		board[move] = turn
		possible_moves.remove(move)
		if turn == 'X':
			turn = 'O'
		else:
			turn = 'X'
	printBoard(board)
	return turn

while True:
	
	board = { 1: ' ', 2: ' ', 3: ' ',
		  4: ' ', 5: ' ', 6: ' ',
		  7: ' ', 8: ' ', 9: ' '}
	
	possible_moves = [x for x in range(1, 10)]	

	print("This is the simple well-known game. Tic tac toe.\nFirst you will be asked to pick a number from 1 to 20, and if your number will be greater than computer's number you will start the game. \n'X' always starts.\nYou are choosing the field on the board by entering number from 1 to 9.\n\n")
	
	printBoard(board)
	
	start = turnChoice()
	
	print("You are " + start + "\n\n")
	
	turn = "X"
	if start == "X":
		while True:
			turn = User(turn, possible_moves)
			if Victory(board):
				print("You have beaten the computer")
				break
			if fullBoard(board):			
				break
			
			turn = computer(turn, possible_moves)
			print("After computer's turn: ")
			printBoard(board)
			if Victory(board):
				print("You were beaten by the computer")
				break
			if fullBoard(board):			
				break		
	else:
		while True:
			turn = computer(turn, possible_moves)
			print("After computer's turn: ")
			printBoard(board)
			if Victory(board):
				print("You were beaten by the computer")
				break		
			if fullBoard(board):			
				break
			
			turn = User(turn, possible_moves)
			if Victory(board):
				print("You have beaten the computer")
				break		
			if fullBoard(board):			
				break		
		
	start_again = input("Do you want to play again? ")
	
	cleanBoard(board)
	print("\n\n\n\n\n")
	if start_again.lower() != 'yes':
		print("Thank you for the game! Bye!")
		break
		
