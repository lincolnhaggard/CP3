import time
#board is rotated
board=[["WR","WK","WB","WC","WQ","WB","WK","WR"],
        ["WP","WP","WP","WP","WP","WP","WP","WP"],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["","","","","","","",""],
        ["BP","BP","BP","BP","BP","BP","BP","BP"],
        ["BR","BK","BB","BC","BQ","BB","BK","BR"],]
turn="W"
        

def print_board(board):
    toret="  0 1 2 3 4 5 6 7\n"
    color=(53, 181, 72)
    conversion={"P":"♙ ",
                "C":"♔ ",
                "K":"♘ ",
                "Q":"♕ ",
                "R":"♖ ",
                "B":"♗ ",
    }
    
    for y,x in enumerate(board):
        toret+=f"{y} "
        for square in x:
            toret+=f"\x1B[48;2;{color[0]};{color[1]};{color[2]}m"
            if color == (53, 181, 72):
                color=(199, 212, 201)
            else:
                color=(53, 181, 72)
            
            if square!="":
                if square[0]=="B":
                    toret+=f"\x1B[38;2;{255};{0};{0}m"
                else:
                    toret+=f"\x1B[38;2;{0};{0};{255}m"
                try:
                    toret+=conversion[square[1]]
                except:
                    toret+="  "
            else:
                toret+="  "
            toret+="\x1B[0m"
        toret+=f" {y}\n\x1B[0m"
    
        if color == (53, 181, 72):
            color=(199, 212, 201)
        else:
            color=(53, 181, 72)
        toret+="\x1B[0m"
    toret+="  0 1 2 3 4 5 6 7"
    return toret

def other_turn(turn):
    if turn=="W":turn="B"
    else:turn="W"
    return turn
     
def find_piece(piece,board):
    for x,row in enumerate(board):
        for y,square in enumerate(row):
            if square==piece:
                return str(x)+str(y)

def push_board(board,move):
    coords=tuple(map(int,tuple(move)))
    newboard=[]
    for i in board:
        newboard.append(i.copy())
    newboard[coords[2]][coords[3]]=newboard[coords[0]][coords[1]]
    newboard[coords[0]][coords[1]]=""
    if newboard[coords[2]][coords[3]]=="WP" and coords[2]==7:
       newboard[coords[2]][coords[3]]="WQ" 
    if newboard[coords[2]][coords[3]]=="BP" and coords[2]==0:
       newboard[coords[2]][coords[3]]="BQ" 
    return newboard

def g_check(board,turn,move):
    newboard=push_board(board,move)
    king=find_piece(turn+"C",newboard)
    moves=legal_moves(newboard,other_turn(turn),False)
    for move in moves:
        if move[2:]==king:
            return False
    return True

