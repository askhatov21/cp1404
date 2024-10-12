"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_subject_details(data)
    print(data)


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME, 'r')
    for line in input_file:
        line = line.strip() #Remove the \n
        parts = line.split(',') # Separate the data into its parts
        parts[2] = int(parts[2]) # Converts the number to an integer
        data.append(parts)  # Add the processed list to the data list
    input_file.close()
    return data

def display_subject_details(data):
    """Display the subject details in a specific format."""
    for subject in data:
        print(f'{subject[0]} is taught by {subject[1]} and has {subject[2]} students')


main()