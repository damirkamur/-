from PIL import Image, ImageDraw


class Drawer:
    def __init__(self, draw_map, cell_size):
        self.__draw_map = draw_map
        self.__cell_size = cell_size
        self.__colors = dict()

    def number(self):
        colors = [self.__draw_map[i][j] for i in range(len(self.__draw_map)) for j in range(len(self.__draw_map[0]))]
        return sorted(list(set(colors)))

    def set_color(self, number, color):
        self.__colors[number] = color

    def set_sell_size(self, cell_size):
        self.__cell_size = cell_size

    def size(self):
        N = len(self.__draw_map)
        M = len(self.__draw_map[0])
        return self.__cell_size * M, self.__cell_size * N

    def draw(self):
        image = Image.new('RGB', self.size(), 'white')
        draw = ImageDraw.Draw(image)
        N = len(self.__draw_map)
        M = len(self.__draw_map[0])
        for i in range(N):
            for j in range(M):
                x1, x2 = j * self.__cell_size, (j + 1) * self.__cell_size
                y1, y2 = i * self.__cell_size, (i + 1) * self.__cell_size
                draw.rectangle([x1, y1, x2, y2], fill=self.__colors.get(self.__draw_map[i][j], 'black'))
        return image


if __name__ == '__main__':
    drawer = Drawer([[1, 2, 3], [4, 5, 6], [7, 8, 9], [3, 2, 1]], 40)
    drawer.set_color(1, 'black')
    drawer.set_color(2, 'red')
    drawer.set_color(3, 'orange')
    drawer.set_color(4, 'yellow')
    drawer.set_color(5, 'green')
    drawer.set_color(6, 'lightblue')
    drawer.set_color(7, 'blue')
    drawer.set_color(8, 'violet')
    drawer.set_color(9, 'white')
    image = drawer.draw()
    image.show()
