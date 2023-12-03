from functools import reduce

# Open the file
file = open("input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()


# Apply reduce on every character of each line
result = 0
for line in contents:
    coordinate = ""
    i = 0
    while len(coordinate) == 0:
        charCoordinate = line[i]
        if charCoordinate.isdigit():
            coordinate = charCoordinate
        i += 1

    i = len(line) - 1
    while len(coordinate) == 1:
        charCoordinate = line[i]
        if charCoordinate.isdigit():
            coordinate += charCoordinate
        i -= 1
    result += int(coordinate)

print(result)
