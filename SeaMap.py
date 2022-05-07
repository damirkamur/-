class SeaMap:
    def __init__(self):
        self.__field = [['.' for _ in range(10)] for _ in range(10)]

    def shoot(self, row, col, result):
        if result == 'miss':
            self.__field[row][col] = '*'
        elif result == 'hit':
            self.__field[row][col] = 'X'
        elif result == 'sink':
            self.__field[row][col] = 'X'
            self.__update(row, col)

    def cell(self, row, col):
        return self.__field[row][col]

    def __update(self, row, col):
        # определяем контуры корабля
        points = [[row, col]]
        # →
        if col < 9:
            r, c = row, col + 1
            while not (self.__field[r][c] == '.' or self.__field[r][c] == '*'):
                points.append([r, c])
                c += 1
                if c > 9:
                    break
        # ←
        if col > 0:
            r, c = row, col - 1
            while not (self.__field[r][c] == '.' or self.__field[r][c] == '*'):
                points.append([r, c])
                c -= 1
                if c < 0:
                    break
        # ↑
        if row > 0:
            r, c = row - 1, col
            while not (self.__field[r][c] == '.' or self.__field[r][c] == '*'):
                points.append([r, c])
                r -= 1
                if r < 0:
                    break
        # ↓
        if row < 9:
            r, c = row + 1, col
            while not (self.__field[r][c] == '.' or self.__field[r][c] == '*'):
                points.append([r, c])
                r += 1
                if r > 9:
                    break
        for r, c in points:
            # справа
            if c < 9:
                if self.__field[r][c + 1] == '.':
                    self.__field[r][c + 1] = '*'
            # слева
            if c > 0:
                if self.__field[r][c - 1] == '.':
                    self.__field[r][c - 1] = '*'
            # снизу
            if r < 9:
                if self.__field[r + 1][c] == '.':
                    self.__field[r + 1][c] = '*'
            # сверху
            if r > 0:
                if self.__field[r - 1][c] == '.':
                    self.__field[r - 1][c] = '*'
            # справа-сверху
            if c < 9 and r > 0:
                if self.__field[r - 1][c + 1] == '.':
                    self.__field[r - 1][c + 1] = '*'
            # слева-сверху
            if c > 0 and r > 0:
                if self.__field[r - 1][c - 1] == '.':
                    self.__field[r - 1][c - 1] = '*'
            # справа-снизу
            if c < 9 and r < 9:
                if self.__field[r + 1][c + 1] == '.':
                    self.__field[r + 1][c + 1] = '*'
            # слева-сверху
            if c > 0 and r < 9:
                if self.__field[r + 1][c - 1] == '.':
                    self.__field[r + 1][c - 1] = '*'


sm = SeaMap()
sm.shoot(0, 0, 'sink')
sm.shoot(0, 9, 'sink')
sm.shoot(9, 0, 'sink')
sm.shoot(9, 9, 'sink')

sm.shoot(3, 3, 'hit')
sm.shoot(3, 5, 'hit')
sm.shoot(3, 2, 'hit')
sm.shoot(3, 4, 'sink')

for row in range(10):
    for col in range(10):
        print(sm.cell(row, col), end='')
    print()
