import random

def choose_word():
    """
    Function to choose a word randomly from a list of predefined words.
    """
    words = ["apple", "banana", "orange", "grape", "kiwi", "melon", "peach", "pear", "strawberry", "blueberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    """
    Function to display the word with guessed letters filled in and others as underscores.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def display_hangman(incorrect_attempts):
    """
    Function to display the Hangman based on the number of incorrect attempts.
    """
    hangman_art = [
        """
           _________
          |         |
                    |
                    |
                    |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
                    |
                    |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
          |         |
                    |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
         /|         |
                    |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
         /|\\        |
                    |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
         /|\\        |
         /          |
                    |
        ==============
        """,
        """
           _________
          |         |
          O         |
         /|\\        |
         / \\        |
                    |
        ==============
        """
    ]
    return hangman_art[incorrect_attempts]

def get_guess(guessed_letters):
    """
    Function to get a valid guess from the player.
    """
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif not guess.isalpha():
            print("Please enter a letter.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
        else:
            return guess

def play_hangman():
    """
    Function to play the Hangman game.
    """
    word = choose_word()
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word, guessed_letters))

    while incorrect_attempts < max_attempts:
        guess = get_guess(guessed_letters)
        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess!")
            incorrect_attempts += 1
            print(display_hangman(incorrect_attempts))

        print(display_word(word, guessed_letters))

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word:", word)
            break

    if incorrect_attempts == max_attempts:
        print("Sorry, you ran out of attempts. The word was:", word)

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == 'yes':
        play_hangman()
    else:
        print("Thanks for playing Hangman!")

# Start the game
play_hangman()
