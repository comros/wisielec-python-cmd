import UI
import os
import script

if __name__ == "__main__":
    word = ''
    correct = []
    incorrect = []
    used = []
    corr=0
    mistakes = 0
    hiddenWord = ''
    userInput = input('Menu:\n#1. Podaj słowo\n#2. Losowe słowo\n> ')
    if userInput == '1':
        word, wordLength = script.startGame(userInput)
    elif userInput == '2':
        word, wordLength = script.startGame(userInput)
        pass
    os.system('cls')
    UI.screen(word,wordLength,correct,incorrect,used,corr,mistakes,hiddenWord)