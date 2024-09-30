import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
 
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()

    print("  ", len(wordlist), "words loaded.")

    return wordlist



def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):

    return all(char in letters_guessed for char in secret_word)


def get_guessed_word(secret_word, letters_guessed):

    return ''.join([char if char in letters_guessed else '_ ' for char in secret_word])


def get_available_letters(letters_guessed):
    
    return ''.join([char for char in string.ascii_lowercase if char not in letters_guessed])


def hangman(secret_word):

    guesses = 6
    warnings = 3
    letters_guessed = []
    vowels = 'aeiou'
    unique_letters = ""

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("------------------")

    while guesses:
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        user_guess = input("Please guess a letter: ").lower()

        if user_guess in letters_guessed:
            if warnings == 0:
                guesses -= 1
            else:
                warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {warnings} warnings: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            continue

        if user_guess not in get_available_letters(letters_guessed):
            if warnings == 0:
                guesses -= 1
            else:
                warnings -= 1
            
            print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            continue
        
        letters_guessed.append(user_guess)

        if user_guess not in secret_word:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            if user_guess not in vowels:
                guesses -= 1
            else:
                guesses -= 2
        else:
            unique_letters += user_guess
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
        
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses * len(unique_letters)}")
            break
        
    else:
        print("Sorry, you ran out of guesses. The word was else.")



def match_with_gaps(my_word, other_word):

    my_word = my_word.replace(" ", "")

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i].isalpha() and my_word[i] != other_word[i]:
                return False
    
        return True
    
    return False


def show_possible_matches(my_word):

    possible_matches = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)
    
    if len(possible_matches) == 0:
        return "No matches found"
    
    return possible_matches

def hangman_with_hints(secret_word):

    guesses = 6
    warnings = 3
    letters_guessed = []
    vowels = ["a", "e", "i", "o", "u"]
    unique_letters = ""

    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")
    print("------------------")

    while guesses:
        print(f"You have {guesses} guesses left.")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        user_guess = input("Please guess a letter: ").lower()

        if user_guess == "*":
            print("Possible word matches are: ")
            for word in show_possible_matches(get_guessed_word(secret_word, letters_guessed)):
                print(word, end=" ")
            print("\n---------------")
            continue

        if user_guess in letters_guessed:
            if warnings == 0:
                guesses -= 1
            else:
                warnings -= 1
            print(f"Oops! You've already guessed that letter. You now have {warnings} warnings: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            continue

        if user_guess not in get_available_letters(letters_guessed):
            if warnings == 0:
                guesses -= 1
            else:
                warnings -= 1
            
            print(f"Oops! That is not a valid letter. You have {warnings} warnings left: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            continue
        
        letters_guessed.append(user_guess)

        if user_guess not in secret_word:
            print(f"Oops! That letter is not in my word: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
            if user_guess not in vowels:
                guesses -= 1
            else:
                guesses -= 2
        else:
            unique_letters += user_guess
            print(f"Good guess: {get_guessed_word(secret_word, letters_guessed)}")
            print("------------------")
        
        if get_guessed_word(secret_word, letters_guessed) == secret_word:
            print("Congratulations, you won!")
            print(f"Your total score for this game is: {guesses * len(unique_letters)}")
            break
        
    else:
        print("Sorry, you ran out of guesses. The word was else.")


if __name__ == "__main__":
    
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)