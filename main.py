import random


def generate_random_numbers(amount, minRange, maxRange):
    numbers = []
    for i in range(amount):
        number = random.randint(minRange, maxRange)
        while number in numbers:
            number = random.randint(minRange, maxRange)
        numbers.append(number)
    return numbers


if __name__ == '__main__':
    amount = 2
    minRange = 1
    maxRange = 10

    random_numbers = generate_random_numbers(amount, minRange, maxRange)
    print(random_numbers)
