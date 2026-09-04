import random

words = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew")

hangman_art = {
    0: ("  ",
        "  ",
        "  "),
    1: (" o ",
        " | ",
        "  "),
    2: (" o ",
        " | ",
        " | "),
    3: (" o ",
        " | ",
        "/| "),
    4: (" o ",
        " | ",
        "/|\\"),
    5: (" o ",
        " | ",
        "/|\\",
        "/ "),
    6: (" o ",
        " | ",
        "/|\\",
        "/ \\"),
}


def display_hangman(tries):
    for line in hangman_art[tries]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0

    guessed_letters = set()

    is_running = True

    while is_running:
        display_hangman(wrong_guesses)
        display_hint(hint)

        guess = input("Guess a letter: ").lower()

        # Validate input first
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        # Check if letter was already guessed
        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        # Correct guess
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess


        # Wrong guess
        else:
            wrong_guesses += 1
            print("Wrong guess!")

        # Check WIN
        if "_" not in hint:
            display_hangman(wrong_guesses)
            display_hint(hint)
            print("You win! 🎉")
            is_running = False

        # Check LOSS
        elif wrong_guesses >= len(hangman_art) - 1:
            display_hangman(wrong_guesses)
            display_answer(answer)
            print("Game over! The correct word was:", answer)
            is_running = False


if __name__ == "__main__":
    main()
