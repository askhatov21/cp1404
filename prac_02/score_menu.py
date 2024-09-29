import random

#I should write main function and other function, write the menu, write the valid_score function

def main():
    valid_score = get_valid_score()
    MENU = """ G - Get a valid score (must be 0-100 inclusive)
    P = print result
    S = show stars
    Q = Quit"""
    print(MENU)
    choice = input(">>>").upper()

    while choice != "Q":
        if choice == "G":
            valid_score = get_valid_score()
            print(f'The score is {valid_score}')
        elif choice == "P":
            result = determine_result(valid_score)
            print(f"Result: {result}")

        elif choice == "S":
            show_stars(valid_score)
        else:
            print("Invalid option")

        print(MENU)
        choice = input(">>>").upper()

    print("Thank you, farewell! ")

def get_valid_score():
    """The user receives a correct rating from 0 to 100 inclusive"""
    score = -1
    while score < 0 or score > 100:
        score_input = int(input("Enter a valid score (0-100): "))
        score = int(score_input)
        if score < 0 or score > 100:
            print("Invalid score. Please enter a score between 0 and 100.")
        else:
            print("Invalid input. Please enter a number")
        return score

def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"
def show_stars(score):
    """Prints the number of stars equal to the rating"""
    print("*" * score)


main()

