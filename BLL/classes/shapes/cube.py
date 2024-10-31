from BLL.classes.shapes.shape import Shape


class Cube(Shape):
    def create_shape(self):
        shape = self.create_array(self.size, self.size)
        for i in range(self.size):
            for j in range(self.size):
                for k in range(self.size):
                    shape[i][j][k] = "*"
        return shape

    def to_2d(self, debug = False):
        shape = self.shape
        size = self.size
        parts = 3 * (size // 5)
        parts = 1 if parts == 0 else parts
        grid_size = size + parts
        result = [[" " for _ in range(grid_size)] for _ in range(grid_size)]
        i1 = len(result) - 1
        num = 1
        offset = 0
        char = "*"
        for i in range(0, size, round(size / parts)):
            for j in reversed(range(size)):
                j1 = offset
                for k in reversed(range(size)):
                    if result[i1][j1] == " " and shape[i][j][k] == "*" and not debug:
                        result[i1][j1] = char
                    elif result[i1][j1] == " " and shape[i][j][k] == "*" and debug:
                        result[i1][j1] = num
                    j1 += 1
                i1 -= 1
            offset += 1
            i1 = len(result) - 1 - offset
            num += 1
            char = "#"
        return result