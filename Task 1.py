import random

words = ["apple", "tiger", "house", "water", "pizza"]

chosen_word = random.choice(words)

guessed_letters = []

attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0:

    display_word = ""

    for letter in chosen_word:

        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in chosen_word:
        guessed_letters.append(guess)
        print("Correct guess!")

    else:
        attempts -= 1
        print("Wrong guess!")
        print("Remaining Attempts:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", chosen_word)
    
    
