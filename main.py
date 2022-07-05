


print("Welcome to Hangman!")
print("Please select from the options below.\n")
print("s- start the game")
print("d- change difficulty")
print("q- quit the game\n")

def lose_turn():
    pass

def congratulations(): #urimit
    print("Congrats!  You win!")  

def play_again(): # luan perseri
    print("Do you wish to play again?")
    

def win_turn(word, correct_guesses):
    print(correct_guesses)
    print(list(word))
    if correct_guesses == list(word):
        congratulations()
        play_again()
    else:
        pick_letter(word, correct_guesses)


def check_guess(word, correct_guesses, letter):
    loss = True
    count = 0
    index = 0
    for shkronje in word:
        if letter == shkronje:
            count = count + 1
            correct_guesses[index] = shkronje
            loss = False
        index += 1
    if loss == True:
        lose_turn()
    else:
        print("This letter was found " + str(count) + " this many times!")
        win_turn(word, correct_guesses)


def pick_letter(word, correct_guesses):
    while True:
        letter = input("Please select a letter: ")
        if letter.isalpha():
            if len(letter) == 1:
                break
            print("Please enter only one letter!")
            continue
        print("No numbers please! Try again!")
    check_guess(word, correct_guesses, letter)

def start_game():
    while True:
        print("please select a word!")
        word = input()
        if word.isalpha():
            break
        print("Please do not use numbers!")
    correct_guesses = []
    for space in word:
        correct_guesses.append('')
    pick_letter(word, correct_guesses) #zgjidhni_germa


while True:
    selection = input()
    if selection == 's' or selection == "d" or selection == "q":
        break
    print("Invalid selection!  Try again!")

if selection == "s":
    start_game()