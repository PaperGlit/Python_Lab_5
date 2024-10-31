from BLL.classes.shapes.shape import Shape


class Pyramid(Shape):
    def create_shape(self):
        width = self.size * 2 - 1
        shape = self.create_array(width, self.size)
        start = self.size
        end = self.size
        for i in range(self.size):
            for j in range(start - 1, end):
                for k in range(start - 1, end):
                    shape[j][i][k] = "*"
            start -= 1
            end += 1
        return shape

    def to_2d(self, debug = False):
        shape = self.shape
        height = self.size
        width = len(shape)
        result = [[" " for _ in range(width + 1)] for _ in range(height + 1)]
        midpoint = (width - 1) // 2
        char = "*"
        num = 1
        for offset in range(2):
            i1 = len(result) - 1 - offset
            for i in reversed(range(height)):
                j1 = offset
                for j in range(width):
                    if result[i1][j1] == " " and shape[midpoint][i][j] == "*" and not debug:
                        result[i1][j1] = char
                    elif result[i1][j1] == " " and shape[midpoint][i][j] == "*" and debug:
                        result[i1][j1] = num
                    j1 += 1
                i1 -= 1
            char = "#"
            num += 1
        return result