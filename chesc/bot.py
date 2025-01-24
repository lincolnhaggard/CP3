import random
import time

def __str__(board):
        codedic={"m":"◉ ","b":"◬ ","a":"◓ ","f":"◇ ","t":"◈ ","g":"▣ ","r":"★ ","d":"◦◦"}
        color=(53, 181, 72)
        toret="  A  B  C  D  E  F  G  H\n"
        for rownum,row in enumerate(board):
            toret+=str(rownum+1)
            for square in row:
                toret+=f"|\x1B[48;2;{color[0]};{color[1]};{color[2]}m"
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
            toret+="|\n"
            if color == (53, 181, 72):
                color=(199, 212, 201)
            else:
                color=(53, 181, 72)
        return toret
def checkmove(move,board,turn):
    if move[0]==move[2] and move[1]==move[3]:
        return False
    elif len(board[move[0]][move[1]])>0 and board[move[0]][move[1]][0]==turn:
        if len(board[move[2]][move[3]])==0:
            return True
        elif board[move[2]][move[3]][0]!=turn:
            return True
        else:
            return False
    else:
        return False
            
def checkorth(pos1,pos2,rang,board):
    if pos1[0]==pos2[0]:
        if abs(pos1[1]-pos2[1])<=rang:
            dirc=1
            if pos1[1]>pos2[1]:
                dirc=-1
            for i in range(1,abs(pos1[1]-pos2[1])):
                if board[pos1[0]][pos1[1]+(i*dirc)]!="":
                    return False
            return True
    elif pos1[1]==pos2[1]:
        if abs(pos1[0]-pos2[0])<=rang:
            dirc=1
            if pos1[0]>pos2[0]:
                dirc=-1
            for i in range(1,abs(pos1[0]-pos2[0])):
                if board[pos1[0]+(i*dirc)][pos1[1]]!="":
                    return False
            return True
    return False
    
def checkdiag(pos1,pos2,rang,board):
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
                if board[pos1[0]+(i*dirc1)][pos1[1]+(i*dirc2)]!="":
                    return False
            return True
    return False
    
def checkguard(pos1,pos2,board,turn):
    count=0
    for i in (-1,0,1):
        for k in (-1,0,1):
            if i!=0 or k!=0:
                if i+pos1[0]>=0 and i+pos1[0]<=7 and k+pos1[1]>=0 and k+pos1[1]<=7:
                    if board[pos1[0]+i][pos1[1]+k]!="" and board[pos1[0]+i][pos1[1]+k][0]!=turn:
                        count+=1
    if count>=3:
        return False
    if abs(pos1[0]-pos2[0])==2:
        if abs(pos1[1]-pos2[1])==2 or abs(pos1[1]-pos2[1])==1 or abs(pos1[1]-pos2[1])==3:
            return True
    if abs(pos1[1]-pos2[1])==2:
        if abs(pos1[0]-pos2[0])==2 or abs(pos1[0]-pos2[0])==1 or abs(pos1[0]-pos2[0])==3:
            return True
    return False
    
def checkpiece(move,board,turn):
    piece=board[move[0]][move[1]][1]
    pos1=(move[0],move[1])
    pos2=(move[2],move[3])
    if piece=="m":
        if checkorth(pos1,pos2,2,board) or checkdiag(pos1,pos2,1,board):
            return True
    if piece=="b":
        if checkorth(pos1,pos2,3,board) or checkdiag(pos1,pos2,3,board):
            return True
    if piece=="a":
        if checkorth(pos1,pos2,8,board):
            return True
    if piece=="f":
        if checkorth(pos1,pos2,1,board) or checkdiag(pos1,pos2,8,board):
            return True
    if piece=="t":
        if checkorth(pos1,pos2,4,board) or checkdiag(pos1,pos2,4,board):
            return True
    if piece=="g":
        if checkguard(pos1,pos2,board,turn):
            return True
    if piece=="r":
        if checkorth(pos1,pos2,1,board) or checkdiag(pos1,pos2,1,board):
            return True
    if piece=="d":
        if checkdiag(pos1,pos2,2,board):
            return True
    return False
    
def checkloss(board):
        """
        these first
        -you lose if you have no farmers or truckers
        -you lose if you have no bakers and 2 bankers
        -you lose if you have no bankers and 2 bakers
        
        
        -you win if you get your advisor next to the enemies royal
        -you win if you get all 4 your monks on the last rank
        
        """
        wp=0
        bp=0
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
        for rownum,row in enumerate(board):
            
            for pnum,piece in enumerate(row):
                if len(piece)>0:
                    if piece[0]=="w":
                        wp+=1
                    if piece[0]=="b":
                        bp+=1
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
                                if board[rownum+i][pnum+k]=="bd":
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
                                if board[rownum+i][pnum+k]=="wd":
                                    bvised=True
        wloss=wftless
        bloss=bftless
        if (wb==2 and wa==0) or (wb==0 and wa==2):
            wloss=True
        if (bb==2 and ba==0) or (bb==0 and ba==2):
            bloss=True
        if wmonk==4:
            bloss=True
        if bmonk==4:
            wloss=True
        if wvised==True:
            wloss=True
        if bvised==True:
            bloss=True
        return wloss,bloss,wb,bp

def makemove(board,turn,maxdepth=2,depth=0):
    moves=[]
    if depth==0:
        print("thinking 1/3")
    for move1 in range(8):
        for move2 in range(8):
            for move3 in range(8):
                for move4 in range(8):
                    move=(move1,move2,move3,move4)
                    if move!=False and checkmove(move,board,turn) and checkpiece(move,board,turn):
                        newboard=[]
                        for row in board:
                            newrow=[]
                            for piece in row:
                                newrow.append(piece)
                            newboard.append(newrow)
                        piece=newboard[move1][move2]
                        newboard[move1][move2]=""
                        newboard[move3][move4]=piece
                        if depth==0:
                            moves.append(move)
                        if depth<maxdepth:
                            if turn=="w":
                                newturn="b"
                            else:
                                newturn="w"
                            moves.append(makemove(newboard,newturn,maxdepth,depth+1))
                        else:
                            moves.append(newboard)
    if depth==0:
        print("thinking 2/3")
        return score(moves,turn)
        
    #    printall(moves)
    #    input("")
    return moves
def printall(moves):
    for i in moves:
        if isinstance(i[0][0],list):
            printall(i)
        else:
            print(__str__(i))
def score(moves,turn,depth=0):
    for x,i in enumerate(moves):
        if not isinstance(i,tuple):
            if isinstance(i[1][1],list):
                moves[x]=score(i,turn,depth+1)
            else:
                wloss,bloss,wp,bp=checkloss(i)
                if turn=="w":
                    if wloss:
                        moves[x]=-1000
                    elif bloss:
                        moves[x]=1000
                    else:
                        moves[x]=wp-bp
                elif turn=="b":
                    if wloss:
                        moves[x]=1000
                    elif bloss:
                        moves[x]=-1000
                    else:
                        moves[x]=bp-wp
    if depth!=0:
        try:
            return sum(moves)/len(moves)
        except:
            print("an error has happened")
            time.sleep(0.5)
            return 1
    else:
        highscore=0
        highest=None
        for x,i in enumerate(moves):
            if not isinstance(i,tuple):
                if i>highscore:
                    highscore=i
                    highest=moves[x-1]
        return highest