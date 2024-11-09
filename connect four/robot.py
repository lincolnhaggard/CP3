import time
import random
def printboard(board):
    toret=""
    for i in board:
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
def makemove(board,colum,turn):
    done=True
    for i in board:
        if i[colum]=="N":
            done=False
    if done:
        return False
    else:
        tomovex=0
        for x,i in enumerate(board):
            if i[colum]=="N":
                tomovex=x
        newboard=[0]*len(board)
        for x,i in enumerate(board):
            newboard[x]=i.copy()
        newboard[tomovex][colum]=turn
        
        return newboard
    
def checkwin(board,turn):
    for i in board:
        for k in range(4):
            if i[k]==turn and i[k+1]==turn and i[k+2]==turn and i[k+3]==turn:
                return True
    for i in range(6):
        for k in range(3):
            if board[k][i]==turn and board[k+1][i]==turn and board[k+2][i]==turn and board[k+3][i]==turn:
                return True
    for i in range(3):
        for k in range(4):
            try:
                if board[i][k]==turn and board[i+1][k+1]==turn and board[i+2][k+2]==turn and board[i+3][k+3]==turn:
                    return True
                if board[-i][k]==turn and board[-(i+1)][k+1]==turn and board[-(i+2)][k+2]==turn and board[-(i+3)][k+3]==turn:
                    return True
            except:
                print(printboard(board))
    return False
#The actual desicion
def evaluateboard(board,turn):
    score=0
    opturn="Y"
    if turn=="Y":
        opturn="R"
    if checkwin(board,turn):
        score+=1000
    if checkwin(board,opturn):
        score-=1000
    return score


def choosemove(board,turn):
    
    depth=6
    vals=choosemove2(board,turn,depth,turn)
    return vals.index(max(vals))
        

def choosemove2(board,turn,depth,trueturn,count=0):
    if count<depth:
        count+=1
        newlist=[]
        for i in range(7):
            newmove=makemove(board,i,turn)
            if newmove!=False:
                newlist.append(newmove)
        opturn="Y"
        if turn=="Y":opturn="R"
        trueopturn="Y"
        if trueturn=="Y":trueopturn="R"
        for i in range(len(newlist)):
            if checkwin(newlist[i],trueturn):
                newlist[i]=1000
            elif checkwin(newlist[i],trueopturn):
                newlist[i]=-1000
            else:
                newlist[i]=choosemove2(newlist[i],opturn,depth,trueturn,count)
        if count!=1:
            toret=0
            for i in newlist:
                toret+=float(i)/len(newlist)
            return toret
        else:
            return newlist
    else:
        return evaluateboard(board,trueturn)
    