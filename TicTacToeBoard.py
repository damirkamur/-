class TicTacToeBoard:
    def __init__(self):
        self.__field = [['-', '-', '-'],
                        ['-', '-', '-'],
                        ['-', '-', '-']]
        self.__queue = 'X'

    def new_game(self):
        self.__init__()
        return 'Новая игра'

    def get_field(self):
        return self.__field

    def check_field(self):
        for iline in range(3):
            if self.__field[iline][0] == self.__field[iline][1] == self.__field[iline][2]:
                if self.__field[iline][0] != '-':
                    return self.__field[iline][0]
        for irow in range(3):
            if self.__field[0][irow] == self.__field[1][irow] == self.__field[2][irow]:
                if self.__field[0][irow] != '-':
                    return self.__field[0][irow]
        if self.__field[0][0] == self.__field[1][1] == self.__field[2][2]:
            if self.__field[0][0] != '-':
                return self.__field[0][0]
        if self.__field[0][2] == self.__field[1][1] == self.__field[2][0]:
            if self.__field[0][2] != '-':
                return self.__field[0][2]
        for i in range(3):
            if '-' in self.__field[i]:
                return None
        return 'D'

    def make_move(self, row, col):
        row -= 1
        col -= 1
        check = self.check_field()
        if check == 'X' or check == '0':
            return 'Игра уже завершена'

        if self.__field[row][col] != '-':
            return f'Клетка {row + 1}, {col + 1} уже занята'

        self.__field[row][col] = self.__queue
        self.__queue = '0' if self.__queue == 'X' else 'X'
        new_check = self.check_field()
        if new_check == 'X':
            return 'Победил игрок X'
        elif new_check == '0':
            return 'Победил игрок 0'
        elif new_check == 'D':
            return 'Ничья'
        else:
            return 'Продолжаем играть'


if __name__ == '__main__':
    board = TicTacToeBoard()
    print(*board.get_field(), sep='\n')
    print(board.make_move(1, 1))
    print(*board.get_field(), sep='\n')
    print(board.make_move(1, 1))
    print(board.make_move(1, 2))
    print(*board.get_field(), sep='\n')
    print(board.make_move(2, 1))
    print(board.make_move(2, 2))
    print(board.make_move(3, 1))
    print(board.make_move(2, 2))
    print(*board.get_field(), sep='\n')
