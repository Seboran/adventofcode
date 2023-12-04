from functools import reduce
import re

# Open the file with explicit encoding
file = open("./day4/input.txt", "r", encoding="utf-8")

# Read the contents of the file
contents = file.readlines()

# Close the file
file.close()

CARD_PATTERN = r"Card\s+(\d+):(.*)\|(.*)"
NUMBER_PATTERN = r"\d+"

RESULT = 0
for line in contents:
    CARD_MATCH = re.match(CARD_PATTERN, line)
    CARD_NUMBER, WINNING_NUMBERS, SCRATCHCARDS = CARD_MATCH.group(
        1), CARD_MATCH.group(2), CARD_MATCH.group(3)
    WINNING_NUMBERS_LIST = re.findall(NUMBER_PATTERN, WINNING_NUMBERS)
    SCRATCHCARDS_LIST = re.findall(NUMBER_PATTERN, SCRATCHCARDS)

    SCRATCHCARD_VALUE = 0
    for scratchCard in SCRATCHCARDS_LIST:
        if scratchCard in WINNING_NUMBERS_LIST:
            if SCRATCHCARD_VALUE == 0:
                SCRATCHCARD_VALUE = 1
            else:
                SCRATCHCARD_VALUE = SCRATCHCARD_VALUE * 2

    RESULT += SCRATCHCARD_VALUE

print(RESULT)
