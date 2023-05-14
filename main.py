import UI
import os
import time
import input_handler

punkty = 0

def Menu():
    os.system('cls')
    word = ''
    correct = []
    incorrect = []
    used = []
    corr=0
    mistakes = 0
    hiddenWord = ''
    UI.printWhite(f'Ilość puntków: {punkty}\n')
    userInput = input('Menu:\n#1. Podaj słowo\n#2. Losowe słowo\n> ')
    if userInput == '1':
        word, wordLength = input_handler.startGame(userInput)
    elif userInput == '2':
        word, wordLength = input_handler.startGame(userInput)
    else:
        os.system('cls')
        UI.printRed('Niepoprawny wybór (dostępne opcje to 1 lub 2)\n')
        time.sleep(2.5)
        Menu()
    os.system('cls')
    UI.screen(word,wordLength,correct,incorrect,used,corr,mistakes,hiddenWord)

if __name__ == "__main__":
    Menu()