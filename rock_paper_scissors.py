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
    game_result = ''

    if player_input == enemy_choice:
        game_result = 'Draw'

    elif images[player_input - 1] == images[enemy_choice]:
        game_result = 'You lost'

    else:
        try:
            if images[player_input + 1] == images[enemy_choice]:
                game_result = 'You won'

        except IndexError:
            if images[enemy_choice] == paper:
                game_result = 'You won'

            elif images[enemy_choice] == rock:
                game_result = 'You lost'

    print('Player input:\n'
          f'{images[player_input]}')

    print('Enemy input:\n'
          f'{images[enemy_choice]}')

    print(f'{game_result}')
    choice = input("Would you like to play again?").lower()

    if choice == 'no':
        print('Game Finished')
        break