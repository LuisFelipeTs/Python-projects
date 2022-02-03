import random

# tic tac
class TTToeBot:
    def __init__(self, p1, p2):
        self.p1_point = 0
        self.p2_point = 0
        self.p1 = p1
        self.p2 = p2
        self.board_st = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.actual_player = self.chooseFplayer()
        self.round = 1
        self.game_status = "TIC-TAC-TOE"
        self.simb = ["X", "O"]

    def chooseFplayer(self):
        rand_res = 1 # random.randint(0,1)
        print(rand_res)
        if rand_res == 0: self.actual_player = self.p1
        else: self.actual_player = self.p2

    def generateBoard(self):
        board_st = self.board_st
        self.actual_board = """|-----------------------------|
|          {12}           
|            {0}  |  {1}  |  {2}             
|           -------------
|            {3}  |  {4}  |  {5} 
|           -------------
|            {6}  |  {7}  |  {8}
|
|    Quadro de pontos : 
|    {13} - {9}
|    {14} - {10}
|-----------------------------|
Player turn: {11}""".format(board_st[0], board_st[1], board_st[2], board_st[3], board_st[4], board_st[5], board_st[6], board_st[7], board_st[8], self.p1_point, self.p2_point, self.actual_player, self.game_status, self.p1, self.p2 )
        return self.actual_board

    def newMove(self, pos): 
        nw_pos = pos - 1
        if self.round % 2 != 0:
            e_simb = self.simb[0]
            self.board_st[nw_pos] = e_simb
        else:
            e_simb = self.simb[1]
            self.board_st[nw_pos] = e_simb
        return self.checkIfend()
         
    def checkIfend(self): 
        self.round +=1
        board_st = self.board_st
        if self.round > 5:
            if (board_st[0] == board_st[1] == board_st[2]) or (board_st[0] == board_st[3] == board_st[6]) or (board_st[0] == board_st[4] == board_st[8]) or (board_st[1] == board_st[4] == board_st[7]) or (board_st[2] == board_st[5] == board_st[8]) or (board_st[2] == board_st[4] == board_st[6]) or (board_st[3] == board_st[4] == board_st[5]) or (board_st[6] == board_st[7] == board_st[8]):
                self.game_status = "{0} Ganhou!".format(self.actual_player)
                if self.actual_player == self.p1: self.p1_point += 1
                else: self.p2_point += 1
                self.actual_player = "FIM DE JOGO"
                return self.generateBoard()
        if self.round == 10 : "Empate!"
        return self.generateBoard()

    def nwGame(self):
        self.actual_player = self.chooseFplayer()
        self.round = 1
        self.game_status = "TIC-TAC-TOE"
        self.board_st = [1, 2, 3, 4, 5, 6, 7, 8, 9]