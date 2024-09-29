scores = int(input("Scores: "))
if scores < 0 or scores > 100:
 print("Invalid score")
elif scores >= 90:
 print("Excellent")
elif scores >= 50:
 print("Pass")
else:
 print("Bad")