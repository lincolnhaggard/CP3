from bot import makemove
"""
what does the game look like
board with pieces

pieces:
    -monk (moves 1 diagonoly or 2 orthagonaly) start with 4◉
    -banker (moves 3 diagonoly or 3 orthagonaly) start with 2◬
    -(a)baker (moves 8 orthagonaly) start with 2◓
    -farmer (moves 8 diagonaly or 1 orthagonaly) start with 2◇
    -trucker (moves 4 diagonaly or 4 orthagonaly) start with 2◈
    -guard (moves exactly 2 orthagonaly then 1, 2 or 3 orthagonaly in a perpendicular direction) start with 2▣
        -guards are special as they can move through pieces but get scared and can't move if there are 3 or more pieces nearby
        | |x| | | |x| |
        |x|x|x| |x|x|x|
        | |x| | | |x| |
        | | | |0| | | |
        | |x| | | |x| |
        |x|x|x| |x|x|x|
        | |x| | | |x| |
    -royal (moves 1 in any direction) start with 1★
    -(d)advisor (moves 2 diagonaly) start with 1◦
{"m":"◉ ","b":"◬ ","a":"◓ ","f":"◇ ","t":"◈ ","g":"▣ ","r":"★ ","d":"◦ "}

mmfggfmm
batdrtab

-wierd win/loose conditions
    -you lose if you have no farmers or truckers
    -you win if you get your advisor next to the enemies royal
    -you win if you get all your monks on the last rank
    -you lose if you have no bakers and 2 bankers
    -you lose if you have no bankers and 2 bakers

add symbols for each piece instead of letters

"""


#rules
print("""
monks    (◉ ) can move 1 diagonally(in an x) or 2 orthogonally(in a +)
bankers  (◬ ) can move 3 diagonally or 3 orthogonally
bakers   (◓ ) can move 8 orthogonally
farmers  (◇ ) can move 8 diagonally or 1 orthogonally
truckers (◈ ) can move 4 diagonally or 4 orthogonally
guards   (▣ ) can move exactly 2 orthogonally then 1, 2, or 3 orthogonally in a perpendicular dircetion
    -guards are special as they can move through pieces 
     but get scared and can't move if there are 3 or more pieces nearby
        | |x| | | |x| |
        |x|x|x| |x|x|x|
        | |x| | | |x| |
        | | | |0| | | |
        | |x| | | |x| |
        |x|x|x| |x|x|x|
        | |x| | | |x| |
royals   (▣ ) can move 1 in any direction
advisors (◦◦) can move 2 diagonally 

if you have no farmers and no truckers you lose the game

if you have no bankers and 2 bakers you lose the game

if you have no bakers and 2 bankers you lose the game

if the enemies advisor is next to your royal you lose the game

if you get all your monks on the last rank you win the game

notation is entered in as (piece you want to move)(were to move) with no spaces
ex: A3A2 would move the piece on the A3 tile to the A2 tile
""")
input(">")

