import time
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

def choosemove(board,turn):
    opturn="Y"
    if turn=="Y":
        opturn="R"
    depth=2
    possibles=[]
    for i in range(depth):
        possibles.append([])
    for k in range(7):
        toadd=makemove(board,k,turn)
        if toadd!=False:
            possibles[0].append(toadd)
    
    
    for i in range(1,depth):
        for x,thisboard in enumerate(possibles[i-1]):
            for k in range(7):
                print(i,x,k)
                toadd=makemove(thisboard,k,turn)
                if toadd!=False:
                    possibles[i].append(toadd)
    return possibles
    