import unittest


def read_input() -> list:
    with open("input1.txt", "r") as file:
        return [int(i) for i in file]


def sonar_sweep(array: list) -> int:
    count = 0
    previous = array[0]
    array.remove(array[0])
    for m in array:
        if previous < m:
            count += 1
        previous = m
    return count


def sonar_sweep_part_two(array: list) -> list:
    answer = []
    for i in range(len(array) - 2):
        answer.append(sum(array[i:i + 3]))
    return answer


def main():
    first_star = sonar_sweep(read_input())
    second_star = sonar_sweep(sonar_sweep_part_two(read_input()))
    print(f"Answer to the first star = {first_star}")
    print(f"Answer to the second star = {second_star}")


if __name__ == '__main__':
    main()


class TestDay1(unittest.TestCase):

    def test_case1(self):
        test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sonar_sweep(test_list), 7, "Should be 7")

    def test_list_is_correct(self):
        expected = [607, 618, 618, 617, 647, 716, 769, 792]
        test_list = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.assertEqual(sonar_sweep_part_two(test_list), expected)
