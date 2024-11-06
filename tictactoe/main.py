import time


class Board:
    def __init__(self):
        self.board=[["N","N","N"],
                    ["N","N","N"],
                    ["N","N","N"]]
    
    def __str__(self):
        toret="=======\n"
        for i in self.board:
            for k in i:
                toret+=""
                if k=="N":
                    toret+=" "
                else:
                    toret+=k

            toret+="|\n"

        return toret
    
board=Board()
print(board)