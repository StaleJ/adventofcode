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


if __name__ == '__main__':
    print(f"First star = {part_one(read_input())}")
