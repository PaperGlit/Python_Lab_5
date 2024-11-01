from BLL.classes.shapes.shape import Shape
import math


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
        z_size = len(shape)
        x_offset = abs(self.pos_x) if self.pos_x < 0 else 0
        z_offset = abs(self.pos_z) if self.pos_z < 0 else 0
        z_size_normalized = z_size - abs(self.pos_z)
        parts = 3 * (z_size_normalized // 5) if z_size_normalized > 4 else 1
        increment = z_size_normalized // parts
        grid_size = math.ceil(z_size_normalized / increment) - 1
        result = [[" " for _ in range(len(shape[0][0]) + grid_size + z_offset - x_offset)] for _ in range(len(shape[0]) + grid_size + z_offset)]
        num = z_offset + 1
        offset = z_offset
        char = "*"
        start_pos = offset
        end_pos = z_size_normalized + start_pos
        for i in range(start_pos, end_pos, increment):
            i1 = len(result) - 1 - offset
            for j in reversed(range(len(shape[i]))):
                j1 = offset + self.pos_x
                for k in range(len(shape[i][j]) - abs(self.pos_x)):
                    if result[i1][j1] == " " and shape[i][j][k] == "*" and not debug:
                        result[i1][j1] = char
                    elif result[i1][j1] == " " and shape[i][j][k] == "*" and debug:
                        result[i1][j1] = num
                    j1 += 1
                i1 -= 1
            offset += 1
            num += 1
            char = "#"
        return result