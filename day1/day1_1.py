answer = 0

with open("input.txt") as input_file:
    for line in input_file.readlines():
        number = ""

        for char in line:
            if char.isdigit():
                number += char
                break

        for i in range(len(line) - 1, -1, -1):
            if line[i].isdigit():
                number += line[i]
                break

        answer += int(number)

print(answer)
