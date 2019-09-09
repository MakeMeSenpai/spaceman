import random

#creates a saved guessed list
letters_guessed = []

# reads txt file and returns secret word
def load_word(): 
    with open('words.txt', 'r') as f:
        words_list = f.read().split(' ')
    secret_word = random.choice(words_list)
    return secret_word

#checks if letters_guessed is in secret word to let the player win
def is_word_guessed(guessed):
    if not '_' in guessed:
        print("GRANTZ")
        return True

#uses list comprehension in order to see if the letter is in the word or not. Thank you Ryan for the help!
def get_guessed_word(secret_word, letters_guessed): 
    guessed = [i if i in letters_guessed else "_" for i in secret_word]
    return "".join(guessed)

#checks if guess is in word and cancles out already guessed letters or inproper input
def is_guess_in_word(guess, secret_word): 
    global letters_guessed
    if guess.isalpha() == False:
        print("Please choose a letter")
    elif len(guess) > 1:
        print("You can only choose one.")
    elif guess in letters_guessed:
        print("But you already chose that one! Try another.")
    else:
        letters_guessed.append(guess)
        print('hek')
        print(letters_guessed)
        "".join(letters_guessed)
        return True

#controls other functions to run the game
def spaceman(secret_word):
    incorrect = 0
    a = "Nice Choice! "
    b = "Try Again! Guesses left: "
    z = "_"
    
    for guesses in range(16):
        guesses += 1
        guess = input('Guess a letter! ').lower()
        if is_guess_in_word(guess, secret_word):
            z = get_guessed_word(secret_word, letters_guessed)
            print(a + z)
            if is_word_guessed(z):
                a = "Yay! You're so smart! You Win!"
                print(a)
                print("The Word was '" + secret_word + "'")
                break
        elif is_guess_in_word(guess, secret_word) == False:
            if incorrect == 6:
                b = "Sorry... Game Over XC"
                print(b)
                print("The Word was '" + secret_word + "'")
                break
            else:
                incorrect += 1
                c = 7 - incorrect
                print(b + str(c))
        if guesses == 15:
            print("Sorry...Something went wrong. Your word was '" + secret_word + "'")
            break

# Use ASCII art to draw the spaceman with each incorrect guess
#double interations means double printing and less effiecient code

# These function calls that will start the game
secret_word = "woord" #load_word()
spaceman(secret_word)