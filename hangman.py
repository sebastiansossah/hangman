
from dataclasses import replace
import string
import random
from words import wordsValues

def getRandom(word):
    #Here we choose a random word of the list 
    word= random.choice(word)
    while word == "-" or word == "":
        word=random.choice(word)
    return  word


def hangman():
    lives_visual_dict = {
        0: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / \\
               |
           """,
        1: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |         / 
               |
            """,
        2: """
                ___________
               | /        | 
               |/        ( )
               |          |
               |          
               |
            """,
        3: """
                ___________
               | /        | 
               |/        ( )
               |          
               |          
               |
            """,
        4: """
                ___________
               | /        | 
               |/        
               |          
               |          
               |
            """,
        5: """
                ___________
               | /        
               |/        
               |          
               |          
               |
            """,
        6: """
               |
               |
               |
               |
               |
            """,
        7: "",
    }

    #Call the function created above
    randomWord=getRandom(wordsValues).upper()
    print(randomWord)
    #Here we separate the letters of the word on a list 
    randomWordLetters= set(randomWord)
    #Here we import the english alphabet
    aplphabet= set(string.ascii_uppercase)
    #Here we going to save all the letters wich used get into on the console
    usedLetters=set()
    #User input

    lives= 7

    while len(randomWordLetters) > 0 and lives>0:
        #Here we print all the letters used by the user 
        print('you have ' ,lives, ' lives. '  ' you have used these letters', ' '.join(usedLetters))

        #On a list comprehension we replace the lettes of the word by a *

        #save the letter if the letter is into the usedLetter, else replace each letter in randomword
        wordList= [letter if letter in usedLetters else '*' for letter in randomWord]
        print('Current word: ', ' '.join(wordList))

        #Here we ask to the user to input the word gessed 
        userLetter=input('Input 1 letter to guess the word: ').upper()

        
        if userLetter in aplphabet or usedLetters:
            usedLetters.add(userLetter)

            if userLetter in randomWordLetters:
                randomWordLetters.remove(userLetter)

            
            else:
                lives=lives-1
        
        if lives==0:
            print('Sorry you die, the word was ', randomWord)
            break
            

        elif userLetter in usedLetters:
            print('you alredy input this letter')
            
        for i in lives_visual_dict:
            if i == lives:
                print(lives_visual_dict[lives])
    print('Congrats you win the word was ', randomWord.capitalize())
        
       



hangman()










    






