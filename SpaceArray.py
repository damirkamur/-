class SpaceArray:
    def __init__(self):
        self.__elements = dict()

    def __getitem__(self, item):
        return self.__elements.get(item, 0)

    def __setitem__(self, key, value):
        self.__elements[key] = value


if __name__ == '__main__':
    print('1.', '=' * 20)
    arr = SpaceArray()
    arr[1] = 10
    arr[8] = 20
    for i in range(10):
        print('arr[{}] = {}'.format(i, arr[i]))

    print('2.', '=' * 20)
    arr = SpaceArray()
    arr[10] = 123
    for i in range(8, 13):
        print('arr[{}] = {}'.format(i, arr[i]))

    print('3.', '=' * 20)


    def print_elem(array, ind):
        print('arr[{}] = {}'.format(ind, array[ind]))


    arr = SpaceArray()
    index = 1000000000
    arr[index] = 123
    print_elem(arr, index - 1)
    print_elem(arr, index)
    print_elem(arr, index + 1)
