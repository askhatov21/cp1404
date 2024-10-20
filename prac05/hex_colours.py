COLOR_TO_HEX = {"AliceBlue": "#f0f8ff",
                "Acid Green": "#b0bf1a",
                "Alizarin crimson": "#e32636",
                "Amaranth": "#e52b50",
                "Amber": "#ffbf00",
                "Amethyst": "#9966cc",
                "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": '#ffefdb',
                "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0"}

color_name = input("Enter a color name: ").strip()

while color_name !="":
    try:
        """Convert input to case-intensive lookup (title-casing the input)"""
        hex_code = COLOR_TO_HEX[color_name.title()]
        print(f'{color_name.title()} is {hex_code}')
    except KeyError:
        print("invalid color name")

    color_name = input("Enter a color name: ").strip()

print("Program exited")
