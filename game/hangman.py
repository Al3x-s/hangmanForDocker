#practice casing correctly
#try to dockerize this application
#started at 21:56 pm May 9th
#ended at 23:22
#1 hour goal failed
#pushing with git cli


import random
import art

wordFile = open("words.txt", "r")
unseparatedList = wordFile.readlines()
wordList = unseparatedList[0].split(" ")
word = random.choice(wordList)



def play_game():
    triesLeft = 6
    stage = 0
    
    
    word = random.choice(wordList)
    
    letterDisplay = []
    for character in range(len(word)):
        letterDisplay.append("_")
    indiv = word
    
    print(art.HANGMANPICS[stage])

    for underscore in letterDisplay:
        print(underscore, end="")
        
    while triesLeft != 0:
        
        print('\n')
        print("what letter would you like to try?\n")
        
        userTry = input().lower()
        if not userTry.isalpha():
            print("please enter a letter")
            userTry= input().lower()
            #find a way to check again
        if userTry in word:
            letterAmount = word.count(userTry)
            print('\n\n' + "You are correct there are " + str(letterAmount) + ' cases of ' + userTry)
            for i in range(len(word)):
                if word[i] == userTry:
                    letterDisplay[i] = userTry
                    indiv = indiv.replace(userTry,'')
        
        elif userTry not in word:
            triesLeft -= 1
            stage += 1
            print("\n\nincorrect you have " + str(triesLeft) +" tries left")
            
        print('\n')
        print(art.HANGMANPICS[stage])
        print('\n')
        
        for underscore in letterDisplay:
                print(underscore, end="")
                
        if indiv == '':
            print('\nCongrats you won')
            triesLeft = 0
            

                
                
    print("\nwould you like to play again?\nPress 'y' for yes and 'n' for no\n")
    again = input()
    if again == 'y':
        play_game()
    else:
        print("thanks for playing!")
        exit()
        
        
print("Welcome to hangman\nWould you like to play?\n" + "Press 'y' for yes and 'n' for no")

choice = input()

if choice == "y":
    play_game()