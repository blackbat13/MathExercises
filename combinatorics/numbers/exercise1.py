from itertools import permutations

def different_numbers(digits: list) -> list:
    """
    Generates all numbers that can be created using the given digits.
    """
    numbers = [int("".join(map(str,el))) for el in permutations(digits)]
    return numbers



a = different_numbers([5, 6, 7, 8, 9])
b = different_numbers([2, 4, 5, 7, 6, 8])

print(f"a)\n\t  answer: {len(a)}\n\t  numbers: {a}")
print(f"b)\n\t  answer: {len(b)}\n\t  numbers: {b}")
