#Use 2 function (NOT one) for converting Celsius to Fahrenheit and vice versa.

def main():
    MENU = """C convert celsius to fahrenheit
    F - convert fahrenheit to celsius  
    Q - Quit """
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0/5 + 32
            print(f'The result is {fahrenheit:.2f}F')
        elif choice == 'F':
            fahrenheits = float(input("Fahrenheits: "))
            celsius = 5/9 * (fahrenheits - 32)
            print(f"Result is {celsius:.2f} C")

        else:
            print("invalid option")


        print(MENU)
        choice = input(">>>").upper()

    print('Thank you')

def celsius_to_fahrenheit(celsius):
    """Convertion celsius to fahrenheit"""
    return celsius * 9.0 / 5 + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convertion fahrenheit to celsius"""
    return 5 / 9 * (fahrenheit - 32)

main()