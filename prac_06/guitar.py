class Guitar:
    """Represent a guitar """
    def __init__(self, name, year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"


    def get_age(self):
        """Return the age of the guitar."""
        current_year = 2022
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is vintage (50 years or older)."""
        return self.get_age() >= 50

def main():
        #Create an instance of the Guitar class
    my_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(my_guitar) #Output:Gibson L-5 CES (1922) : $16,035.40

    #Print the age of the guitar
    print(f'The guitar is {my_guitar.get_age()} years old.')
    print(f"Is the guitar vintage? {'Yes' if my_guitar.is_vintage() else 'No'}")

if __name__ == "__main__":

    main()