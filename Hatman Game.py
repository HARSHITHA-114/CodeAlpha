import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'program', 'keyboard', 'mouse', 'monitor', 'internet']
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to Hangman!")
    print("Guess the word:", display_word(word, guessed_letters))

    while '_' in display_word(word, guessed_letters) and incorrect_guesses < max_attempts:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            incorrect_guesses += 1
            print("Incorrect guess! You have", max_attempts - incorrect_guesses, "attempts left.")
        else:
            print("Correct guess!")

        print("Guessed letters:", ', '.join(guessed_letters))
        print(display_word(word, guessed_letters))

    if '_' not in display_word(word, guessed_letters):
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of attempts. The word was:", word)

hangman()
