from itertools import permutations

def different_numbers(digits: list) -> list:
    """
    Generates all numbers that can be created using the given digits.
    """
    numbers = [int("".join(map(str,el))) for el in permutations(digits)]
    numbers = list(filter(lambda x: len(str(x)) == len(digits), numbers))
    return numbers

def run_diffent_numbers(digits: list, print_numbers: bool = False):
    result = different_numbers(digits)

    print(f"Digits: {digits}")
    print(f"Number of numbers that can be created: {len(result)}")

    if print_numbers:
        print(f"List of created numbers: {result}")


if __name__ == "__main__":
    run_diffent_numbers([5, 6, 7, 8, 9], True)
    print()
    run_diffent_numbers([2, 4, 5, 7, 6, 8])
    print()
    run_diffent_numbers([i for i in range(1, 10)])
    print()
    run_diffent_numbers([i for i in range(0, 10)])
