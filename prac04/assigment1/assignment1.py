import csv

def main():
MENU = " D - Display all places\n R - Recommended a random place\n A - Add a new place\n M - Mark a place as visited\n Q - quit\n"
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




main()