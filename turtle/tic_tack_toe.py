import sys
#first to print the board
def printing_board(mylist):
    print(' ')
    for i in range(3):
        print("                                                   "+str(mylist[i]))
#second to take player1 and player 2 input 
def player_input(position,mylist,player):
    if position <=3 and position>=1:
        mylist[0][position-1]=player
    elif position>=4 and position <=6:
        mylist[1][position-4]=player
    elif position>=7 and position<=9:
        mylist[2][position-7]=player
    else:
        print("                                               PLEASE ENTER A VALID INPUT")
# third to ask position to player
def asking_position(mylist,player):
    position=input()
    player_input(position,mylist,player)
    print(' ')
    printing_board(mylist)
    print(' ')
#fourth to check the winner
def winner(mylist,player):
    t='1'
    x=0
    o=0
    for i in range(3):
        if mylist[i][0]==mylist[i][1]==mylist[i][2]=='X':
            t='0'
            x=1
        elif mylist[i][0]==mylist[i][1]==mylist[i][2]=='O':
            t='0'
            o=1
        elif mylist[0][i]==mylist[1][i]== mylist[2][i]=='X':
            t='0'
            x=1
        elif mylist[0][i]==mylist[1][i]== mylist[2][i]=='O':
            t='0'
            o=1
    if mylist[0][0]==mylist[1][1]==mylist[2][2]=='X':
        t='0'
        x=1
    elif mylist[0][0]==mylist[1][1]==mylist[2][2]=='O':
        t='0'
        o=1
    elif mylist[0][2]==mylist[1][1] == mylist[2][0]=='X' :
        t='0'
        x=1
    elif mylist[0][2]==mylist[1][1] == mylist[2][0]=='O':
        t='0'
        o=1
    
    if x==1:
        return x
    else:
        return o
    

# the suggestion table
def suggestion():
    print("                                                                                               the positions are as follows")
    print("                                                                                                        [1,2,3]")
    print("                                                                                                        [4,5,6]")
    print("                                                                                                        [7,8,9]")
    print(' ')


#the main function

print(" ")
print('                                             HELLO, WELCOME TO TIC TACK TOE GAME         ')
print(' ')
print('                                     Would you like to play the game or do you wish to exit.')
print(' ')
x=input('                                       Please press 1 to play the game and 0 to exit: ')
if x==0:
    print(' ')
    print(' ')
    print('                                         thank you, this game will terminate now')
    sys.exit()
print(' ')
print(' ')
print("                                                 Ok then, let's start the game ")
print(' ')
tt=1
value=' '
while tt>0:
    value=raw_input("                                           player1, please select 'X' or 'O': ")
    if value.upper()=='X'or value.upper()=='O':
        tt=0
    else:
        print("                                                  PLEASE ENTER A VALID INPUT ")
player1=value
player2=' '
if player1.upper()=='X':
    player2='O'
    player1=player1.upper()
elif player1.upper()=='O':
    player2='X'
    player1=player1.upper()

print(' ')
print(' ')
mylist=[[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
printing_board(mylist)
print(' ')
q=1
while q>0:
    suggestion()
    print('                                          player1 please enter a position from 1 to 9:')
    print(' ')
    asking_position(mylist,player1)
    suggestion()
    t=winner(mylist,player1)
    if t==1:
        print("                                      Congrats,  player1 won the game.!!! ")
        sys.exit()
    print('                                          player2 please enter a position from 1 to 9:')
    print(' ')
    asking_position(mylist,player2)
    t=winner(mylist,player2)
    if t==1:
        print("                                      Congrats,  player2 won the game.!!! ")
        sys.exit()