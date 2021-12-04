def read_input() -> list:
    with open("input3.txt", "r") as data:
        return [list(lines.strip()) for lines in data]


def part_one(array: list):
    gamma = ""
    epsilon = ""
    for x in range(len(array[0])):
        zero = 0
        one = 0
        for y in range(len(array)):
            if array[y][x] == '1':
                one += 1
            else:
                zero += 1
        if one > zero:
            gamma += "1"
            epsilon += "0"
        else:
            epsilon += "1"
            gamma += "0"
    return int(gamma, 2) * int(epsilon, 2)


def find_one_or_zero(array: list, index: int):
    zero = 0
    one = 0
    for y in range(len(array)):
        if array[y][index] == '1':
            one += 1
        else:
            zero += 1
    return 1 if one >= zero else 0


def oxygen_generator_rating(array: list):
    index = 0
    while len(array) > 1:
        one_or_zero = find_one_or_zero(array, index)
        if one_or_zero == 1:
            array = [row for row in array if row[index] == '1']
        else:
            array = [row for row in array if row[index] == '0']
        index += 1

    return "".join(array[0])


def co2_scrubber_rating(array: list):
    index = 0
    while len(array) > 1:
        one_or_zero = find_one_or_zero(array, index)
        if one_or_zero == 1:
            array = [row for row in array if row[index] == '0']
        else:
            array = [row for row in array if row[index] == '1']
        index += 1

    return "".join(array[0])


if __name__ == '__main__':
    print(f"First star = {part_one(read_input())}")
    print(f"Second Star = {int(oxygen_generator_rating(read_input()),2) * int(co2_scrubber_rating(read_input()),2)}")
