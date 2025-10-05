import random

# Word list
words = ["apple", "grape", "chair", "plant", "river"]

# Pick a random word
word = random.choice(words)

# Start with blanks
guessed_word = ["_"] * len(word)

# Chances
chances = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

# Game loop
while chances > 0 and "_" in guessed_word:
    guess = input("Enter a letter: ")

    if guess in word:
        print("Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        chances -= 1
        print("Wrong guess! Chances left:", chances)

    print("Word:", " ".join(guessed_word))

# End of game
if "_" not in guessed_word:
    print("You WIN! The word was:", word)
else:
    print("You LOSE! The word was:", word)