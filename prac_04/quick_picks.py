import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6


def main():
    number_of_picks = int(input("How many quick picks? "))
    for _ in range(number_of_picks):
        quick_pick = generate_quick_pick()
        print_formatted_quick_pick(quick_pick)

def generate_quick_pick():
    """Generates a list of unique random numbers, sorted in ascending order."""
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        num = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if num not in quick_pick:
            quick_pick.append(num)
    quick_pick.sort()
    return quick_pick

def print_formatted_quick_pick(quick_pick):
    """Prints the numbers of a quick pick neatly aligned."""
    formatted_numbers = ' '.join(f"{number:2}" for number in quick_pick)
    print(formatted_numbers)


main()