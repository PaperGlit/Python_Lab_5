from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, length):
        self.size = length
        self.shape = self.create_shape()
        self.pos_x = 0
        self.pos_y = 0

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