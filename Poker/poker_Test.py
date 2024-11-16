import unittest
from poker import (
    generate_deck,
    extract_values,
    extract_symbols,
    isPair,
    isTwoPair,
    isTriple,
    isQuadruple,
    isFullHouse,
    isStraight,
    isFlush,
    isStraightFlush,
    isRoyalFlush,
    simulate_draws,
    calculate_probabilities
)

class TestPokerSimulator(unittest.TestCase):

    def setUp(self):
        self.deck = generate_deck()

    def test_generate_deck(self):
        self.assertEqual(len(self.deck), 52)
        self.assertTrue(all(card.startswith(('♥', '♦', '♠', '♣')) for card in self.deck))

    def test_extract_values(self):
        cards = ["♥ 10", "♠ 14", "♦ 11"]
        self.assertEqual(extract_values(cards), [10, 11, 14])

    def test_extract_symbols(self):
        cards = ["♥ 10", "♠ 14", "♦ 11"]
        self.assertEqual(extract_symbols(cards), ["♥", "♠", "♦"])

    def test_isPair(self):
        self.assertTrue(isPair(["♥ 10", "♠ 10", "♦ 11", "♣ 12", "♣ 13"]))
        self.assertFalse(isPair(["♥ 10", "♠ 11", "♦ 12", "♣ 13", "♣ 14"]))

    def test_isTwoPair(self):
        self.assertTrue(isTwoPair(["♥ 10", "♠ 10", "♦ 11", "♣ 11", "♣ 13"]))
        self.assertFalse(isTwoPair(["♥ 10", "♠ 10", "♦ 12", "♣ 13", "♣ 14"]))

    def test_isTriple(self):
        self.assertTrue(isTriple(["♥ 10", "♠ 10", "♦ 10", "♣ 12", "♣ 13"]))
        self.assertFalse(isTriple(["♥ 10", "♠ 10", "♦ 11", "♣ 12", "♣ 13"]))

    def test_isQuadruple(self):
        self.assertTrue(isQuadruple(["♥ 10", "♠ 10", "♦ 10", "♣ 10", "♣ 13"]))
        self.assertFalse(isQuadruple(["♥ 10", "♠ 10", "♦ 10", "♣ 12", "♣ 13"]))

    def test_isFullHouse(self):
        self.assertTrue(isFullHouse(["♥ 10", "♠ 10", "♦ 10", "♣ 11", "♣ 11"]))
        self.assertFalse(isFullHouse(["♥ 10", "♠ 10", "♦ 10", "♣ 12", "♣ 13"]))

    def test_isStraight(self):
        self.assertTrue(isStraight(["♥ 10", "♠ 11", "♦ 12", "♣ 13", "♣ 14"]))
        self.assertFalse(isStraight(["♥ 10", "♠ 11", "♦ 13", "♣ 14", "♣ 2"]))

    def test_isFlush(self):
        self.assertTrue(isFlush(["♥ 10", "♥ 11", "♥ 12", "♥ 13", "♥ 14"]))
        self.assertFalse(isFlush(["♥ 10", "♠ 11", "♦ 12", "♣ 13", "♣ 14"]))

    def test_isStraightFlush(self):
        self.assertTrue(isStraightFlush(["♥ 10", "♥ 11", "♥ 12", "♥ 13", "♥ 14"]))
        self.assertFalse(isStraightFlush(["♥ 10", "♥ 11", "♥ 12", "♥ 13", "♣ 14"]))

    def test_isRoyalFlush(self):
        self.assertTrue(isRoyalFlush(["♥ 10", "♥ 11", "♥ 12", "♥ 13", "♥ 14"]))
        self.assertFalse(isRoyalFlush(["♥ 10", "♥ 11", "♥ 12", "♥ 13", "♠ 14"]))

    def test_simulate_draws(self):
        results = simulate_draws(self.deck, 10)
        self.assertEqual(len(results), 10)

    def test_calculate_probabilities(self):
        results = ["One Pair", "Two Pair", "One Pair", "Flush"]
        probabilities = calculate_probabilities(results)
        self.assertAlmostEqual(probabilities["One Pair"], 0.5)
        self.assertAlmostEqual(probabilities["Two Pair"], 0.25)
        self.assertAlmostEqual(probabilities["Flush"], 0.25)

if __name__ == "__main__":
    unittest.main()
