def card_to_value(card):
    ten = ('T','Q','J','K')
    if card in ten:
        value = 10
    elif card == 'A':
        value = 1
    else:
        value = int(card)
    return(value)
'''Takes in the type of card and returns the value for that card'''
def hard_score(hand):
    sum = 0
    for card in hand:
        sum += card_to_value(card)
    return sum
'''Takes in the hand and returns the sum of the cards with Ace having a value of 1'''

def soft_score(hand):
    sum = 0
    firstace = True
    for card in hand:
        if card == 'A' and firstace:
            sum += 11
            firstace = False
        elif card == 'A':
            sum += 1
        else:
            sum += card_to_value(card)
    return sum
'''takes in the hand and returns its sum with the first Ace being worth 11 
and any other Ace afterwards being 1 '''