def legal_moves(board,turn,check=True):
    moves=[]
    for x,row in enumerate(board):
        for y,square in enumerate(row):
            
            if square!="":
                if square[0]==turn:
                    if square[1]=="R":
                        for dire in ("up","left","right","down"):
                            for i in range(1,9):
                                if dire=="right":
                                    nextsquare=(x+i,y)
                                if dire=="left":
                                    nextsquare=(x-i,y)
                                if dire=="up":
                                    nextsquare=(x,y+i)
                                if dire=="down":
                                    nextsquare=(x,y-i)
                                if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                    break
                                try:
                                    
                                    if board[nextsquare[0]][nextsquare[1]]=="":
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                    elif board[nextsquare[0]][nextsquare[1]][0]!=turn:
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        break
                                    else:
                                        break
                                except:
                                    break
                    if square[1]=="B":
                        for dire in ("up","left","right","down"):
                            for i in range(1,9):
                                if dire=="right":
                                    nextsquare=(x+i,y+i)
                                if dire=="left":
                                    nextsquare=(x-i,y-i)
                                if dire=="up":
                                    nextsquare=(x-i,y+i)
                                if dire=="down":
                                    nextsquare=(x+i,y-i)
                                if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                    break
                                try:
                                    
                                    if board[nextsquare[0]][nextsquare[1]]=="":
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                    elif board[nextsquare[0]][nextsquare[1]][0]!=turn:
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        break
                                    else:
                                        break
                                except:
                                    break
                    if square[1]=="K":
                        for dire in ((1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)):
                            nextsquare=(x+dire[0],y+dire[1])
                            if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                continue
                            if board[nextsquare[0]][nextsquare[1]]=="":
                                if check:
                                    if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                else:
                                    moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                            elif board[nextsquare[0]][nextsquare[1]][0]!=turn:
                                if check:
                                    if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                else:
                                    moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                    if square[1]=="P":
                        if square[0]=="W":
                            
                            dires=((1,0,False,1,1),(1,-1,True),(1,1,True))
                        elif square[0]=="B":
                            dires=((-1,0,False,6,-1),(-1,-1,True),(-1,1,True))
                        for dire in dires:
                            nextsquare=(x+dire[0],y+dire[1])
                            if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                continue
                            if board[nextsquare[0]][nextsquare[1]]=="":
                                if not dire[2]:
                                    if check:
                                        if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                    else:
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                    if dire[3]==x and board[nextsquare[0]+dire[4]][nextsquare[1]]=="":
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]+dire[4]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]+dire[4]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]+dire[4]}{nextsquare[1]}")
                            elif board[nextsquare[0]][nextsquare[1]][0]!=turn and dire[2]:
                                if check:
                                    if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                else:
                                    moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                    if square[1]=="Q":
                        for dire in ("up","left","right","down","rup","rleft","rright","rdown"):
                            for i in range(1,9):
                                if dire=="right":
                                    nextsquare=(x+i,y+i)
                                if dire=="left":
                                    nextsquare=(x-i,y-i)
                                if dire=="up":
                                    nextsquare=(x-i,y+i)
                                if dire=="down":
                                    nextsquare=(x+i,y-i)
                                if dire=="rright":
                                    nextsquare=(x+i,y)
                                if dire=="rleft":
                                    nextsquare=(x-i,y)
                                if dire=="rup":
                                    nextsquare=(x,y+i)
                                if dire=="rdown":
                                    nextsquare=(x,y-i)
                                if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                    break
                                try:
                                    
                                    if board[nextsquare[0]][nextsquare[1]]=="":
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                    elif board[nextsquare[0]][nextsquare[1]][0]!=turn:
                                        if check:
                                            if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                                moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        else:
                                            moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                        break
                                    else:
                                        break
                                except:
                                    break
                    if square[1]=="C":
                        for dire in ((1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)):
                            nextsquare=(x+dire[0],y+dire[1])
                            if nextsquare[0]<0 or nextsquare[0]>7 or nextsquare[1]<0 or nextsquare[1]>7:
                                continue
                            if board[nextsquare[0]][nextsquare[1]]=="":
                                if check:
                                    if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                else:
                                    moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                            elif board[nextsquare[0]][nextsquare[1]][0]!=turn:
                                if check:
                                    if g_check(board,turn,f"{x}{y}{nextsquare[0]}{nextsquare[1]}"):   
                                        moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                                else:
                                    moves.append(f"{x}{y}{nextsquare[0]}{nextsquare[1]}")
                        
    return moves

