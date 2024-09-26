import random
def initialize_lotto():
    lottozahlen = []
    for i in range(45):
        lottozahlen.append(i)
    return lottozahlen

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
        if number in statistics:
            statistics[number] += 1
        else:
            statistics[number] = 1

if __name__ == "__main__":
    lottozahlen = initialize_lotto()
    statistics = {}
    for i in range(1000):
        randomNumbers = random_numbers(lottozahlen)
        update_statistics(randomNumbers, statistics)
    print(statistics)
    print("Random Numbers: ")