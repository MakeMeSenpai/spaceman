import random
import time
import os 

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
        return True

#uses list comprehension in order to see if the letter is in the word or not. Thank you Ryan for the help!
def get_guessed_word(secret_word, letters_guessed): 
    guessed = [i if i in letters_guessed else "_" for i in secret_word]
    return "".join(guessed)

#checks if guess is in word and cancles out already guessed letters or inproper input
def is_guess_in_word(guess, secret_word): 
    global letters_guessed
    if guess.isalpha() == False:
        time.sleep(1)
        os.system('clear')
        print("Please choose a letter")
    elif len(guess) > 1:
        time.sleep(1)
        os.system('clear')
        print("You can only choose one.")
    elif guess in letters_guessed:
        time.sleep(1)
        os.system('clear')
        print("But you already chose that one! Try another.")
        print(letters_guessed)
    elif guess in secret_word:
        letters_guessed.append(guess)
        "".join(letters_guessed)
        return True
    else:
        letters_guessed.append(guess)
        return False

#controls other functions to run the game
def spaceman(secret_word):
    incorrect = 0
    a = "Nice Choice! "
    b = "Try Again! Guesses left: "
    z = "_"
    
    for guesses in range(16):
        guesses += 1
        guess = input('Guess a letter! ').lower()
        x = is_guess_in_word(guess, secret_word)
        if x:
            time.sleep(1)
            os.system('clear')
            z = get_guessed_word(secret_word, letters_guessed)
            print(a + z)
            if is_word_guessed(z):
                time.sleep(1)
                os.system('clear')
                a = "Yay! You're so smart! You Win!"
                print(a)
                print("The Word was '" + secret_word + "'")
                break
        elif x == False:
            if incorrect == 6:
                time.sleep(1)
                os.system('clear')
                b = "Sorry... Game Over XC"
                print(b)
                print("The Word was '" + secret_word + "'")
                break
            else:
                incorrect += 1
                c = 7 - incorrect
                time.sleep(1)
                os.system('clear')
                print(b + str(c))
                if c == 6:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                    """)
                elif c == 5:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '... ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \
             /           _ |_______________|   _.        \
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~

                    """)
                elif c == 4:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\'
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\'
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\'
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '... ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \''
             /           _ |_______________|   _.        \''
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
           /          '' /   \      /         \           /\'
 ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
         /            /    / \\ --  _____//          ~ - .   \'
  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   .
   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/
     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._
 _  /         \ /_.' | /  /       (_________/ ~~-|
   /           //   _|/  /-              .    __ |..~. _____ -.. '  "
 ..\==========/'   \_/ _/  __      ___..     /  \|
                    """)
                elif c == 3:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\'
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\'
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\'
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '... ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \'
             /           _ |_______________|   _.        \'
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
           /          '' /   \      /         \           /\'
 ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
         /            /    / \\ --  _____//          ~ - .   \'
  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   .
   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/
     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._
 _  /         \ /_.' | /  /       (_________/ ~~-|
   /           //   _|/  /-              .    __ |..~. _____ -.. '  "
 ..\==========/'   \_/ _/  __      ___..     /  \|
     / _____  \'.______/___....------......__\__/|
 '  |          \     |\__________________|__|___/|  ~~~~~..   - ~  '
  ~ |        _  \   /~      \     \ --  /         \'
    | | | | | \_|  |   \     \ ~      //           |
 _. |_| | | | .    |-----..   \       /  /-      __|..~. _____ -.. '  "
      |_|_|_|   _. |       \_  \\ _ ./          ___|
  ~~~  ..   - ~  ' |         \__\___/__...------   |  ~~~~~..   - ~  '
                   |  .-         | | .       __    |
                   |     __..    | |    ______     |      .     ~
..~. _  __ -.. '   \           __| |   |      |    | _        .
                    """)
                elif c == 2:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\'
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\'
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\'
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '... ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \'
             /           _ |_______________|   _.        \'
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
           /          '' /   \      /         \           /\'
 ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
         /            /    / \\ --  _____//          ~ - .   \'
  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   .
   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/
     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._
 _  /         \ /_.' | /  /       (_________/ ~~-|
   /           //   _|/  /-              .    __ |..~. _____ -.. '  "
 ..\==========/'   \_/ _/  __      ___..     /  \|
     / _____  \'.______/___....------......__\__/|
 '  |          \     |\__________________|__|___/|  ~~~~~..   - ~  '
  ~ |        _  \   /~      \     \ --  /         \'
    | | | | | \_|  |   \     \ ~      //           |
 _. |_| | | | .    |-----..   \       /  /-      __|..~. _____ -.. '  "
      |_|_|_|   _. |       \_  \\ _ ./          ___|
  ~~~  ..   - ~  ' |         \__\___/__...------   |  ~~~~~..   - ~  '
                   |  .-         | | .       __    |
                   |     __..    | |    ______     |      .     ~
