import random

def generate_deck():
    symbols = ['♥', '♦', '♠', '♣']
    values = range(2, 15)  # Kartenwerte 2 bis 14 (Ass = 14)
    return [f"{symbol} {value}" for symbol in symbols for value in values]
    # Beispiel Karte example_card = "♥ 10"

def extract_values(cards):
    return sorted(int(card.split()[1]) for card in cards)

def extract_symbols(cards):
    return [card.split()[0] for card in cards]

def isPair(cards):
    values = extract_values(cards)
    
    return any(values.count(value) == 2 for value in set(values)) # set, damit die Funktion jeden Wert nur einmal prüft

def isTwoPair(cards):
    values = extract_values(cards)
    pairs = [value for value in set(values) if values.count(value) == 2]
    return len(pairs) == 2

def isTriple(cards):
    values = extract_values(cards)
    return any(values.count(value) == 3 for value in set(values))

def isQuadruple(cards):
    values = extract_values(cards)
    return any(values.count(value) == 4 for value in set(values))

def isFullHouse(cards):
    values = extract_values(cards)
    has_triple = any(values.count(value) == 3 for value in set(values))
    has_pair = any(values.count(value) == 2 for value in set(values))
    return has_triple and has_pair

def isStraight(cards):
    values = extract_values(cards)
    # schauen, ob Abstand zwischen allen Werten 1 ist
    return all(values[i] - values[i - 1] == 1 for i in range(1, len(values)))

def isFlush(cards):
    symbols = extract_symbols(cards)
    return len(set(symbols)) == 1  # set, da alle Symbole gleich sein müssen

def isStraightFlush(cards):
    return isStraight(cards) and isFlush(cards)

def isRoyalFlush(cards):
    values = extract_values(cards)
    return values == [10, 11, 12, 13, 14] and isFlush(cards)

def simulate_draws(deck, num_draws, num_cards=5):
    results = []
    for _ in range(num_draws):
        random_pick = random.sample(deck, num_cards)
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
    return results

def calculate_probabilities(results):
    total_draws = len(results)
    hand_counts = {hand: results.count(hand) for hand in set(results)} # set, damit jede Hand nur einmal gezählt wird
    return {hand: count / total_draws for hand, count in hand_counts.items()}

def main():
    deck = generate_deck()

    while True:
        try:
            draws = int(input("Anzahl der Ziehungen: "))
            if draws <= 0:
                raise ValueError("Die Anzahl der Ziehungen muss eine positive Zahl sein.")
            break
        except ValueError as e:
            print(f"Ungültige Eingabe: {e}. Bitte geben Sie eine ganze Zahl größer als 0 ein.")
    num_cards = 5
    results = simulate_draws(deck, draws, num_cards)
    probabilities = calculate_probabilities(results)

    print("\nWahrscheinlichkeiten der Pokerhände:")
    for hand, probability in probabilities.items():
        print(f"{hand}: {probability:.5%}")

if __name__ == "__main__":
    main()
