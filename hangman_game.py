import random

words = ["python", "apple", "banana", "computer", "program"]

word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("=== HANGMAN GAME ===")

while incorrect_guesses < max_incorrect:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Guessed Letters:", guessed_letters)
    print("Remaining Chances:", max_incorrect - incorrect_guesses)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in word:
        incorrect_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The word was:", word)
