from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, size):
        self.size = size
        self.shape = self.create_shape()
        self.pos_x = 0
        self.pos_y = 0
        self.pos_z = 0

    @abstractmethod
    def create_shape(self):
        pass

    @abstractmethod
    def to_2d(self):
        pass

    @staticmethod
    def create_array(width, height):
        shape = [[[" " for _ in range(width)] for _ in range(height)] for _ in range(width)]
        return shape

    def change_size(self, new_size):
        self.size = new_size
        self.shape = self.create_shape()

    def move(self, x = 0, y = 0, z = 0):
        self.pos_x += x
        self.pos_y += y
        self.pos_z += z
        shape = self.create_shape()
        size_x = len(shape[0][0])
        size_y = len(shape[0])
        size_z = len(shape)
        if self.pos_z != 0:
            for _ in range(abs(self.pos_z)):
                shape.append([[[" " for _ in range(size_x)] for _ in range(size_y)] for _ in range(size_z)])
            if self.pos_z < 0:
                shape = shape[self.pos_z:] + shape[:self.pos_z]
            size_z = len(shape)
        if self.pos_y != 0:
            for i in range(size_z):
                for _ in range(abs(self.pos_y)):
                    shape[i].append([[" " for _ in range(size_x)] for _ in range(abs(size_y))])
            if self.pos_y < 0:
                for i in range(size_z):
                    shape[i] = shape[i][self.pos_y:] + shape[i][:self.pos_y]
            size_y = len(shape[0])
        if self.pos_x != 0:
            for i in range(size_z):
                for j in range(size_y):
                    for _ in range(abs(self.pos_x)):
                        shape[i][j].append([" " for _ in range(size_x)])
            if self.pos_x < 0:
                for i in range(size_z):
                    for j in range(size_y):
                        shape[i][j] = shape[i][j][self.pos_x:] + shape[i][j][:self.pos_x]
        self.shape = shape