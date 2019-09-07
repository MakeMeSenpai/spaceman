import random

def load_word(): #reads txt file and returns secret word
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
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

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''
    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    for letter in secret_word:
        if letters_guessed == letter:
            return letters_guessed in secret_word


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    if guess in secret_word:
        return True
    else:

        return False

def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    incorrect = 0
    a = "Nice Choice!"
    b = "Try Again!"
    for guesses in range(13):
        guesses += 1
        guess = input('Guess a letter! ')
        if is_guess_in_word(guess, secret_word):
            if is_word_guessed(guess, secret_word):
                a = "Yay! You're so smart! You Win!"
                print(a)
                print("The Word was '" + secret_word + "'")
                break
            else:
                print(a)
        if is_guess_in_word(guess, secret_word) == False:
            if incorrect == 6:
                b = "Sorry... Game Over XC"
                print(b)
                print("The Word was '" + secret_word + "'")
                break
            else:
                print(b)
                incorrect += 1

#The user is always prompted to guess a letter until they win or lose 
#User is allowed seven (7) incorrect guesses, and they should be told how many guesses they have left after each incorrect guess
#After guessing a letter, the user must be told the following:
#Correct guess: the placeholder text with the correct letter filled in.
#If the word is “dog” and they guess “g” as their first guess, they should see _ _ g
#Incorrect guess: a message telling them their guess is incorrect, and then the number of guesses they have remaining
#If a guessed letter appears multiple times in the word, that guessed letter should appear in all valid blanks
#Correct Example (word is “apple”): p → _ pp_ _
#Incorrect Example (word is “apple”): p → _p_ _
#If a user successfully guesses all the letters, the game ends, and the user is shown a message notifying them that they won
#If a user guesses incorrectly seven (7) times, the game ends, and the user is shown a message notifying them that they lost
#TODO: show the player information about the game according to the project spec
#TODO: Ask the player to guess one letter per round and check that it is only one letter
#TODO: Check if the guessed letter is in the secret or not and give the player feedback
#TODO: show the guessed word so far
#TODO: check if the game has been won or lost

#Alert the user if they guessed a letter they already guessed, and don’t have it count as an incorrect guess
#Users can only guess individual letters at a time. If they guess anything other than an individual letter, they should be prompted and told to input only one letter
#Prompt  the user to play again after a game ends. If they say yes, then start a new game.
#Change the number of incorrect guesses allowed to match the length of the mystery word
#Show the user the mystery word when they lose
#Use ASCII art to draw the spaceman with each incorrect guess
#Sinister Spaceman: After the user guesses a correct letter, change the mystery word to be a new mystery word that is the same word length and uses the same correctly guessed letters
#Example: mystery word is “car”, user guesses “a”, the user is shown “_a_”, but the word is now changed to “bar”

#These function calls that will start the game
secret_word = "word" #load_word()
spaceman(secret_word)