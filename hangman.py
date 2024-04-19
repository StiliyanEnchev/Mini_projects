import random
HANGMAN = (
"""
-----
|   |
|   0
|
|
|
|
|
|
""",
"""
-----
|   |
|   0
|   |
|
|
|
|
|
""",
"""
-----
|   |
|   0
|  /|
|
|
|
|
|
""",
"""
-----
|   |
|   0
|  /|\\
|   |
|
|
|
|
""",
"""
-----
|   |
|   0
|  /|\\
|   |
|  /
|
|
|
""",
"""
-----
|   |
|   0
|  /|\\
|   |
|  / \\
|
|
|
""")

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
guessed_word = list('_' * len(chosen_word))
turns = 0
won = False

while '_' in guessed_word and turns < 6:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        print("Letter not found. Try again")
        print(HANGMAN[turns])
        print(''.join(guessed_word))
        turns += 1
        continue

    match = [char if char == guess else '_' for char in chosen_word]

    for indx in range(len(match)):
        if match[indx] != "_":
            guessed_word[indx] = match[indx]

    print('You guessed right!')
    print(''.join(guessed_word))

    if '_' not in guessed_word:
        won = True
        break

if not won:
    print('Game Over')

if won:
    print('Congratulations! You won the game.')
