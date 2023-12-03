import re

# Open the file
file = open("./day2/input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()

result = 0

# red, green, blue
realValues = [12, 13, 14]
realRed = 12
realGreen = 13
realBlue = 14


def get_numbers_from_string(string):
    numbers = re.findall(r'\d+', string)
    return list(map(int, numbers))


for line in contents:
    # Get the part of the line after ":"
    line_parts = line.split(":")
    gameID = line_parts[0].strip()
    gameValues = line_parts[1].strip().split(";")
    games = list(map(lambda x: x.strip(), gameValues))
    games = list(map(lambda x: x.split(','), games))

    impossibleGame = False
    for game in games:
        red, green, blue = 0, 0, 0
        for value in game:
            if "green" in value:
                green = get_numbers_from_string(value)[0]
            elif "red" in value:
                red = get_numbers_from_string(value)[0]
            elif "blue" in value:
                blue = get_numbers_from_string(value)[0]

        if not (realRed >= red and realGreen >= green and realBlue >= blue):
            impossibleGame = True

    if not impossibleGame:
        print(gameID, games)
        result += get_numbers_from_string(gameID)[0]


print(result)
