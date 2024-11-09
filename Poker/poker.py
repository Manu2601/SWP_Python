import random

# Eigene benutzerdefinierte Exception für leeren Deck
class DeckEmptyException(Exception):
    pass

# Definieren der möglichen Symbole und Kartenwerte
symbols = ['♥', '♦', '♠', '♣']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Liste zur Speicherung des Kartenstapels
cards = []
# Liste zur Speicherung der Ergebnisse der Zufallsziehungen
results = []

# Funktion zur Erstellung des Kartenstapels
def generate_deck():
    # Erstelle alle Kombinationen von Symbolen und Werten
    for symbol in symbols:
        for value in values:
            cards.append(f"{symbol} {value}")
    
    # Sicherstellen, dass der Deck nicht leer ist
    if not cards:
        raise DeckEmptyException("Der Kartenstapel wurde nicht korrekt erstellt oder ist leer.")

# Funktion zur Bestimmung der höchsten Karte
def highCard(cards):
    return max([card[2:] for card in cards])  # Vergleicht die Kartenwerte

# Funktion, um zu überprüfen, ob eine bestimmte Anzahl (n) von Karten desselben Wertes existiert
def hasNOfNumber(cards, n):
    # Extrahiere die Kartenwerte
    card_values = [card[2:] for card in cards]
    for value in card_values:
        # Prüfe, ob der Wert genau n-mal vorkommt
        if card_values.count(value) == n:
            return True, value 
    return False, None

# Funktion zur Überprüfung, ob ein Paar vorhanden ist
def isPair(cards):
    return hasNOfNumber(cards, 2)[0]

# Funktion zur Überprüfung, ob zwei Paare vorhanden sind
def isTwoPair(cards):
    first = hasNOfNumber(cards, 2)
    if first[0]: 
        # Entferne das erste Paar und prüfe auf ein weiteres Paar
        cards = [card for card in cards if card[2:] != first[1]]  
        second = hasNOfNumber(cards, 2)
        if second[0]:  
            return True
    return False

# Funktion zur Überprüfung, ob ein Drilling vorhanden ist
def isTriple(cards):
    return hasNOfNumber(cards, 3)[0]

# Funktion zur Überprüfung, ob ein Vierling vorhanden ist
def isQuadruple(cards):
    return hasNOfNumber(cards, 4)[0]

# Funktion zur Überprüfung, ob ein Full House vorhanden ist
def isFullHouse(cards):
    triple = hasNOfNumber(cards, 3)
    if triple[0]:
        # Entferne das Dreierpaar und prüfe auf ein Paar
        remaining_cards = [card for card in cards if card[2:] != triple[1]]
        return hasNOfNumber(remaining_cards, 2)[0]
    return False

# Funktion zur Überprüfung, ob eine Straße (Sequenz) vorhanden ist
def isStraight(cards):
    # Mapping für Bildkartenwerte
    change_cards = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10}
    card_values = []
    for card in cards:
        value = card[2:]
        # Konvertiere Kartenwerte zu numerischen Werten
        if value in change_cards:
            card_values.append(change_cards[value])
        else:
            card_values.append(int(value))

    # Sortiere die Werte und prüfe, ob sie eine fortlaufende Sequenz bilden
    card_values.sort()
    for i in range(1, 5):
        if card_values[i] - card_values[i - 1] != 1:
            return False

    return True

# Funktion zur Überprüfung, ob ein Flush (alle Symbole gleich) vorhanden ist
def isFlush(cards):
    # Symbole der ersten Karte
    firstsymbol = cards[0][0]
    return all([card[0] == firstsymbol for card in cards])

# Funktion zur Überprüfung, ob ein Straight Flush vorhanden ist
def isStraightFlush(cards):
    return isStraight(cards) and isFlush(cards)

# Funktion zur Überprüfung, ob ein Royal Flush vorhanden ist
def isRoyalFlush(cards):
    # Set für Royal Flush-Werte (Reihenfolge egal)
    royal_values = {'10', 'J', 'Q', 'K', 'A'} 
    card_values = {card[2:] for card in cards}
    
    return card_values == royal_values and isFlush(cards)

# Erstellen des Kartenstapels
try:
    generate_deck()  # Hier wird die DeckEmptyException ausgelöst, falls der Stapel leer ist
except DeckEmptyException as e:
    print(f"Fehler: {e}")
    cards = []  # Stapel bleibt leer, wenn der Fehler auftritt

# Wenn der Stapel leer ist, breche die Simulation ab
if not cards:
    print("Der Kartenstapel konnte nicht erstellt werden. Simulation wird abgebrochen.")
else:
    # Simuliere 3.000.000 Zufallsziehungen mit je 5 Karten
    for _ in range(3_000_000):
        try:
            # Wähle zufällig 5 Karten aus dem Stapel
            random_pick = random.sample(cards, 5)
            
            # Hier simulieren wir den Fall, dass der Stapel leer wird
            if not cards:  # Dieser Check dient nur als Simulation für den leeren Stapel
                raise DeckEmptyException("Der Kartenstapel ist leer, es können keine weiteren Karten gezogen werden.")
            
            # Bestimme das bestmögliche Pokerblatt für die Auswahl
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
        except DeckEmptyException as e:
            print(f"Fehler beim Ziehen der Karten: {e}")
            break  # Beendet die Simulation, wenn der Kartenstapel leer ist

    # Zählen der Häufigkeit jeder Handkombination
    result_counts = {}
    for hand in results:
        if hand in result_counts:
            result_counts[hand] += 1
        else:
            result_counts[hand] = 1
    total_draws = len(results)

    # Berechnung der Wahrscheinlichkeiten für jede Handkombination
    probabilities = {hand: count / total_draws for hand, count in result_counts.items()}
    for hand, probability in probabilities.items():
        print(f"{hand}: {probability:.5%}")
