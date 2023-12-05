import re
from functools import reduce


def get_count(color, substring):
    return sum(
        list(
            map(
                lambda x: int(x[0 : -1 * (len(color) + 1)]),
                re.findall(f"[0-9]+ {color}", substring),
            )
        )
    )


def get_game_power(game):
    min_numbers_required = [0, 0, 0]
    for hand in game.split(";"):
        min_numbers_required[0] = max(get_count("red", hand), min_numbers_required[0])
        min_numbers_required[1] = max(get_count("green", hand), min_numbers_required[1])
        min_numbers_required[2] = max(get_count("blue", hand), min_numbers_required[2])
    return reduce((lambda x, y: x * y), min_numbers_required)


answer = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        answer += get_game_power(line)

print(answer)
