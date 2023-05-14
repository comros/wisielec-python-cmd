import UI
import random
from colorama import Fore, Back

# Wybieranie trybu
def startGame(mode):
    
    if mode == '1':
        word = input('Podaj hasło: ').upper().strip()
        wordLength = len(word)
        return word, wordLength
    elif mode == '2':
        with open('words.txt', 'r', encoding='UTF-8') as file:
            rand = random.randint(0,288)
            for i in range(rand):
                file.readline()
            word = file.readline().strip().upper()
            print(word)
            input()
            wordLength = len(word)
            return word, wordLength


# Wyświetlanie liter
def LettersDisplay(mistakes,corr,correct,incorrect):
    letters = 'AĄBCĆDEĘFGHIJKLŁMNŃOPRSTUÓWXYZŻŹ'
    for i in range(0, len(letters)):
                # Wyświetlanie liter przy pierwszej iteracji
                if mistakes == 0 and corr == 0:
                   UI.printWhite(letters[i])
                # Wyświetlanie poprawnych i niepoprawnych liter
                else:
                    flag = 0
                    for j in range(0, len(correct)):
                        if letters[i] == correct[j]:
                            UI.printGreen(letters[i])
                            flag = 1
                    for j in range(0, len(incorrect)):
                        if letters[i] == incorrect[j]:
                            UI.printRed(letters[i])
                            flag = 1
                    if flag == 0:
                        UI.printWhite(letters[i])

# Wprowadzanie liter
def LetterInput(used):
    while True:
        UI.printWhite('')
        letter = input('\nPodaj literę: ').upper()
        if len(letter) > 1:
            UI.printRed("Możesz wpisać tylko jedną literę!"+ Fore.WHITE)
        elif not letter.isalpha():
            UI.printRed("Możesz wpisać tylko litery!"+ Fore.WHITE)
        elif letter in used:
            UI.printRed(f"{letter} już zostało użyte"+ Fore.WHITE)
        else:
            used.append(letter)
            return letter

# Sprawdzanie wprowadzonych liter
def LetterCheck(letter,word,correct,incorrect,corr,mistakes):
    flag2 = 0
    for i in range(0,len(word)):
        if word[i] == letter:
            flag2 = 1
            correct.append(letter)
            corr+=1    
    if flag2 == 0:
        incorrect.append(letter)
        mistakes+=1
    return corr, mistakes

# Przyjmuje ilosc pomylek, jezeli pomylki >= 10 -> sekwencja konca gry / powinna tez obslugiwac wygraną gry
def EndGame(mistakes):
    pass