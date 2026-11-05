def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        result = ""

        for character in secret_word:
            if character in guesses:
                result += character
            else:
                result += "_"

        print(result)

        return all(character in guesses for character in secret_word)
    
    return hangman_closure

secret_word = input("Enter a secret word: ").lower()

game = make_hangman(secret_word)

while True:
    letter = input("Guess a letter: ").lower()

    if game(letter):
        print("You guessed the word!")
        break