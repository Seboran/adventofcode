import re

# Open the file
file = open("./day2/input.txt", "r")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()

result = 0

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

  red, green, blue = 0, 0, 0

  for game in games:
    for value in game:
      if "green" in value:
        value = get_numbers_from_string(value)[0]
        if (value > green):
          green = value
      elif "red" in value:
        value = get_numbers_from_string(value)[0]
        if (value > red):
          red = value
      elif "blue" in value:
        value = get_numbers_from_string(value)[0]
        if (value > blue):
          blue = value

    
  
  
  result += red * green * blue
  



print(result)

  
  