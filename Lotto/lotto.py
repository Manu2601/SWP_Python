import random
def initialize_lotto():
    return list(range(45))

def random_numbers(lottozahlen):
    randomNumbers = []
    for j in range(6):
        randomIndex = random.randint(0, 44 - j)
        randomNumber = lottozahlen[randomIndex]
        randomNumbers.append(randomNumber)
        lastIndex = 44 - j
        lastNumber = lottozahlen[lastIndex]
        lottozahlen[randomIndex] = lastNumber
        lottozahlen[lastIndex] = randomNumber
    return randomNumbers

def update_statistics(randomNumbers, statistics):
    for number in randomNumbers:
        statistics[number] = statistics.get(number, 0) + 1

if __name__ == "__main__":
    statistics = {}
    for i in range(1000):
        lottozahlen = initialize_lotto()
        randomNumbers = random_numbers(lottozahlen)
        update_statistics(randomNumbers, statistics)
    print(statistics)
    