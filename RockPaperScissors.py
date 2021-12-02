from random import randint
import time

Plays = ['Rock', 'Paper', 'Scissors']
comp = Plays[randint(0, 2)]
player = False
Lose = 'You lose!'
Win = 'You Win!'
Tie = 'Tie!'
score = 0
ties = 0
loses = 0
print('You must make new line before continuing in play \nCase Sensitive Answers. \nType "Quit" to end Session')
while player == False:
    player = input('Rock, Paper, Scissors?:  ')
    if player == comp:
        time.sleep(0.5)
        print(Tie)
        ties = ties+1
    elif player == 'Rock':
        time.sleep(0.5)
        if comp == 'Paper':
            print(Lose, comp, 'covers', player)
            loses = loses+1
        else:
            print(Win, player, 'smashes', comp)
            score = score+1
    elif player == 'Paper':
        time.sleep(0.5)
        if comp == 'Scissors':
            print(Lose, comp, 'cut', player)
            loses = loses+1
        else:
            print(Win, player, 'covers', comp)
            score = score+1
    elif player == 'Scissors':
        time.sleep(0.5)
        if comp == 'Rock':
            print(Lose, comp, 'smashes', player)
            loses = loses+1
        else:
            print(Win, player, 'cut', comp)
            score= score+1
    elif player == 'Quit':
        print('Quitter')
        time.sleep(1)
        quit()    
    else:
        print('Invalid input, learn how to spell dweeb')
    print('You have won', score, 'time(s) \nYou have tied', ties,'time(s) \nYou have lost', loses, 'time(s)' )
    player = False
    comp = Plays[randint(0, 2)]
    input()