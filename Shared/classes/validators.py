from BLL.classes.cube import Cube
from BLL.classes.pyramid import Pyramid
from BLL.classes.sphere import Sphere


class Validators:
    @staticmethod
    def validate_value(value, min_value, max_value):
        try:
            result = int(value)
            if min_value > result > max_value:
                raise ValueError("Incorrect value, please try again.")
        except ValueError:
            raise ValueError("Incorrect value, please try again.")
        return result

    @staticmethod
    def create_shape(shape, size):
        match shape:
            case 1:
                return Cube(size)
            case 2:
                return Pyramid(size)
            case 3:
                return Sphere(size)
            case _:
                raise ValueError("Incorrect value, please try again.")

    @staticmethod
    def validate_color(value, console):
        match value:
            case "1":
                console.shape.color = "\033[31m"
            case "2":
                console.shape.color = "\033[32m"
            case "3":
                console.shape.color = "\033[33m"
            case "4":
                console.shape.color = "\033[34m"
            case "5":
                console.shape.color = "\033[35m"
            case "6":
                console.shape.color = "\033[36m"
            case "7":
                console.shape.color = "\033[37m"
            case "8":
                console.shape.color = "random"
            case "0":
                console.shape.color = "\033[39m"
            case _:
                raise ValueError("Incorrect value, please try again.")

    @staticmethod
    def main_prompt(value, console):
        match value:
            case "1":
                console.create_shape()
            case "2":
                console.change_size()
            case "3":
                console.move_shape()
            case "4":
                console.change_color()
            case "5":
                print(console.shape)
            case _:
                raise ValueError("Incorrect value, please try again.")