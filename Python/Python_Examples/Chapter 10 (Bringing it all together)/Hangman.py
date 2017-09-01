import random
def hangman(word):
    wrong = 0                               #Number of incorrect letters
    stages = ["_______        ",            #
              "|       |      ",
              "|       O      ",
              "|      /|\     ",
              "|      / \     "]
    rletters = list(word)                   #List of characters in the word word
    board = ["_"] * len(word)               #List of strings, keeps track of hints to player. Creates a _ for every letter in word
    win = False                             #Keeps track of whether or not the player has won the game
    print("Welcome to hangman")
    while wrong < len(stages) -1:           #While the number of incorrect guesses is less than stages(which is basically number of wrong guesses before GO
        print("\n")                         #New Line
        msg = "Guess a letter"
        char = input(msg)                   #Get User input
        if char in rletters:                #If the guess is in the word
            cind = rletters.index(char)     #cind(charindex) = the index of rletters that char is at
            board[cind] = char              #Updates the board position at above index to the players guess
            rletters[cind] = '$'            #Changes the same index of rletters to $ So it isn't selected again if the p[layer guesses the same letter again
        else:                               #If the guess is not in the word
            wrong += 1                      #wrong guesses incremented
        print((" ".join(board)))            #Prints the board
        e = wrong + 1                       #Number of wrong guesses (Used below)
        print("\n"                          #Insert a new line between strings in the stages variable
              .join(stages[0: e]))          #Print Strings in the stages list: index[0] - index[e]
        if "_" not in board:                #If there are no more remaining _
              print("You win! it was: ")    #Player wins, print it
              print(" ".join(board))        #Print the board
              win = True                    #Sets win to true
              break                         #Stops running program
    if not win:                             #This is outside of the while loop. so if there are more wrong guesses than available guesses and the player hasn't won
            print("\n"
                  .join(stages[0: len(stages)+1]))
            print("You lose! It was: {}.".format(word))

#Challenge
#Choose a random work
wordSelector = random.randint(0,10)
wordList = ["Jared",
            "Jessica",
            "Jacqueline",
            "Annie",
            "Television"
            "Chair",
            "Apple",
            "PizzaRoll",
            "Keyboard",
            "Python"]
hangman(Jared)
