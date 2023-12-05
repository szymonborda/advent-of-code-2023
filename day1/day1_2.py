NUMBERS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

NUMBERS_KEYS = NUMBERS.keys()

answer = 0


def get_word_number_or_none(chars):
    for word in NUMBERS_KEYS:
        if word in chars:
            return NUMBERS[word]


with open("input.txt") as input_file:
    for line in input_file.readlines():
        number = ""
        word_number = ""

        for char in line:
            if char.isdigit():
                number += char
                break

            word_number += char

            if word_number_to_add := get_word_number_or_none(word_number):
                number += word_number_to_add
                break

        word_number = ""

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                number += line[i]
                break

            word_number = line[i] + word_number

            if word_number_to_add := get_word_number_or_none(word_number):
                number += word_number_to_add
                break

        answer += int(number)

print(answer)
