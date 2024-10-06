FILENAME = "name.txt"
"""Query the nme and write it to file"""
name = input("Name: ")
out_file = open('name.txt', "w")
out_file.write(name)
out_file.close()
print(f"Your name has been written to name.txt")

#2.
"""Opening the file and reading the name for output"""
in_file = open('name.txt', "r")
name = in_file.read().strip()
in_file.close()
print(f'Hi {name}')


#3.
"""Reading the first two numbers and outputting their sum"""
with open("numbers.txt", "r") as file:
    first_number = int(file.readline().strip())
    second_number = int(file.readline().strip())
    print(f'The sum of the first two number is: {first_number + second_number}')


#4.
"""Reading whole numbers and count their sum"""
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(f'The total of all numbers is: {total}')