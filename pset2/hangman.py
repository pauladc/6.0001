# Problem Set 2, hangman.py
# Name: Paula Contreras Nino
# Collaborators: None
# Time spent: 3:45

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    counter = 0
    for i in range (len(secret_word)):
        for j in range (len(letters_guessed)):
            if (secret_word[i] == letters_guessed[j]):
                counter +=1
    if (counter == len(secret_word)):
        return True
    else:
        return False


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and plus signs (+) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    toReturn = ''
    for e in secret_word:
        if e in letters_guessed:
            toReturn += e
        else:
            toReturn += '+'
    return toReturn
            
            


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''

    return ''.join(char for char in string.ascii_lowercase if char not in letters_guessed)   
    
    
def hangman(secret_word, with_help):

    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.
    '''
    print('Welcome to Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} letters long.')
    '''
    * The user should start with 10 guesses.
    '''
        
    numGuesses = 10
    guessed = []
    # creates a list of vowels to later deduct 2 points
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    def create_choose(secret_word, available_letters, guessed):
        #creates a string that holds the letters in available letters and secret word
        choose_from = ''
        for i in range (len(available_letters)):
            if available_letters[i] in secret_word:
                choose_from += available_letters[i]
        new = random.randint(0, len(choose_from)-1)
        revealed_letter = choose_from[new]
        guessed.append(revealed_letter)
        return revealed_letter
    
    # continues the game while the player has guesses left
    while(numGuesses > 0):
        print('--------------')
        print(f'You currently have {numGuesses} guesses left.')
        print('Available letters: ' + get_available_letters(guessed))
        user_guess = input('Please guess a letter: ')
        #factors in for playing the game with help
        if (user_guess == '!' and with_help):
            if (numGuesses > 3):
                numGuesses -= 3
                toReveal = create_choose(secret_word, get_available_letters(guessed), guessed)
                print(f'Letter revealed: {toReveal}')
                print('Good guess: ' + get_word_progress(secret_word, guessed))
            else:
                print('Oops! Not enough guesses left: ' + get_word_progress(secret_word, guessed))
            
        else:
            if (user_guess.lower() in guessed):
                print("Oops! You've already guessed that letter: " + get_word_progress(secret_word, guessed))
            else:
                if(user_guess.isalpha() and len(user_guess) == 1):
                    low_user_guess = user_guess.lower()
                    guessed.append(low_user_guess)
                    if (low_user_guess in secret_word):
                        print('Good guess: ' + get_word_progress(secret_word, guessed))
                    else:
                        if(low_user_guess in vowels):
                            numGuesses -= 2
                        else:
                            numGuesses -= 1
                        print('Oops! That letter is not in my word: ' + get_word_progress(secret_word, guessed))
                else:
                        print('Oops! That is not a valid letter. Please input a letter from the alphabet: ' + get_word_progress(secret_word, guessed))
        #case where the player has won
        if (has_player_won(secret_word, guessed)):
            print('--------------')
            print('Congratulations, you won!')
            unique = ''.join(set(secret_word))
            print(f'Your total score for this game is: {4*len(unique)*numGuesses + 2*len(secret_word)}')
            break
        elif (numGuesses <= 0):
            print('--------------')
            print(f'Sorry, you ran out of guesses. The word was {secret_word}.')

              


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
        secret_word = choose_word(wordlist)
    #   secret_word = 'wildcard'
        with_help = True
        hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "!" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.