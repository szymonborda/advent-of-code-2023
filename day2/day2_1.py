import re


def get_count(color, substring):
    return sum(
        list(
            map(
                lambda x: int(x[0 : -1 * (len(color) + 1)]),
                re.findall(f"[0-9]+ {color}", substring),
            )
        )
    )


def is_game_valid(game):
    for hand in game.split(";"):
        if (
            get_count("red", hand) > 12
            or get_count("green", hand) > 13
            or get_count("blue", hand) > 14
        ):
            return False
    return True


def get_game_id(game):
    return int(game.split(":")[0].split(" ")[1])


answer = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        if is_game_valid(line):
            answer += get_game_id(line)

print(answer)
