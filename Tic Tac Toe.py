#displaying board
from IPython.display import clear_output
board=[' ']*10
board[0]='#'
examiner_counter=0
def display():
    clear_output()
    global board
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('- - -')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('- - -')
    print(board[1]+'|'+board[2]+'|'+board[3])


#input
player1=''
player2=''
def toss():
    global player1
    global player2
    while player1!='X'and player1!='O':
        print('Player 1, Enter your choice : X or O')
        player1=input()
    if(player1=='X'):
        player2='O'
    else:
        player2='X'
    return(player1,player2)

#testing toss
toss()

#check result function
def examiner():
    global examiner_counter
    global player1
    global player2
    if((board[7]==player1 and board[8]==player1) and board[9]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[7]==player2 and board[8]==player2) and board[9]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[4]==player1 and board[5]==player1) and board[6]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[4]==player2 and board[5]==player2) and board[6]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[1]==player1 and board[2]==player1) and board[3]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[1]==player2 and board[2]==player2) and board[3]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[7]==player1 and board[5]==player1) and board[3]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[7]==player2 and board[5]==player2) and board[3]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[9]==player1 and board[5]==player1) and board[1]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[9]==player2 and board[5]==player2) and board[1]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')    
    if((board[7]==player1 and board[4]==player1) and board[1]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[7]==player2 and board[4]==player2) and board[1]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[8]==player1 and board[5]==player1) and board[2]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[8]==player2 and board[5]==player2) and board[2]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
    if((board[9]==player1 and board[6]==player1) and board[3]==player1):
        examiner_counter=examiner_counter+1
        print('Player 1 has won the game!!')
    if((board[9]==player2 and board[6]==player2) and board[3]==player2):
        examiner_counter=examiner_counter+1
        print('Player 2 has won the game!!')
#game start
print('Lets play')
index=9
for item in [1,2,3,4,5,6,7,8,9]:
    print('Player 1 select your position')
    position=int(input())
    board[position]=player1
    index=index-1
    clear_output()
    display()
    examiner()
    if(index==0 or examiner_counter==1):
        break
    print('Player 2 select your position')
    position=int(input())
    board[position]=player2
    clear_output()
    display()
    index=index-1
    examiner()
    if(index==0 or examiner_counter==1):
        break
if(examiner_counter==0):
    print('-----Draw-----')
    




    