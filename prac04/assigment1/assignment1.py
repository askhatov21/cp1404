import csv
import random

FILENAME = "file.csv"
def main():
    MENU = "D - Display all places\nR - Recommended a random place\nA - Add a new place\nM - Mark a place as visited\nQ - quit\n"
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

def sort_key(place):
    """Return the key for sorting places by visited status and priority."""
    return (place[3], place[2]) # Sort by visited status ('v' or 'n') and priority (integer)
def display_places(places):
    """Display a formatted list of places."""
    if places:
        places.sort(key=sort_key) # Use the separate sort_key function
        for i , place in enumerate(places, start=1):
            print(f"{i}. {place}")

        else:
            print("No places loaded.")
def recommend_places(places):
    """Function for recommends for random places."""

    print("Recommendation logic not implemented yet.")

def get_positive_int(prompt):
    """Prompt the user for a positive integer, with validation."""
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Number must be > 0")
        except ValueError:
            print("Invalid input; enter a valid number")
def mark_visited(places):
    """Mark a place as visited."""
    unvisited_place = [place for place in places if place[3] == "n"]
    if not unvisited_place:
        print("No unvisited places")
        return
    display_places(places)
    place_num = get_positive_int("Enter the number of a place to mark as visited: ")

    if 0 < place_num <= len(places) and places[place_num - 1][3] == "n":
        places[place_num - 1][3] = 'v'
        print(f'{places[place_num - 1][0]}in {places[place_num - 1][1]} visited!')
    else:
        print("Invalid place number")


def save_places(places, filename='file.csv'):
    """Function for saving places to a CSV file."""
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(places)
    print(f'{len(places)} places saved to {filename}')
main()