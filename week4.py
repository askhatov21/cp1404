names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))
name_to_remove = input("Who do you want to remove")

names.remove(name_to_remove)
print(names)

while name_to_remove != "":
    try:
        name_to_remove(name_to_remove)
    except ValueError:
        print("Name not in the list!")
    print(names)
    name_to_remove = input("Who do you want to remove?")

print("Good try")


