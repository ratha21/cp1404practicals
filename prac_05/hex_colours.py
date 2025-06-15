

COLOUR_NAME_TO_CODE = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    if colour_name in COLOUR_NAME_TO_CODE:
        print(f"{colour_name.title()} is {COLOUR_NAME_TO_CODE[colour_name]}")
    else:
        print("Invalid colour name")
    colour_name = input("Enter a colour name: ").lower()
