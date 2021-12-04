def read_input():
    index = 0
    hashmap = {}
    temp = []
    with open("small_input4.txt", "r") as data:
        numbers = data.readline()
        array = [line.strip().split() for line in data]
        array.remove(array[0])
        for element in array:
            if element:
                temp.append(element)
            else:
                hashmap[index] = temp
                index += 1
                temp = []
    hashmap[index] = temp
    return hashmap


if __name__ == '__main__':
    print(read_input())
