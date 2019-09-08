import random


def load_word():  # reads txt file and returns secret word
    with open('words.txt', 'r') as f:
        words_list = f.read().split(' ')
    secret_word = random.choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    if secret_word == letters_guessed:
        return True


def get_guessed_word(secret_word, letters_guessed): #uses list comprehension in order to see if the letter is in the word or not. Thank you Ryan for the help!
    guessed = [i if i in letters_guessed else "_" for i in secret_word]
    return "".join(guessed)

def is_guess_in_word(guess, secret_word): #checks if guess is in word and cancles out already guessed letters or inproper input
    inproper = """ `1234567890-=[];',"./~!@#$%^&*()_+|:"""
    letters_guessed = []
    if guess in inproper:
        print("Please choose a letter")
    elif guess in letters_guessed:
        print("But you already chose that one! Try another.")
    else:
        letters_guessed.append(guess)
        return guess in secret_word


def spaceman(secret_word):
    '''clear
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    incorrect = 0
    a = "Nice Choice! "
    b = "Try Again! Guesses left: "
    for guesses in range(16):
        guesses += 1
        guess = input('Guess a letter! ').lower()
        if is_guess_in_word(guess, secret_word):
            if is_word_guessed(guess, secret_word):
                a = "Yay! You're so smart! You Win!"
                print(a)
                print("The Word was '" + secret_word + "'")
                break
            else:
                c = get_guessed_word(secret_word, guess)
                print(a + c)
        if is_guess_in_word(guess, secret_word) == False:
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

# The user is always prompted to guess a letter until they win or lose
# User is allowed seven (7) incorrect guesses, and they should be told how many guesses they have left after each incorrect guess
# After guessing a letter, the user must be told the following:
# Correct guess: the placeholder text with the correct letter filled in.
# If the word is “dog” and they guess “g” as their first guess, they should see _ _ g
# Incorrect guess: a message telling them their guess is incorrect, and then the number of guesses they have remaining
# If a guessed letter appears multiple times in the word, that guessed letter should appear in all valid blanks
# Correct Example (word is “apple”): p → _ pp_ _
# Incorrect Example (word is “apple”): p → _p_ _
# If a user successfully guesses all the letters, the game ends, and the user is shown a message notifying them that they won
# If a user guesses incorrectly seven (7) times, the game ends, and the user is shown a message notifying them that they lost
# TODO: show the player information about the game according to the project spec
# TODO: Ask the player to guess one letter per round and check that it is only one letter
# TODO: Check if the guessed letter is in the secret or not and give the player feedback
# TODO: show the guessed word so far
# TODO: check if the game has been won or lost

# Alert the user if they guessed a letter they already guessed, and don’t have it count as an incorrect guess
# Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
# Prompt  the user to play again after a game ends. If they say yes, then start a new game.
# Change the number of incorrect guesses allowed to match the length of the mystery word
# Show the user the mystery word when they lose
# Use ASCII art to draw the spaceman with each incorrect guess
# Sinister Spaceman: After the user guesses a correct letter, change the mystery word to be a new mystery word that is the same word length and uses the same correctly guessed letters
# Example: mystery word is “car”, user guesses “a”, the user is shown “_a_”, but the word is now changed to “bar”


# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)
