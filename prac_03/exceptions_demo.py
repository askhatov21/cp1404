"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Otherwise, when a function takes an argument of a type but with an invalid or incorrect value.
2. When will a ZeroDivisionError occur?
zerodivisionerror occurs an attempt is made to divide any number by zero, which is not defined in math.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
To avoid a ZeroDivisionError, you need to add a check before performing the division operation to ensure that the divisor is not zero. If the divisor is zero, you can either skip this step or replace it with another value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")