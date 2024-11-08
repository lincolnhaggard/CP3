import time
from robot import choosemove

class Game:
    def __init__(self):
        self.board=[["N","N","N","N","N","N","N"],
                    ["N","N","N","N","N","N","N"],
                    ["N","N","N","N","N","N","N"],
                    ["N","N","N","N","N","N","N"],
                    ["N","N","N","N","N","N","N"],
                    ["N","N","N","N","N","N","N"],]
        
    def __str__(self):
        toret=""
        for i in self.board:
            toret+="||"
            for k in i:
                if k=="N":
                    toret+=" "
                else:
                    toret+=k
                toret+="||"
            toret+="\n"
        toret+="  1  2  3  4  5  6  7"
        return toret
    def makemove(self,turn,colum):
        done=True
        for i in self.board:
            if i[colum]=="N":
                done=False
        if done:
            return False
        else:
            tomovex=0
            for x,i in enumerate(self.board):
                if i[colum]=="N":
                    tomovex=x
            self.board[tomovex][colum]=turn
    def checkwin(self):
        for turn in ("R","Y"):
            for i in self.board:
                for k in range(4):
                    if i[k]==turn and i[k+1]==turn and i[k+2]==turn and i[k+3]==turn:
                        return turn
            for i in range(6):
                for k in range(3):
                    if self.board[k][i]==turn and self.board[k+1][i]==turn and self.board[k+2][i]==turn and self.board[k+3][i]==turn:
                        return turn
            for i in range(4):
                for k in range(3):
                    if self.board[i][k]==turn and self.board[i+1][k+1]==turn and self.board[i+2][k+2]==turn and self.board[i+3][k+3]==turn:
                        return turn
                    if self.board[-i][k]==turn and self.board[-(i+1)][k+1]==turn and self.board[-(i+2)][k+2]==turn and self.board[-(i+3)][k+3]==turn:
                        return turn

board=Game()

while board.checkwin()==None:
    print(board)
    colum=int(input("Pick a colum: "))-1
    board.makemove("R",colum)
    print(choosemove(board.board,"Y"))
print(board)
print(board.checkwin())