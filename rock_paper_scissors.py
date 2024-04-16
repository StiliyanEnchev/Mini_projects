import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

images = [paper, rock, scissors]
choice = 'yes'

while True:
    player_input = int(input('Choose 0 for paper, 1 for rock, 2 for scissors:'))
    enemy_choice = random.randint(0, 2)


    if player_input == enemy_choice:
        print('Player input:\n'
              f'{images[player_input]}')

        print('Enemy input:\n'
            f'{images[enemy_choice]}')

        print('Draw')
        choice = input("Would you like to play again?").lower()


    elif images[player_input - 1] == images[enemy_choice]:
        print('Player input:\n'
            f'{images[player_input]}')

        print('Enemy input:\n'
            f'{images[enemy_choice]}')

        print('You lost!')
        choice = input("Would you like to play again?").lower()

    else:
        try:
            if images[player_input + 1] == images[enemy_choice]:
                print('Player input:\n'
                    f'{images[player_input]}')

                print('Enemy input:\n'
                    f'{images[enemy_choice]}')

                print('You won!')
                choice = input("Would you like to play again?").lower()

        except IndexError:
            if images[enemy_choice] == paper:
                print('Player input:\n'
                    f'{images[player_input]}')

                print('Enemy input:\n'
                    f'{images[enemy_choice]}')

                print('You won!')
                choice = input("Would you like to play again?").lower()

            elif images[enemy_choice] == rock:
                print('Player input:\n'
                    f'{images[player_input]}')

                print('Enemy input:\n'
                    f'{images[enemy_choice]}')

                print('You lost!')
                choice = input("Would you like to play again?").lower()

    if choice == 'no':
        print('Game Finished')
        break


