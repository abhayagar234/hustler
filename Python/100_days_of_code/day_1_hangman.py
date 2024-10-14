choice_of_words = ["python", "java", "kotlin", "javascript"]
import random


def hangman():
    word = random.choice(choice_of_words)
    word_length = len(word)
    display = []
    for _ in range(word_length):
        display += "_"
    print(display)
    attempt = 4
    guessed_letter = set()
    while attempt > 0:
        guess = input("Guess a letter: ").lower()
        if guess in guessed_letter:
            print("You have already guessed this letter.")
            continue
        guessed_letter.add(guess)
        for position in range(word_length):
            letter = word[position]
            if letter == guess:
                display[position] = letter
        print(display)
        if guess not in word:
            attempt -= 1
            print("Incorrect guess. You have", attempt, "attempts left.")
        if "_" not in display:
            print("You win.")
            break
    print(f"The word was {word}")


hangman()
