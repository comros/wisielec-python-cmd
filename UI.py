import os
import math
from colorama import Fore, Back

def printWhite(data):
    print(Fore.WHITE, data, end="", sep="")

def printRed(data):
    print(Fore.RED, data, end="", sep="")

def printGreen(data):
    print(Fore.GREEN, data, end="", sep="")

def screen(word, mistakes):
    os.system('cls')
    wordLength = len(word)

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
    printWhite(f'{corners["upperLeft"]+lines["horizontal"]}WISIELEC{lines["horizontal"]*16+lines["horizontal"]*wordLength+corners["upperRight"]}\n')

    # Pętla generująca środek okna gry (za pomocą ilości pomyłek będziemy mogli zmieniać co jest rysowane w środku)
    for i in range(0, 8):
        printWhite(lines["vertical"]+" "*25+" "*wordLength+lines["vertical"]+'\n')    

    # Dół okna gry
    printWhite(corners["bottomLeft"]+lines["horizontal"]*25+lines["horizontal"]*wordLength+corners["bottomRight"]+'\n')
    
    leters = 'AĄBCĆDEĘFGHIJKLŁMNŃOPRSTUÓWXYZŻŹ'

    # Środkowanie liter
    printWhite(" "*math.floor(((wordLength - 5)/2)))
    for i in range(0, len(leters)):
        # Tutaj można dodać warunek sprawdzający, czy litera jest odgadnięta (poprawna lub nie) i przypisać kolor
        printWhite(leters[i])

    # Nie wiem jeszcze, czy zostanie to tutaj, czy przeniesiemy to do main'a (pod printem infa ma być input użytkownika)
    info = '\n\nPodaj literę: ' 
    printWhite(info)


    # Debug
    printRed(f'\nDługość hasła: {wordLength}' + Fore.WHITE) 
