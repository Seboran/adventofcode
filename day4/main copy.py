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

SCRATCH_CARDS_WITH_COPIES = list(
    map(lambda line: (line, 1), contents))
for index, (line, copies) in enumerate(SCRATCH_CARDS_WITH_COPIES):
    CARD_MATCH = re.match(CARD_PATTERN, line)
    CARD_NUMBER, WINNING_NUMBERS, SCRATCHCARDS = CARD_MATCH.group(
        1), CARD_MATCH.group(2), CARD_MATCH.group(3)
    WINNING_NUMBERS_LIST = re.findall(NUMBER_PATTERN, WINNING_NUMBERS)
    SCRATCHCARDS_LIST = re.findall(NUMBER_PATTERN, SCRATCHCARDS)

    NUMBER_VALID_NUMBERS = 0
    for scratchCard in SCRATCHCARDS_LIST:
        if scratchCard in WINNING_NUMBERS_LIST:
            NUMBER_VALID_NUMBERS += 1
    for indexNewCopies in range(index + 1, index + 1 + NUMBER_VALID_NUMBERS):
        localLine, localCopies = SCRATCH_CARDS_WITH_COPIES[indexNewCopies]
        SCRATCH_CARDS_WITH_COPIES[indexNewCopies] = (
            localLine, localCopies + copies)
    print(line, copies, sep="\n")

print("\nResult")
print(reduce(lambda x, y: y[1] + x, SCRATCH_CARDS_WITH_COPIES, 0))
