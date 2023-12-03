import re

# Open the file
file = open("./day3/input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()

result = 0

patternSpecialChar = r"[^\d.]+"


# Convert contents to bidimensional array
bidimensionalArray = [list(line.strip()) for line in contents]
width = len(bidimensionalArray[0])
height = len(bidimensionalArray)

possibleGears = []

for j in range(width):
  for i in range(height):
    cell = bidimensionalArray[i][j]
    if (cell == "*"):
      possibleGears.append((i, j))

print(possibleGears)

ratiosList = []

# get all ratios and their start and end position
for index, line in enumerate(list(map(lambda x: x.strip(), contents))):
  pattern = r"\d+"
  for match in re.finditer(pattern, line):
    startMatch, endMatch = match.start(), match.end()
    ratiosList.append((int(match.group(0)), startMatch, endMatch, index))

# get all possible gears

for possibleGear in possibleGears:
  possibleGearX, possibleGearY = possibleGear
  # get adjacent cells
  adjacentCells = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
  possibleAdjacentCells = list(map(lambda x: (possibleGearX + x[0], possibleGearY + x[1]), adjacentCells))

  correspondingGears = []
  for index, ratio in enumerate(ratiosList):
    if len(correspondingGears) != 2:
      ratioValue, ratioStart, ratioEnd, ratioIndex = ratio
      for possibleAdjacentCell in possibleAdjacentCells:
        if not ratioValue in correspondingGears:
          adjacentCellX, adjacentCellY = possibleAdjacentCell
          isSameLine = ratioIndex == adjacentCellX
          isInPositionRange = adjacentCellY in range(ratioStart, ratioEnd)
          if (isSameLine and isInPositionRange):
            correspondingGears.append(ratioValue)
            print(ratioValue)
  if (len(correspondingGears) == 2):
    print(correspondingGears)
    result += correspondingGears[0] * correspondingGears[1]

print(result)
