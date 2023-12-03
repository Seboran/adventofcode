import re

# Open the file
file = open("./day3/input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()

result = 0

patternSpecialChar = r"[^\d.]+"


for index, line in enumerate(list(map(lambda x: x.strip(), contents))):
  pattern = r"\d+"
  for match in re.finditer(pattern, line):
    startMatch, endMatch = match.start(), match.end()

    # check right of last value
    if (endMatch < len(line)):
      nextChar = line[endMatch]
      if (re.search(patternSpecialChar, nextChar)):
        result += int(match.group(0))
        print(match)
        continue
    # check left of first value
    if (startMatch > 0):
      previousChar = line[startMatch - 1]
      if (re.search(patternSpecialChar, previousChar)):
        result += int(match.group(0))
        print(match)
        continue
        
    # check over and under each value
    if index > 0:
      beginningLineAbove = startMatch
      # Check diagonal above left
      if (startMatch > 0):
        beginningLineAbove = startMatch - 1
      endLineAbove = endMatch
      if (endMatch < len(line)):
        endLineAbove = endMatch + 1
      
      lineAbove = contents[index - 1][beginningLineAbove:endLineAbove]

      if (re.search(patternSpecialChar, lineAbove)):
        result += int(match.group(0))
        print(match)
        continue
    if index < len(contents) - 1:
      beginningLineBelow = startMatch
      # Check diagonal above left
      if (startMatch > 0):
        beginningLineBelow = startMatch - 1
      endLineBelow = endMatch
      if (endMatch < len(line)):
        endLineBelow = endMatch + 1
      
      lineBelow = contents[index + 1][beginningLineBelow:endLineBelow]
      if (re.search(patternSpecialChar, lineBelow)):
        result += int(match.group(0))
        print(match)
        continue




print(result)

  
  