import os
import math
import script
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
                if i == 4:
                    printWhite(lines["vertical"]+" "*25+hiddenWord+lines["vertical"]+'\n') 
                else:
                    printWhite(lines["vertical"]+" "*25+"  "*wordLength+lines["vertical"]+'\n')
                

            # Dół okna gry
            printWhite(corners["bottomLeft"]+lines["horizontal"]*25+lines["horizontal"]*wordLength*2+corners["bottomRight"]+'\n')
            printRed(f'\nDługość hasła: {wordLength}\n' + Fore.WHITE)  
        
            # Środkowanie liter
            printWhite(" "*math.floor(((wordLength - 5)/2)))
            
            #Wyświetlanie liter
            script.LettersDisplay(mistakes,corr,correct,incorrect)

            print('\n')
            print(correct)
            print(incorrect)
            print(f'pomyłki: {mistakes}')
            
            #Wpisywanie liter
            letter = script.LetterInput(used)
            
            #sprawdzanie poprawnosci wprowadzanych liter
            corr, mistakes = script.LetterCheck(letter,word,correct,incorrect,corr,mistakes)
            # Nie wiem jeszcze, czy zostanie to tutaj, czy przeniesiemy to do main'a (pod printem infa ma być input użytkownika)
            


            # Debug
            
