import time


class Board:
    def __init__(self):
        self.board=[["N","N","N"],
                    ["N","N","N"],
                    ["N","N","N"]]
    
    def __str__(self):
        toret=" 1 2 3\n"
        for x,i in enumerate(self.board):
            toret+=str(x)
            for k in i:
                toret+="|"
                if k=="N":
                    toret+=" "
                else:
                    toret+=k

            toret+="|\n"

        return toret
    
    def checkwin(self):
        for win in ("X","O"):
            for i in range(3):
                if self.board[i][0]==win and self.board[i][1]==win and self.board[i][2]==win:
                    return win
                if self.board[0][i]==win and self.board[1][i]==win and self.board[2][i]==win:
                    return win
            if self.board[0][0]==win and self.board[1][1]==win and self.board[2][2]==win:
                return win
            if self.board[2][0]==win and self.board[1][1]==win and self.board[0][2]==win:
                return win
        return "N"
    
    def makemove(self,turn,pos1,pos2):
        pass
    
board=Board()
print(board)