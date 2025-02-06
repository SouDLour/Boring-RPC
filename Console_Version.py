import coinProbability as cPB
import time

# About:        
# The Purpose was to avoid using random.choice(); instead assign a randome numerical float
# in which whichever number came out the greatest, meant the user or bot won. That numerical float
# is attached to the user choice of heads or tails and then compared to the bots numerical number.



#Store the wins in a list. Will be used later in a comparison to determines who won.
userWin = []
botWin = []

# Stores number of rounds to be played
flipCount = 0

# The Bot chance at winning the round. Technically given the nature of my code, I didnt need to seperate
# heads and tails into two functions. Why? Because the user has first dibs on the choice of heads or tails.
# Therefore, it would only need to be compared to the bots numerical float value.

def botH():
    #BotHea
    bH = cPB.probability()
    return bH
def botT():
    bT = cPB.probability()
    return bT

# CompareTally: 

#Compares the list to determines whom wins. Whichever list contains the most objects, wins.
def compareTally(usrW,botW):
    if usrW > botW:
        return 'User Won'
    elif usrW < botW:
        return 'Bot Won'
    else:
        return 'Tie'

# The main screen of this terminal Heads v Tails Game
def mainWindow():
    userChoice = input('''
    ==============================      
    |   (H) Heads or (T)Tails    |
    ==============================   
    Enter Choice > ''')

    if userChoice == 'h':
        print('clicked h')
        userHead = cPB.probability()
        botTail = botT()
        if userHead > botTail:
            userWin.append(1)
        elif userHead == botTail:
            userWin.append(1)
            botWin.append(1)
        else:
            botWin.append(1)
        cPB.compare(userHead,botTail)
    elif userChoice == 't':
        print('clicked t')
        userTail = cPB.probability()
        botHead= botH()
        if userTail > botHead:
            userWin.append(1)
        elif userTail == botHead:
            userWin.append(1)
            botWin.append(1)
        else:
            botWin.append(1)
        cPB.compare(userTail,botHead)
    else:
        print('Crashing Application: You Entered Invalid Value')
        quit()


if __name__ == '__main__':

    rounds = int(input('How Many rounds to play? (Enter Number) > '))
    while True:
        mainWindow()
        flipCount += 1
        time.sleep(1)
        if flipCount == rounds:
            print('''
                    ===================
                    {winner}
                    Terminating Program
                    ==================='''.format(winner = compareTally(userWin,botWin)))
            quit()
        else:
            continue
        