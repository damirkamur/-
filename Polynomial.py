class Polynomial:
    def __init__(self, coefficients):
        self.__coef = coefficients

    def __call__(self, x):
        sum = 0
        xx = 1
        for i in range(len(self.__coef)):
            sum += xx * self.__coef[i]
            xx *= x
        return sum

    def __add__(self, other):
        new_coef = list()
        c1 = self.__coef
        c2 = other.coef
        len_diff = len(c1) - len(c2)
        if len_diff > 0:
            c2 += [0] * len_diff
        elif len_diff < 0:
            c1 += [0] * len_diff
        return Polynomial([c1[i] + c2[i] for i in range(len(c1))])

    @property
    def coef(self):
        return self.__coef


if __name__ == '__main__':
    print('1.', '=' * 20)
    poly = Polynomial([10, -1])
    print(poly(0))
    print(poly(1))
    print(poly(2))

    print('2.', '=' * 20)
    poly1 = Polynomial([0, 0, 1])
    print(poly1(-2))
    print(poly1(-1))
    print(poly1(0))
    print(poly1(1))
    print(poly1(2))
    print()

    poly2 = Polynomial([0, 0, 2])
    print(poly2(-2))
    print(poly2(-1))
    print(poly2(0))
    print(poly2(1))
    print(poly2(2))
    print()

    poly3 = poly1 + poly2
    print(poly3(-2))
    print(poly3(-1))
    print(poly3(0))
    print(poly3(1))
    print(poly3(2))
    print()

    print('3.', '=' * 20)
    poly1 = Polynomial([0, 1])
    poly2 = Polynomial([10])
    poly3 = poly1 + poly2
    poly4 = poly2 + poly1

    print(poly3(-2), poly4(-2))
    print(poly3(-1), poly4(-1))
    print(poly3(0), poly4(0))
    print(poly3(1), poly4(1))
    print(poly3(2), poly4(2))