class board:
    def __init__(self):
        self.board=[
            ["bb","ba","bt","bd","br","bt","ba","bb"],
            ["bm","bm","bf","bg","bg","bf","bm","bm"],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["","","","","","","",""],
            ["wm","wm","wf","wg","wg","wf","wm","wm"],
            ["wb","wa","wt","wd","wr","wt","wa","wb"]
            ]
        self.turn="w"
        
    def __str__(self):
        codedic={"m":"◉ ","b":"◬ ","a":"◓ ","f":"◇ ","t":"◈ ","g":"▣ ","r":"★ ","d":"◦◦"}
        color=(53, 181, 72)
        toret="  A B C D E F G H\n"
        for rownum,row in enumerate(self.board):
            toret+=str(rownum+1)+" "
            for square in row:
                toret+=f"\x1B[48;2;{color[0]};{color[1]};{color[2]}m"
                if color == (53, 181, 72):
                    color=(199, 212, 201)
                else:
                    color=(53, 181, 72)
                if square=="":
                    toret+="  "
                else:
                    if square[0]=="b":
                        toret+=f"\x1B[38;2;{0};{0};{0}m"
                    else:
                        toret+=f"\x1B[38;2;{255};{255};{255}m"
                    toret+=codedic[square[1]]
                toret+="\x1B[0m"
            toret+=f" {rownum+1}\n"
            if color == (53, 181, 72):
                color=(199, 212, 201)
            else:
                color=(53, 181, 72)
        toret+="  A B C D E F G H\n"
        return toret
        
    def convertmove(self,move):
        try:
            move=move.strip().lower()
            lettonum={"a":0,"b":1,"c":2,"d":3,"e":4,"f":5,"g":6,"h":7}
            move=((int(move[1])-1),lettonum[move[0]],(int(move[3])-1),lettonum[move[2]])
            return move
        except:
            print("invalid notation")
            return False
        
    def checkmove(self,move):
        if move[0]==move[2] and move[1]==move[3]:
            print("you can't move a piece to the same square")
            return False
        elif len(self.board[move[0]][move[1]])>0 and self.board[move[0]][move[1]][0]==self.turn:
            if len(self.board[move[2]][move[3]])==0:
                return True
            elif self.board[move[2]][move[3]][0]!=self.turn:
                return True
            else:
                print("You can't move onto your own piece")
                return False
        else:
            print("That's not a piece you own")
            return False
            
    def checkorth(self,pos1,pos2,rang):
        if pos1[0]==pos2[0]:
            if abs(pos1[1]-pos2[1])<=rang:
                dirc=1
                if pos1[1]>pos2[1]:
                    dirc=-1
                for i in range(1,abs(pos1[1]-pos2[1])):
                    if self.board[pos1[0]][pos1[1]+(i*dirc)]!="":
                        print("You cannot move through pieces")
                        return False
                return True
        elif pos1[1]==pos2[1]:
            if abs(pos1[0]-pos2[0])<=rang:
                dirc=1
                if pos1[0]>pos2[0]:
                    dirc=-1
                for i in range(1,abs(pos1[0]-pos2[0])):
                    if self.board[pos1[0]+(i*dirc)][pos1[1]]!="":
                        print("You cannot move through pieces")
                        return False
                return True
        return False
        
    def checkdiag(self,pos1,pos2,rang):
        if abs(pos1[0]-pos2[0])==abs(pos1[1]-pos2[1]):
            if abs(pos1[0]-pos2[0])<=rang:
                clear=True
                dirc1=1
                dirc2=1
                if pos1[0]>pos2[0]:
                    dirc1=-1
                if pos1[1]>pos2[1]:
                    dirc2=-1
                for i in range(1,abs(pos1[0]-pos2[0])):
                    if self.board[pos1[0]+(i*dirc1)][pos1[1]+(i*dirc2)]!="":
                        print("You cannot move through pieces")
                        return False
                return True
        return False
        
    def checkguard(self,pos1,pos2):
        count=0
        for i in (-1,0,1):
            for k in (-1,0,1):
                if i!=0 or k!=0:
                    if i+pos1[0]>=0 and i+pos1[0]<=7 and k+pos1[1]>=0 and k+pos1[1]<=7:
                        if self.board[pos1[0]+i][pos1[1]+k]!="" and self.board[pos1[0]+i][pos1[1]+k][0]!=self.turn:
                            count+=1
        if count>=3:
            print("guards get scared if there are 3 or more enemy pieces nearby")
            return False
        if abs(pos1[0]-pos2[0])==2:
            if abs(pos1[1]-pos2[1])==2 or abs(pos1[1]-pos2[1])==1 or abs(pos1[1]-pos2[1])==3:
                return True
        if abs(pos1[1]-pos2[1])==2:
            if abs(pos1[0]-pos2[0])==2 or abs(pos1[0]-pos2[0])==1 or abs(pos1[0]-pos2[0])==3:
                return True
        return False
        
    def checkpiece(self,move):
        







        piece=self.board[move[0]][move[1]][1]
        pos1=(move[0],move[1])
        pos2=(move[2],move[3])
        if piece=="m":
            if self.checkorth(pos1,pos2,2) or self.checkdiag(pos1,pos2,1):
                return True
            else:
                print("monks    (◉ ) can move 1 diagonally(in an x) or 2 orthogonally(in a +)")
        if piece=="b":
            if self.checkorth(pos1,pos2,3) or self.checkdiag(pos1,pos2,3):
                return True
            else:
                print("bankers  (◬ ) can move 3 diagonally or 3 orthogonally")
        if piece=="a":
            if self.checkorth(pos1,pos2,8):
                return True
            else:
                print("bakers   (◓ ) can move 8 orthogonally")
        if piece=="f":
            if self.checkorth(pos1,pos2,1) or self.checkdiag(pos1,pos2,8):
                return True
            else:
                print("farmers  (◇ ) can move 8 diagonally or 1 orthogonally")
        if piece=="t":
            if self.checkorth(pos1,pos2,4) or self.checkdiag(pos1,pos2,4):
                return True
            else:
                print("truckers (◈ ) can move 4 diagonally or 4 orthogonally")
        if piece=="g":
            if self.checkguard(pos1,pos2):
                return True
            else:
                print("""guards   (▣ ) can move exactly 2 orthogonally then 1, 2, or 3 orthogonally in a perpendicular dircetion
-guards are special as they can move through pieces 
 but get scared and can't move if there are 3 or more pieces nearby
    | |x| | | |x| |
    |x|x|x| |x|x|x|
    | |x| | | |x| |
    | | | |0| | | |
    | |x| | | |x| |
    |x|x|x| |x|x|x|
    | |x| | | |x| |""")
        if piece=="r":
            if self.checkorth(pos1,pos2,1) or self.checkdiag(pos1,pos2,1):
                return True
            else:
                print("royals   (▣ ) can move 1 in any direction")
        if piece=="d":
            if self.checkdiag(pos1,pos2,2):
                return True
            else:
                print("advisors (◦◦) can move 2 diagonally ")
        return False
    
    def checkloss(self):
        """
        these first
        -you lose if you have no farmers or truckers
        -you lose if you have no bakers and 2 bankers
        -you lose if you have no bankers and 2 bakers
        
        
        -you win if you get your advisor next to the enemies royal
        -you win if you get all 4 your monks on the last rank
        
        """
        
        wftless=True
        bftless=True
        wb=0
        wa=0
        bb=0
        ba=0
        wmonk=0
        bmonk=0
        wvised=False
        bvised=False
        for rownum,row in enumerate(self.board):
            
            for pnum,piece in enumerate(row):
                if piece=="wf" or piece=="wt":
                    wftless=False
                if piece=="wb":
                    wb+=1
                if piece=="wa":
                    wa+=1
                if rownum==0:
                    if piece=="wm":
                        wmonk+=1
                if piece=="wr":
                    for i in (-1,0,1):
                        for k in (-1,0,1):
                            if i+rownum>=0 and i+rownum<=7 and k+pnum>=0 and k+pnum<=7:
                                if self.board[rownum+i][pnum+k]=="bd":
                                    wvised=True
                if piece=="bf" or piece=="bt":
                    bftless=False
                if piece=="bb":
                    bb+=1
                if piece=="ba":
                    ba+=1
                if rownum==7:
                    if piece=="bm":
                        bmonk+=1
                if piece=="br":
                    for i in (-1,0,1):
                        for k in (-1,0,1):
                            if i+rownum>=0 and i+rownum<=7 and k+pnum>=0 and k+pnum<=7:
                                if self.board[rownum+i][pnum+k]=="wd":
                                    bvised=True
        wloss=wftless
        bloss=bftless
        print("\033c",end="")
        if wftless:
            print("white ran out of truckers and farmers")
        if bftless:
            print("black ran out of truckers and farmers")
        if (wb==2 and wa==0) or (wb==0 and wa==2):
            wloss=True
            print("white didn't balance the bakers and bankers")
        if (bb==2 and ba==0) or (bb==0 and ba==2):
            bloss=True
            print("black didn't balance the bakers and bankers")
        if wmonk==4:
            bloss=True
            print("white enlightened all their monks")
        if bmonk==4:
            wloss=True
            print("black enlightened all their monks")
        if wvised==True:
            wloss=True
            print("black advised white's royal")
        if bvised==True:
            bloss=True
            print("white advised black's royal")
        return wloss,bloss
        
                    
    def move(self,move,convert=True):
        global end
        if convert:
            move=self.convertmove(move)
        if move!=False and self.checkmove(move) and self.checkpiece(move):
            piece=self.board[move[0]][move[1]]
            self.board[move[0]][move[1]]=""
            self.board[move[2]][move[3]]=piece
            if self.turn=="w":
                self.turn="b"
            else:
                self.turn="w"
            losses=self.checkloss()
        else:
            return False
        if losses[0]!=False or losses[1]!=False:
            end=True
board=board()
end=False
turn={"w":"white","b":"black"}
if input("Would you like to play against a robot?(yes/no): ").strip().lower()=="yes":
    while True:
        try:
            dific=int(input("Enter the dificulty(1-3): "))
            if dific==1 or dific==2 or dific==3:
                break
            else:
                print("out of range")
                continue
        except:
            print("not a number")
    while not end:
        print("\033c",end="")
        print(board)
        print(f"{turn[board.turn]}'s turn")
        while board.move(input(">"))==False:pass
        if not end:
            print("\033c",end="")
            print(board)
            print(f"{turn[board.turn]}'s turn")
            board.move(makemove(board.board,board.turn,dific),False)
while not end:
    print("\033c",end="")
    print(board)
    print(f"{turn[board.turn]}'s turn")
    while board.move(input(">"))==False:pass
print(board)