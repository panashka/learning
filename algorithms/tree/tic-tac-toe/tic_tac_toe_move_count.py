from array import *
from enum import Enum
import time

class TicTac(Enum):
	TIC = 'X'
	TAC = 'O'
	EMPTY = '_'

# class TicTacBoardInfo():
# 	def __init__(self):
# 		self.empty_count = 0
# 		self.win_count = 0
# 		self.loose_count = 0

def print_arr(arr):
	for r in arr:
		for c in r:
			print(c, end = " ")
		print()

def check_player_board_move(board, tic_tac: TicTac):
	empty_count = 0
	# check horizontal	
	for row in board:	
		win_count = 0
		for val in row:
			if val == TicTac.EMPTY.value:
				empty_count += 1
			elif val == tic_tac.value:
				win_count += 1			

		if win_count == 3:
			return 'win'

	# check vertical
	for col in zip(*board):
		win_count = 0
		for val in col:
			if val == tic_tac.value:
				win_count += 1			

		if win_count == 3:
			return 'win'

	# check diagonals
	win_count = 0
	for i in range(3):
		val = board[i][i]
		if val == tic_tac.value:
			win_count += 1

	if win_count == 3:
		return 'win'

	i = 0
	j = 2
	win_count = 0
	while i<=2 and j>=0:
		val = board[i][j]
		if val == tic_tac.value:
			win_count += 1
		i += 1
		j -= 1

	if win_count == 3:
		return 'win'

	return 'draw' if empty_count == 0 else 'unknown' 


# def check_board(board, tic_tac: TicTac):
# 	tic_tac_board_info = TicTacBoardInfo()
# 	win_counter = 0
# 	loose_counter = 0
# 	# check horizontal	
# 	for row in board:	
# 		for val in row:
# 			if val == TicTac.EMPTY.value:
# 				tic_tac_board_info.empty_count += 1
# 			elif val == tic_tac.value:
# 				win_counter += 1
# 			else:
# 				loose_counter += 1

# 		if win_counter == 2 and loose_counter == 0:
# 			tic_tac_board_info.win_count += 1
# 		elif loose_counter == 2 and win_counter == 0:
# 			tic_tac_board_info.loose_count += 1
# 		win_counter = 0
# 		loose_counter = 0
	
# 	win_counter = 0
# 	loose_counter = 0
# 	# check vertical
# 	for col in zip(*board):
# 		for val in col:
# 			if val == tic_tac.value:
# 				win_counter += 1
# 			elif val != tic_tac.value and val != TicTac.EMPTY.value:
# 				loose_counter += 1

# 		if win_counter == 2 and loose_counter == 0:
# 			tic_tac_board_info.win_count += 1
# 		elif loose_counter == 2 and win_counter == 0:
# 			tic_tac_board_info.loose_count += 1	
# 		win_counter = 0
# 		loose_counter = 0

# 	win_counter = 0
# 	loose_counter = 0
# 	# check diagonal
# 	for i in range(len(board)):
# 		val = board[i][i]
# 		if val == tic_tac.value:
# 			win_counter += 1
# 		elif val != tic_tac.value and val != TicTac.EMPTY.value:
# 			loose_counter += 1

# 	if win_counter == 2 and loose_counter == 0:
# 		tic_tac_board_info.win_count += 1
# 	elif loose_counter == 2 and win_counter == 0:
# 		tic_tac_board_info.loose_count += 1				

# 	win_counter = 0
# 	loose_counter = 0
# 	i = 0
# 	j = 2
# 	while i <= 2 and j >= 0:
# 		val = board[i][j]
# 		if val == tic_tac.value:
# 			win_counter += 1
# 		elif val != tic_tac.value and val != TicTac.EMPTY.value:
# 			loose_counter += 1

# 		i += 1
# 		j -= 1
	
# 	if win_counter == 2 and loose_counter == 0:
# 		tic_tac_board_info.win_count += 1
# 	elif loose_counter == 2 and win_counter == 0:
# 		tic_tac_board_info.loose_count += 1							


# 	return tic_tac_board_info

class BoardResultStatistics():
	def __init__(self):
		self.tic_win_count = 0
		self.tac_win_count = 0
		self.draw_count = 0

	def set_result_count(self, tic_tac: TicTac):
		if tic_tac.value == TicTac.TIC.value:
			self.tic_win_count += 1
		elif tic_tac.value == TicTac.TAC.value:
			self.tac_win_count += 1
		else:
			self.draw_count += 1

	def __str__(self):
		return ' Tic win count: {}\n Tac win count: {}\n Draw count: {}'.format(self.tic_win_count, self.tac_win_count, self.draw_count)

# if current move is 'X' then check board for the next move of 'O'. Otherwise visa versa
def get_next_tic_tac_turn(tic_tac: TicTac):
	return TicTac.TIC if tic_tac.value == TicTac.TAC.value else TicTac.TAC

def count_board_results(board, statistics, current: TicTac):
	for i in range(len(board)):
		for j in range(len(board[i])):
			val = board[i][j]
			if val == TicTac.EMPTY.value:
				board[i][j] = current.value
				# print_arr(board)
				state = check_player_board_move(board, current)
				# print('current player: ' + current.value + ', current state: ' + state)
				if state == 'win':
					statistics.set_result_count(current)
				elif state == 'draw':
					statistics.set_result_count(TicTac.EMPTY)
				else:
					count_board_results(board, statistics, get_next_tic_tac_turn(current))

				# reverse board to the previous state
				board[i][j] = val
				# print('resersed board: ')
				# print_arr(board)


# board = [	['_', 'X', '_'], 
# 			['O', 'X', '_'], 
# 			['X', 'O', '_']
# 		]
board = [	['_', '_', '_'], 
			['_', '_', '_'], 
			['_', '_', '_']
		]
statistics = BoardResultStatistics()
count_board_results(board, statistics, TicTac.TAC)
print(statistics)


# tic_tac_board_info = check_board(board, TicTac.TIC)

# if tic_tac_board_info.win_count > 0:
# 	print('TIC is winning')
# elif tic_tac_board_info.loose_count > 1:
# 	print('TIC is loosing')
# elif tic_tac_board_info.empty_count <= 2:
# 	print('draw')
# else:
# 	print('not known')

