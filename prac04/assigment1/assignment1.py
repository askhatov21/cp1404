import csv

def main():
MENU = " D - Display all places\nR - Recommended a random place\nA - Add a new place\nM - Mark a place as visited\nQ - quit\n"
print("Travel Tracker 1.0 - by Askhatov Amir")
places = load_places() # Load location  from csv file

choice = ""
while choice != "Q":
    print(MENU)
    choice = input(">>>").upper()
    if choice == "D":
        display_places(places)
    elif choice == "R":
        recommend_places(places)
    elif choice == "M":
        mark_visited(places)
    elif choice == "Q":
        save_places(places)
        print("Goodbye!")
    else:
        print("Invalid menu choice")

def load_places(filename="file.csv"):
    """Load places from a CSV file and returns them as a list"""
    places = []
    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                places.append(row)
        print(f'{len(places)} places loaded from {filename}')
    except FileNotFoundError:
        print(f'File {filename} not found.')
    return places

def recommend_place(places):
    """Function for recommends for random places."""
    #Logic for recommend place
    print("Recommendation logic not implemented yet.")


main()