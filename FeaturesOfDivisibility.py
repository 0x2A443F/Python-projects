import concurrent.futures


def getNumbers(minNumber: int, maxNumber: int, dividers: [int]):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda d: set([i for i in range(minNumber, maxNumber) if i % d == 0]), dividers))
    return results


def countUniqueNumbers(numbers: [set[int]]):
    all_unique_digits = set.union(*numbers)
    return len(all_unique_digits)


def countNumbersDivisibleByAllDividers(numbers: [set[int]]):
    common_elements = set.intersection(*numbers)
    return len(common_elements)


if __name__ == '__main__':
    minNumber, maxNumber = [int(i) for i in input("Set range: ").split()]
    dividers: [int] = [int(i) for i in input("Set dividers: ").split()]

    numbers = getNumbers(minNumber, maxNumber, dividers)
    print(f"Number of numbers divisible by any divisors: {countUniqueNumbers(numbers)}")
    print(f"Number of numbers divisible by all divisors: {countNumbersDivisibleByAllDividers(numbers)}")
