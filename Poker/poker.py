import random
symbols = ['♥', '♦', '♠', '♣']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
# Karte sieht so aus '♠ 10'
cards = []
results = []
def generate_deck():
    for symbol in symbols:
        for value in values:
            cards.append(f"{symbol} {value}")        

def highCard(cards):
    return max([card[2:] for card in cards])

def hasNOfNumber(cards, n):
    card_values = [card[2:] for card in cards]
    for value in card_values:
        if card_values.count(value) == n:
            return True, value 
    return False, None

def isPair(cards):
    return hasNOfNumber(cards, 2)[0]

def isTwoPair(cards):
    first = hasNOfNumber(cards, 2)
    if first[0]: 
        cards = [card for card in cards if card[2:] != first[1]]  
        second = hasNOfNumber(cards, 2)
        if second[0]:  
            return True
    return False

def isTriple(cards):
    return hasNOfNumber(cards, 3)[0]

def isQuadruple(cards):
    return hasNOfNumber(cards, 4)[0]

def isFullHouse(cards):
    triple = hasNOfNumber(cards, 3)
    if triple[0]:
        remaining_cards = [card for card in cards if card[2:] != triple[1]]
        return hasNOfNumber(remaining_cards, 2)[0]
    return False


def isStraight(cards):
    change_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10}
    card_values = []
    for card in cards:
        value = card[2:]
        if value in change_cards:
            card_values.append(change_cards[value])
        else:
            card_values.append(int(value))

    card_values.sort()

    for i in range(1, 5):
        if card_values[i] - card_values[i - 1] != 1:
            return False

    return True

def isFlush(cards):
    firstsymbol = cards[0][0]
    return all([card[0] == firstsymbol for card in cards])

def isStraightFlush(cards):
    return isStraight(cards) and isFlush(cards)

def isRoyalFlush(cards):
    # ein set -> Reihenfolge egal
    royal_values = {'10', 'J', 'Q', 'K', 'A'} 
    card_values = {card[2:] for card in cards}
    
    return card_values == royal_values and isFlush(cards)


generate_deck()     
for _ in range(3_000_000):
    random_pick = random.sample(cards, 5)
    
    if isRoyalFlush(random_pick):
        results.append("Royal Flush")
    elif isStraightFlush(random_pick):
        results.append("Straight Flush")
    elif isQuadruple(random_pick):
        results.append("Four of a Kind")
    elif isFullHouse(random_pick):
        results.append("Full House")
    elif isFlush(random_pick):
        results.append("Flush")
    elif isStraight(random_pick):
        results.append("Straight")
    elif isTriple(random_pick):
        results.append("Three of a Kind")
    elif isTwoPair(random_pick):
        results.append("Two Pair")
    elif isPair(random_pick):
        results.append("One Pair")
    else:
        results.append("High Card")

result_counts = {}
for hand in results:
    if hand in result_counts:
        result_counts[hand] += 1
    else:
        result_counts[hand] = 1
total_draws = len(results)

probabilities = {hand: count / total_draws for hand, count in result_counts.items()}
for hand, probability in probabilities.items():
    print(f"{hand}: {probability:.5%}")
