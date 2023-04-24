import UI

# Tutaj będzie pobierane hasło / wybierane z pliku i formatowane, zarządzanie inputem user'a itd. który będzie wysyłany potem do funkcji w UI
def startGame():
    pass

import random
if __name__ == "__main__":
    userInput = input('Menu:\n#1. Podaj słowo\n#2. Losowe słowo\n> ')
    UI.screen(userInput, 0)