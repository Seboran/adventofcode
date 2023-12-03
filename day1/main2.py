from functools import reduce
import re

# Open the file
file = open("input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()


# Dictionary to map spelled-out numbers to digits
number_mapping = {
  "one": "1",
  "two": "2",
  "three": "3",
  "four": "4",
  "five": "5",
  "six": "6",
  "seven": "7",
  "eight": "8",
  "nine": "9"
}

# Apply reduce on every character of each line
result = 0
# contents = ["eightwothree"]
for line in contents :
  pattern = r"(?=(one|two|three|four|five|six|seven|eight|nine|[0-9]))"


  matches = re.findall(pattern, line)

  print(line.lstrip())

  intermediateValue = int(number_mapping.get(matches[0], matches[0]) + number_mapping.get(matches[-1], matches[-1]))
  print(intermediateValue, "\n")
  result += intermediateValue

print(result)



