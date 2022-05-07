class Queue:
    def __init__(self, *args):
        self.__array = [arg for arg in args]

    def __str__(self):
        string = ' -> '.join(map(str, self.__array))
        return f'[{string}]'

    def __eq__(self, other):
        return True if self.__array == other.array else False

    def __add__(self, other):
        return Queue(*(self.__array + other.array))

    def __iadd__(self, other):
        self.__array = self.__array + other.array
        return self

    def __rshift__(self, N):
        return Queue(*self.__array[N:])

    def __next__(self):
        return Queue(*self.__array[1:])

    def append(self, *args):
        for elem in args:
            self.__array.append(elem)

    def copy(self):
        return Queue(*self.__array[:])

    def pop(self):
        if self.__array == list():
            return
        else:
            elem = self.__array[0]
            self.__array.pop(0)
            return elem

    def extend(self, other):
        self.__array = self.__array + other.array

    def next(self):
        return Queue(*self.__array[1:])

    @property
    def array(self):
        return self.__array


if __name__ == '__main__':
    q1 = Queue(1, 2, 3)
    print(q1)
    q1.append(4, 5)
    print(q1)
    qx = q1.copy()
    print(qx.pop())
    print(qx)
    q2 = q1.copy()
    print(q2)
    print(q1 == q2, id(q1) == id(q2))
    q3 = q2.next()
    print(q1, q2, q3, sep='\n')
    print(q1 + q3)
    q3.extend(Queue(1, 2))
    print(q3)
    q4 = Queue(1, 2)
    q4 += q3 >> 4
    print(q4)
    q5 = next(q4)
    print(q4)
    print(q5)
