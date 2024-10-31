from BLL.classes.shapes.shape import Shape
import numpy as np

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

    def to_2d(self):
        shape = self.shape
        height = self.size
        width = len(shape)
        result = [[" " for _ in range(width * 2 - 1)] for _ in range(height * 2 - 1)]
        midpoint = (width - 1) // 2
        char = "*"
        for offset in range(2):
            i1 = len(result) - 1 - offset
            for i in reversed(range(height)):
                j1 = offset
                for j in range(width):
                    if result[i1][j1] == " " and shape[midpoint][i][j] == "*":
                        result[i1][j1] = char
                    j1 += 1
                i1 -= 1
            char = "#"


        #
        # num = 1
        # offset = 0
        # char = "*"
        # for i in reversed(range(width)):
        #     for j in reversed(range(height)):
        #         j1 = offset
        #         for k in reversed(range(width)):
        #             result[i1][j1] = shape[j][i][k]
        #             j1 += 1
        #         i1 -= 1
        #     offset += 0
        #     i1 = len(result) - 1 - offset
        #     num += 1
        return result