..~. _  __ -.. '   \           __| |   |      |    | _        .
                   /             | | ~ |__.___|.   |
                   |    __       | |   |      |    |              .. '
  ~~~~~..   - ~  ' | ''          / \   |      |    |___     __.
  ....   -         |  _____...   | |   \______/    |  ~~~~~..   - ~  '
                   | /        '--| |      ~~       |
     ~..   - ~  '  |/            | |    __----  .. |   .      .     _
                   ||____......._| |               |
                   |----         | |               |  ~~~~~..   - ~  '
   '... ... ~~~    |       -.    | |       _..     |
                   | ..         // |               | _~"".    .    
                    """)
                elif c == 1:
                    print("""
                         _______________________
                       //   __..--~~~~--..__    \\
                      ||___/  |  |   |  |   \ __/ |
                      ||  /   ___________    \    |
                      ||_/   /.......... \    |   |
                      | |   /..........   \   |   |
 _____________________| |  /...........    \  |   |________________
  ;   . . .   .       |_| |...........      | |   | .''."...  ... .
 ___   ..~.         _.' | |..........       | |   |         . ~
  .      '     .   / \_.| |..........       | |   |\ ~.   ._..---._
                  |. /| \ \............     / /   |/ .    /\      /\'
    '... ... ~~~  | \|| _\ \............   / /-.__|      // ~-._./ -\'
  ..~             |  |_.~\\ \_____________/ /// '.|     /__       __.\'
  ___   ..~.      |_.~   .\\_______________//   _ ~-.  ~~~~..  ~~~~~.
                 .~ -.     \__.---.________/   ______\.
 .''."...  ... ./\        _|      |---|  = |__ \__\===\   '... ... ~~~
               /  '.  .  |_|=     |---|    | _| \======\ ___   ..~.
   ..~        / .   \      |=     |___|    ||       __. \'
             /           _ |_______________|   _.        \'
 .''."...  ./                /   \___    ~~  \            \  '" ..   ~~
           /          '' /   \      /         \           /\'
 ___   .  /     -- .   /'   __\____/       ____\___.'   --  \ ___   ..~.
         /            /    / \\ --  _____//          ~ - .   \'
  ..--  /_..-       ./.   /  _/   _|___  \\       .     -   _/)
       /   ___     ./|__  / _/   (_____ / \\  .          \ ~ /   .
   .  /___////_   /  |   / _/    (_____ \  \\       _./ ..__/
     /___/__/_ \ /  _|  /__/ _-- (_____  \:_\\_____________/      ._
 _  /         \ /_.' | /  /       (_________/ ~~-|
   /           //   _|/  /-              .    __ |..~. _____ -.. '  "
 ..\==========/'   \_/ _/  __      ___..     /  \|
     / _____  \'.______/___....------......__\__/|
 '  |          \     |\__________________|__|___/|  ~~~~~..   - ~  '
  ~ |        _  \   /~      \     \ --  /         \'
    | | | | | \_|  |   \     \ ~      //           |
 _. |_| | | | .    |-----..   \       /  /-      __|..~. _____ -.. '  "
      |_|_|_|   _. |       \_  \\ _ ./          ___|
  ~~~  ..   - ~  ' |         \__\___/__...------   |  ~~~~~..   - ~  '
                   |  .-         | | .       __    |
                   |     __..    | |    ______     |      .     ~
..~. _  __ -.. '   \           __| |   |      |    | _        .
                   /             | | ~ |__.___|.   |
                   |    __       | |   |      |    |              .. '
  ~~~~~..   - ~  ' | ''          / \   |      |    |___     __.
  ....   -         |  _____...   | |   \______/    |  ~~~~~..   - ~  '
                   | /        '--| |      ~~       |
     ~..   - ~  '  |/            | |    __----  .. |   .      .     _
                   ||____......._| |               |
                   |----         | |               |  ~~~~~..   - ~  '
   '... ... ~~~    |       -.    | |       _..     |
                   | ..         // |               | _~"".    .
                   |          -  \ | __----.   ..  \
  ~~~..   - ~  '   |_____________| |_______________/
                   \_____________| |______________/   '    ...  __  ~
                    /     ----- \   /----------- \
   __~~..   - ~  ' /___      ----\ /--...___      \'
                  /    ..--      | | __..     ___./  .     .   ~
      - ~  '..    \  __________./  |_____________/  .   - ~  ' ~~~~
  ..._____~~~~~~JRO\___________/    \___________/  -_______...._____
..            ___ . ~~~~~~~~~~~. __\ ~~~~~~~~~~~~~...      _  ~
__    ....         ''        ...""       ....'''      -_~~~     ~~~...
                    """)
#ASCII done by Jro on https://www.asciiart.eu/space/astronauts. Thanks for the art! 
        if guesses == 15:
            time.sleep(1)
            os.system('clear')
            print("Sorry...Something went wrong. Your word was '" + secret_word + "'")
            break

# These function calls that will start the game
secret_word = load_word()
spaceman(secret_word)