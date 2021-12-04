def read_input():
    data = []
    with open("input2.txt", "r") as file:
        for lines in file:
            data_tuple = tuple(lines.split())
            data.append(data_tuple)
    return data


def dive_day2(array: list) -> int:
    horizontal_position = 0
    depth = 0
    for index, item in enumerate(array):
        direction = item[0]
        number = int(item[1])
        if direction == 'forward':
            horizontal_position += number
        elif direction == 'down':
            depth += number
        else:
            depth -= number
    return horizontal_position * depth


def part_two(array: list) -> int:
    horizontal = 0
    aim = 0
    depth = 0

    for index, item in enumerate(array):
        direction = item[0]
        number = int(item[1])
        if direction == 'forward':
            if aim != 0:
                depth += number * aim
            horizontal += number
        elif direction == 'down':
            aim += number
        else:
            aim -= number
    return horizontal * depth


if __name__ == '__main__':
    print(f"First star = {dive_day2(read_input())}")
    print(f"Second star = {part_two(read_input())}")
