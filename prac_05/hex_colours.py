"""
CP1404/CP5632 Practical
Hex colour in a dictionary
Colour name will show their respective hex code
"""

COLOUR_TO_HEX = {"BLACK": "#000000", "AQUA": "##00ffff", "BEIGE": "#f5f5dc",
                 "BLUE1": "#0000ff", "BRASS": "#b5a642", "BRICK RED": "#cb4154",
                 "BRONZE": "#cd7f32", "BROWN": "#a52a2a", "BURLYWOOD": "#deb887",
                 "BURNT ORANGE": "#cc5500"}
print(COLOUR_TO_HEX)

while True:
    try:
        colour_name = input("Enter colour name: ").upper()
        if colour_name == "":
            break
        else:
            colour_hex = COLOUR_TO_HEX[colour_name]
            print(f"Hex code for colour {colour_name:3} is {colour_hex}")
    except KeyError:
        print("Invalid colour name")
