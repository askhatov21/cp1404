#Test Scores
#Pseudocode:

#constant num_scores = 4

#create an empty list to store the scores

#for i from 1 to num_scores
#    print "score " + i + ": "
#    get the score from the user
#    add the score to the list

#for i from 1 to num_scores
#    print "score " + i + " was " + score + ", which is " + jcu_grade(score)

#calculate the average score
#print "the average score was " + average score

#if the last score in the list is higher than the average score
#    print "the trend is positive"
#else
    #print "the trend is not positive"


def jcu_grade(score):
    if score < 50:
        return "N"
    elif score < 65:
        return "P"
    elif score < 75:
        return "C"
    elif score < 85:
        return "D"
    else:
        return "HD"

def main():
    num_scores = 4
    scores = []

    for i in range(num_scores):
        while True:
            try:
                score = float(input(f"Score {i+1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Error: Score must be between 0 and 100.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")

    for i, score in enumerate(scores, start=1):
        print(f"Score {i} was {score:.1f}, which is {jcu_grade(score)}")

    average_score = sum(scores) / len(scores)
    print(f"The average score was {average_score:.3f}")

    trend = "positive" if scores[-1] > average_score else "not positive"
    print(f"The trend is {trend}")

if __name__ == "__main__":
    main()