def score(board,turn,aturn):
    points=0
    values={"P":100,"K":500,"R":1500,"B":1000,"Q":3000,"C":100000000000}
    posco={"P":{"B":[[0]*8,
                     [2500]*8,
                     [1000]*8,
                     [100]*8,
                     [50]*8,
                     [20]*8,
                     [0]*8,
                     [0]*8],
                "W":[[0]*8,
                     [0]*8,
                     [20]*8,
                     [50]*8,
                     [100]*8,
                     [1000]*8,
                     [2500]*8,
                     [0]*8],     },
            "K":[[15,10,5 ,5 ,5 ,5 ,5 ,15],
                 [10,0 ,0 ,0 ,0 ,0 ,0 ,10],
                 [5 ,0 ,25,25,25,25,0 ,5 ],
                 [5 ,0 ,25,50,50,25,0 ,5 ],
                 [5 ,0 ,25,50,50,25,0 ,5 ],
                 [5 ,0 ,25,25,25,25,0 ,5 ],
                 [10,0 ,0 ,0 ,0 ,0 ,0 ,10],
                 [15,10,5 ,5 ,5 ,5 ,10,15]],

            "R":[[5 ,10,15,25,25,15,10,5 ],
                 [10,10,10,15,15,10,10,10],
                 [15,10,15,10,10,15,10,15],
                 [25,15,10,5 ,5 ,10,15,25],
                 [25,15,10,5 ,5 ,10,15,25],
                 [15,10,15,10,10,15,10,15],
                 [10,10,10,15,15,10,10,10],
                 [5 ,10,15,25,25,15,10,5 ]],

            "B":[[5 ,10,15,15,15,15,10,5 ],
                 [10,0 ,5 ,5 ,5 ,5 ,0 ,10],
                 [15,5 ,15,15,15,15,5 ,15],
                 [15,5 ,15,10,10,15,5 ,15],
                 [15,5 ,15,10,10,15,5 ,15],
                 [15,5 ,15,15,15,15,5 ,15],
                 [10,0 ,5 ,5 ,5 ,5 ,0 ,10],
                 [5 ,10,15,15,15,15,10,5 ]],
            "Q":[[0 ,0 ,5 ,5 ,5 ,5 ,0 ,0 ],
                 [0 ,15,15,15,15,15,15,0 ],
                 [5 ,15,25,25,25,25,15,5 ],
                 [5 ,15,25,50,50,25,15,5 ],
                 [5 ,15,25,50,50,25,15,5 ],
                 [5 ,15,25,25,25,25,15,5 ],
                 [0 ,15,15,15,15,15,15,0 ],
                 [0 ,0 ,5 ,5 ,5 ,5 ,0 ,0 ]],
            "C":[[10,15,25,15,15,25,15,10],
                 [15,5 ,5 ,5 ,5 ,5 ,5 ,15],
                 [25,5 ,0 ,0 ,0 ,0 ,5 ,25],
                 [15,5 ,0 ,0 ,0 ,0 ,5 ,15],
                 [15,5 ,0 ,0 ,0 ,0 ,5 ,15],
                 [25,5 ,0 ,0 ,0 ,0 ,5 ,25],
                 [15,5 ,5 ,5 ,5 ,5 ,5 ,15],
                 [10,15,25,15,15,25,15,10]],
                     }
    
    for x,i in enumerate(board):
        for y,square in enumerate(i):
            if square!="":
                try:
                    if square[0]==turn:
                        points+=values[square[1]]
                        if square[1]=="P":
                            points+=posco[square[1]][aturn][x][y]
                        else:
                            points+=posco[square[1]][x][y]
                    else:
                        points-=values[square[1]]
                        if square[1]=="P":
                            points-=posco[square[1]][aturn][x][y]
                        else:
                            points-=posco[square[1]][x][y]
                    
                except:
                    print(square)
    return points
def tree(board,turn,trueturn,depth=0):
    if depth<=3:
        poses={}
        for move in legal_moves(board,turn):
            newposes=tree(push_board(board,move),other_turn(turn),trueturn,depth+1)
            
            poses[move]=newposes
        if turn!=trueturn:
            if len(list(poses.values()))>0:
                return min(list(poses.values()))
            else:
                return -100000000000
        else:
            if depth==0:
                ma=max(list(poses.values()))
                for i in list(poses.keys()):
                    if poses[i]==ma:
                        return i
            if len(list(poses.values()))>0:
                return max(list(poses.values()))
            else:
                return -100000000000
    else:
        return score(board,trueturn,turn)

while True:
    while True:
        print(print_board(board))
        move=input("\n\nmove: ")
        if move in legal_moves(board,turn):
            board=push_board(board,move)
            if turn=="W":turn="B"
            else:turn="W"
            break
        else:
            print("illegal move")
            print(legal_moves(board,turn))
            continue
    print(print_board(board))
    print("thinking...")
    tim=time.time()
    move=tree(board,turn,turn)
    print(f"{str(round(time.time()-tim,2))} seconds")
    board=push_board(board,move)
    turn=other_turn(turn)
    
    