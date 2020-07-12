import random 

class TicTacToe(object):
	def __init__(self):
		self.board = [" ", " "," "," "," "," "," "," "," "]
		self.winning_combos = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                  [0, 3, 6], [1, 4, 7], [2, 5, 8],
                  [0, 4, 8], [2, 4, 6]]
	def show_board(self):
		print(self.board[0] + " - " + self.board[1] + " - " + self.board[2]);
		print(self.board[0+3] + " - " + self.board[1+3] + " - " + self.board[2+3]);
		print(self.board[0+6] + " - " + self.board[1+6] + " - " + self.board[2+6]);
		
	def get_available_moves(self):
		l = []
		for i in range(0,9):
			if self.board[i] == ' ':
				l.append(i)
		return l
		
	def make_human_move(self, i):
		if i<0 or i>8:
			print("Out of board")
			return False
		if self.board[i]=='X' or self.board[i]=='O':
			print("Cell not empty")
			return False
		self.board[i]='X'	
		return	True
	
	def get_human_moves(self):
		l = []
		for i in range(0,9):
			if self.board[i]=='X':
				l.append(i)
		return l
	
	def mini_max(self, depth, agent):
		if depth == 0 or self.game_over()==True:
			pw, aw = self.check_win(self.get_human_moves() , self.get_com_moves())
			if aw == True:
				return 10
			elif pw == True:
				return 0
			else:
				return 5
		if agent == "O":
			ai_max = 0
			for move in self.get_available_moves():
				self.board[move] = "O"
				move_reward = self.mini_max(depth-1, self.change_agent(agent))
				self.board[move] = " "
				ai_max = max(ai_max, move_reward)
			return ai_max
		if agent == "X":
			p_min = 10
			for move in self.get_available_moves():
				self.board[move] = "O"
				move_reward = self.mini_max(depth-1, self.change_agent(agent))
				self.board[move] = " "
				p_min = min(p_min, move_reward)
			return p_min
				
	def make_ai_move(self, depth, agent):
		reward = 5
		next_move = []
		for move in self.get_available_moves():
			print("Making move " + str(move+1))
			self.board[move] = agent
			move_reward = self.mini_max(depth-1, self.change_agent(agent))
			print("Move reward " + str(move_reward))
			self.board[move] = " "
			if move_reward > reward:
				next_move = [move]
				break
			elif move_reward == reward:
				reward = max(move_reward, reward)
				next_move.append(move)
		l = len(next_move)
		if l==1:
			return next_move[0]
		elif l > 1:
			n = random.randint(0,l-1)
			return next_move[n]
		else:
			mv = self.get_available_moves()
			l = len(mv)
			n = random.randint(0, l-1)
			return mv[n]
					
	def game_over(self):
		pw, aw = self.check_win(self.get_human_moves() , self.get_com_moves())
		if len(self.get_available_moves())==0:
			return True
		elif (pw==True or aw==True):
			return True
		else:
			return False
	
	def change_agent(self,agent):
		if agent=="X":
			return "O"
		else:
			return "X"
	def get_com_moves(self):
		l = []
		for i in range(0,9):
			if self.board[i]=='O':
				l.append(i)
		return l
				
	def check_win(self, player_moves, ai_moves):
		player_win = True
		for combo in self.winning_combos:
			player_win = True
			for e in combo:
				if e not in player_moves:
					player_win = False
					break
			if player_win == True:
				break
		
		ai_win = True
		for combo in self.winning_combos:
			ai_win = True
			for e in combo:
				if e not in ai_moves:
					ai_win = False
					break
			if ai_win == True:
				break
		
		return player_win, ai_win
 
		

ttt = TicTacToe()
while ttt.game_over()!=True:
	x = input("Choose a cell to move\n")
	x = int(x)
	if (ttt.make_human_move(x-1)==False):
		continue
	if ttt.game_over()==True:
		break
	move = ttt.make_ai_move(8, "O")
	ttt.board[move] = "O"
	print("Computer chose - " + str (move+1))
	ttt.show_board()
