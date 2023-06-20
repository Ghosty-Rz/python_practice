secret_word = "Purple"
guess = "n"  # this is used to enable the user to enter multiple prompts
guess_count = 0

while guess != secret_word:
    if guess_count < 5:
        guess = input("Enter Guess: ")

        if guess_count == 1:
            print("it is a color")
        if guess_count == 3:
            print("it starts with p")

        guess_count += 1

print("you win")
