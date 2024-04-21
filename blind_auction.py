logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''

print(logo)
bids = {}
def highers_bid(bids_dictionary):
    highers_bid = ['John', 0]
    for key, value in bids_dictionary.items():
        if int(value) > highers_bid[1]:
            highers_bid = [key, int(value)]

    return highers_bid

while True:

    name = input('What is your name?')
    bid = input('What is your bid: $')

    bids[name] = bid

    others = input('Is there other bidders?').lower()

    if others == 'yes':
        continue

    else:
        print('The winner is:')
        print(*highers_bid(bids))
        break
