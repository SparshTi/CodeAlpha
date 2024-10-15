import random
words = ["python", "java", "swift", "hangman", "programming", "computer"]

def get_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_to_guess = get_random_word(words)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    game_won = False

    print("Welcome to Hangman!")

    while incorrect_guesses < max_incorrect_guesses and not game_won:
        print(f"\nWord: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        player_guess = input("Guess a letter: ").lower()

        if not player_guess.isalpha() or len(player_guess) != 1:
            print("Please enter a valid single letter.")
            continue

        if player_guess in guessed_letters:
            print(f"You've already guessed '{player_guess}'")
            continue

        guessed_letters.add(player_guess)

        if player_guess in word_to_guess:
            print(f"Good guess! '{player_guess}' is in the word.")
        else:
            print(f"Sorry, '{player_guess}' is not in the word.")
            incorrect_guesses += 1

        if all(letter in guessed_letters for letter in word_to_guess):
            game_won = True

    if game_won:
        print(f"\nCongratulations! You guessed the word: {word_to_guess}")
    else:
        print(f"\nGame over! The correct word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()