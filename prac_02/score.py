import random
def main():
 score = int(input("Scores: "))
 result = determine_result(score)
 print(result)

 random_score = random.randint(0, 100)
 random_result = determine_result(random_score)
 print(f'Random score: {random_score}, Result: {random_result}')

def determine_result(score):
    """Function takes an estimate and returns the result without output """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"



main()