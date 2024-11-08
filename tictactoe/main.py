import time
from robot import Robot

class Board:
    def __init__(self):
        self.board=[["N","N","N"],
                    ["N","N","N"],
                    ["N","N","N"]]
    
    def __str__(self):
        toret="  1 2 3\n"
        for x,i in enumerate(self.board):
            toret+=str(x+1)
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
            end=True
            for i in self.board:
                if "N" in i:
                    end=False
            if end:
                return "T"
        return "N"
    
    def makemove(self,turn,pos1,pos2):
        if pos1<=2 and pos1>=0 and pos2<=2 and pos2>=0 and self.board[pos1][pos2]=="N":
            self.board[pos1][pos2]=turn
        else:
            return "N"
        
    

robot=[]
wins=[]
f=open("tictactoe/score.txt","r")
score=f.read()
f.close
score2=[]
toadd=""
for i in score:
    if i!=",":
        toadd+=i
    else:
        score2.append(float(toadd))
        toadd=""
print(score2)
t=time.time()
tcount=0
tadvarage=0
for i in range(1000):
    robot.append(Robot(score2))
    wins.append(0)
print(max((1,2,3)))
count=0
count2=0
gens=20

while count<gens:
    count+=1
    for x,robot1 in enumerate(robot):
        for o,robot2 in enumerate(robot):
            if robot1!=robot2:
                board=Board()
                while board.checkwin()=="N":
                    if False:
                        try:
                            pos2=int(input("Enter the x position: "))-1
                            pos1=int(input("Enter the y posiiton: "))-1
                        except:
                            pos2=1000
                            pos1=1000
                        while board.makemove("X",pos1,pos2)=="N":
                            print("That space is invalid")
                            try:
                                pos2=int(input("Enter the x position: "))-1
                                pos1=int(input("Enter the y posiiton: "))-1
                            except:
                                pos2=1000
                                pos1=1000
                    
                    board.makemove("X",robot1.make_choice(board.board,"X")[0],robot1.make_choice(board.board,"X")[1])
                    if count2%10000==0:
                        print(board)
                    board.makemove("O",robot2.make_choice(board.board,"O")[0],robot2.make_choice(board.board,"O")[1])
                    if count2%10000==0:
                        print(board)
                    #time.sleep(0.1)
                if board.checkwin()=="X":
                    wins[x]+=1
                if board.checkwin()=="O":
                    wins[o]+=1
                if count2%10000==0:
                    tcount+=1
                    tadvarage*=1-(1/tcount)
                    tadvarage+=int((time.time()-t)*1000)*(1/tcount)
                    tadvarage=round(tadvarage,3)
                    print(str(int((time.time()-t)*1000))+"ms")
                    print(f"Advarage: {tadvarage}ms")
                    print(f"Predicted time left: {round(tadvarage/1000/60*(((1000**2*gens)-count2)/10000),2)}m")
                    #print(f"Debug advarage: AIM: {tadvarage/1000/60} gens: {(gens-count)}, ((1000**2-count2)/10000)")
                    t=time.time()
                count2+=1
    robot2=[]
    
    for i in range(1000):
        robot2.append(Robot(robot[wins.index(max(wins))].vals))
    if count<gens:
        robot=robot2.copy()
    else:
        robot=robot[wins.index(max(wins))]
        f=open("tictactoe/score.txt","w")
        toret=""
        for i in robot.vals:
            toret+=str(i)+","
        f.write(toret+"\n")
        f.close()
        print(toret)
    print(wins)
    wins=[0]*1000
board=Board()
while board.checkwin()=="N":
    print(board)
    try:
        pos2=int(input("Enter the x position: "))-1
        pos1=int(input("Enter the y posiiton: "))-1
    except:
        pos2=1000
        pos1=1000
    while board.makemove("X",pos1,pos2)=="N":
        print("That space is invalid")
        try:
            pos2=int(input("Enter the x position: "))-1
            pos1=int(input("Enter the y posiiton: "))-1
        except:
            pos2=1000
            pos1=1000
    
    #board.makemove("X",robot1.make_choice(board.board,"X")[0],robot1.make_choice(board.board,"X")[1])
    #print(board)
    board.makemove("O",robot.make_choice(board.board,"O")[0],robot.make_choice(board.board,"O")[1])
    #print(board)
    #time.sleep(0.1)