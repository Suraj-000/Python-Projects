#The black jack game 

import sys
import random
#The dealer, the player , the coumpter

#shuffling list
def shuffle_list():
    print(" ")
    print("Your cards: "),
    for i in range(2):
        ff=random.choice(input_list)
        player_list.append(ff)
        input_list.remove(ff)
        ff=random.choice(input_list)
        computer_list.append(ff)
        input_list.remove(ff)
    print(player_list)
    print(" ")
    print("Computer's first card: "),
    print(computer_list[0])
    print(" ")
    print("Press y to get another card , n to pass : "),
    tt=raw_input()
    if tt.upper()=='Y':
        y=random.choice(input_list)
        if y==11:
            q=sum(player_list)
            if q+y>21:
                player_list.append(y-10)
            else:
                player_list.append(y)
        input_list.remove(y)
        deal_check()
    else:
        deal_check()

        


#checking the deal
def deal_check():
    p=sum(player_list)
    c=sum(computer_list)
    print("player's cards: "),
    print(player_list)
    print("Computer's cards: "),
    print(computer_list)
    if p>21:
        print("you lost!!")
    elif p>c and p<=21:
        print("you won!!")
    elif p<c:
        print("you lost!!")
    elif p==c:
        print("It's a draw.")


#the main 
input_list=[11,2,3,4,5,6,7,8,9,10,10,10,10]
player_list=[]
computer_list=[]
print ("THE BLACK JACK GAME")
print(" ")
print(" ")
print("Hello, welcome to the black jack game ")
print(" ")
print("press y to play the game, n to exit the game"),
m=1
while m:
    game_input=raw_input()
    if game_input.upper()=='Y' or game_input.upper()=='N':
        m=0
    else:
        print("PLEASE ENTER A VALID INPUT")
if game_input.upper()=='Y':
    shuffle_list()
else:
    print("thank you for playing the game")
    sys.exit()