from BLL.classes.shapes.shape import Shape


class Sphere(Shape):
    def create_shape(self):
        shape = self.create_array(self.size, self.size)
        center = (self.size + 1) // 2
        cycle = list(range(1, center + 1)) + list(range(center - (self.size % 2), 0, -1))
        j = 0
        for i in cycle:
            if i >= 1:
                shape[j] = self.create_circle(i)
            j += 1
        return shape

    def create_circle(self, diameter):
        result = [[" " for _ in range(self.size)] for _ in range(self.size)]
        result1 = [[" " for _ in range(diameter)] for _ in range(diameter)]
        radius = diameter / 2 - .5
        r = (radius + .25) ** 2 + 1
        for i in range(diameter):
            y = (i - radius) ** 2
            for j in range(diameter):
                x = (j - radius) ** 2
                if x + y <= r:
                    result1[i][j] = "*"
                else:
                    result1[i][j] = " "
        expand_start = (len(result) - len(result1)) // 2
        expand_end = self.size - expand_start if (len(result) - len(result1)) % 2 == 0 else self.size - expand_start - 1
        i1, j1 = 0, 0
        for i in range(expand_start, expand_end):
            for j in range(expand_start, expand_end):
                result[i][j] = result1[i1][j1]
                j1 += 1
            j1 = 0
            i1 += 1
        return result