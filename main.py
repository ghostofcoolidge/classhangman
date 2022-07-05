


print("Welcome to Hangman!")
print("Please select from the options below.\n")
print("s- start the game")
print("d- change difficulty")
print("q- quit the game\n")

def pick_letter():
    while True:
        letter = input("Please select a letter: ")
        if letter.isalpha():
            if len(letter) == 1:
                break
            print("Please enter only one letter!")
            continue
        print("No numbers please! Try again!")

def start_game():
    while True:
        print("please select a word!")
        word = input()
        if word.isalpha():
            break
        print("Please do not use numbers!")
    pick_letter() #zgjidhni_germa


while True:
    selection = input()
    if selection == 's' or selection == "d" or selection == "q":
        break
    print("Invalid selection!  Try again!")

if selection == "s":
    start_game()