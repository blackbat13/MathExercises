from itertools import permutations


def different_numbers(digits: list, condition) -> list:
    """
    Generates all numbers that can be created using the given digits.
    """
    numbers = [int("".join(map(str, el))) for el in permutations(digits)]
    numbers = list(filter(lambda x: len(str(x)) == len(digits), numbers))
    if condition is not None:
        numbers = list(filter(condition, numbers))

    return numbers


def run_diffent_numbers(digits: list, condition = None, print_numbers: bool = False):
    result = different_numbers(digits, condition)

    print(f"Digits: {digits}")
    print(f"Number of numbers that can be created: {len(result)}")

    if print_numbers:
        print(f"List of created numbers: {result}")


if __name__ == "__main__":
    run_diffent_numbers([5, 6, 7, 8, 9], print_numbers=True)  # 120
    print()
    run_diffent_numbers([2, 4, 5, 7, 6, 8])  # 720
    print()
    run_diffent_numbers([i for i in range(1, 10)])  # 362880
    print()
    run_diffent_numbers([i for i in range(0, 10)])  # 3265920
    print()
    run_diffent_numbers([i for i in range(1, 6)], condition=lambda x: x < 50000, print_numbers=True)  # 96
    print()
    run_diffent_numbers([i for i in range(1, 6)], condition=lambda x: x > 30000, print_numbers=True)  # 72
