import os
import math
import input_handler
from colorama import Fore, Back

def printWhite(data):
    print(Fore.WHITE, data, end="", sep="")

def printRed(data):
    print(Fore.RED, data, end="", sep="")

def printGreen(data):
    print(Fore.GREEN, data, end="", sep="")


def screen(word,wordLength,correct,incorrect,used,corr,mistakes,hiddenWord):
         
        while True:

            #Ukrycie hasła
            hiddenWord = ""
            correct = list(set(correct))
            for i in range(0, wordLength):
                flag3 = 0
                
                for j in range(0, len(correct)):
                    if word[i] == correct[j]:
                        hiddenWord += word[i]+" "
                        flag3 = 1
                if word[i] == ' ':
                    hiddenWord += "  "
                elif flag3 == 0:
                    hiddenWord += "_ "

            os.system('cls')
            # Tablica do budowy UI (potem usunie się zbędne znaki)
            corners = {
                "upperLeft":     "┌",    #218 np. chr(218)
               "upperRight":    "┐",    #191
               "mediumLeft":    "├",    #195 
               "mediumRight":   "┤",    #180
               "bottomLeft":    "└",    #192
               "bottomRight":   "┘",    #217
               "upperMid":      "┬",    #194
               "midiumMid":     "┼",    #197
               "bottomMid":     "┴"     #193
                }
            lines =   {
               "vertical": "│",         #179
               "horizontal": "─"        #196
                }
            
            # Góra okna gry
            printWhite(f'{corners["upperLeft"]+lines["horizontal"]}WISIELEC{lines["horizontal"]*16+lines["horizontal"]*wordLength*2+corners["upperRight"]}\n')

            # Pętla generująca środek okna gry (za pomocą ilości pomyłek będziemy mogli zmieniać co jest rysowane w środku)
            for i in range(0, 8):
                print(lines["vertical"], end='')

                if i == 1 and mistakes >= 3:
                    printWhite("   ┌────────┐"+" "*12+"  "*wordLength)
                elif i == 2:
                    if mistakes in range(2,4):
                        printWhite("   │"+" "*21+"  "*wordLength)
                    elif mistakes >= 4:
                        printWhite("   │        │"+" "*12+"  "*wordLength)
                    else:
                        printWhite(" "*25+"  "*wordLength)
                elif i == 3:
                    if mistakes in range(2,5):
                        printWhite("   │"+" "*21+hiddenWord)
                    elif mistakes >= 5:
                        printWhite("   │        O"+" "*12+hiddenWord)
                    else:
                        printWhite(" "*25+hiddenWord)
                elif i == 4:
                    if mistakes in range(2,6):
                        printWhite("   │"+" "*21+"  "*wordLength)
                    elif mistakes in range(6,9):
                        printWhite("   │        │"+" "*12+"  "*wordLength)
                    elif mistakes in range(9, 10):
                        printWhite("   │       ╱│"+" "*12+"  "*wordLength)
                    elif mistakes >= 10:
                        printWhite("   │       ╱│╲"+" "*11+"  "*wordLength)
                    else:
                        printWhite(" "*25+"  "*wordLength)
                elif i == 5 and mistakes >= 2:
                    if mistakes in range(2, 7):
                        printWhite("   │"+" "*21+"  "*wordLength)
                    elif mistakes in range(7,8):
                        printWhite("   │       ╱ "+" "*12+"  "*wordLength)
                    elif mistakes >= 8:
                        printWhite("   │       ╱ ╲"+" "*11+"  "*wordLength)
                    else:
                        printWhite(" "*25+"  "*wordLength)
                elif i == 6 and mistakes >= 1:
                    printWhite("  ─┴─"+" "*20+"  "*wordLength)
                elif i == 7:
                    printWhite(" "*25+"  "*wordLength)
                else:
                    printWhite(" "*25+"  "*wordLength)
                print(lines["vertical"])

            # Dół okna gry
            printWhite(corners["bottomLeft"]+lines["horizontal"]*25+lines["horizontal"]*wordLength*2+corners["bottomRight"]+'\n')
            printRed(f'\nDługość hasła: {wordLength}\n' + Fore.WHITE)  
        
            # Środkowanie liter
            printWhite(" "*math.floor(((wordLength - 5)/2)))
            
            #Wyświetlanie liter
            input_handler.LettersDisplay(mistakes,corr,correct,incorrect)

            print('\n')
            print(correct)
            print(incorrect)
            print(f'pomyłki: {mistakes}')
            
            #Wpisywanie liter
            letter = input_handler.LetterInput(used)
            
            #sprawdzanie poprawnosci wprowadzanych liter
            corr, mistakes = input_handler.LetterCheck(letter,word,correct,incorrect,corr,mistakes)
            # Nie wiem jeszcze, czy zostanie to tutaj, czy przeniesiemy to do main'a (pod printem infa ma być input użytkownika)
