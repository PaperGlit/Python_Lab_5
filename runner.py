from BLL.classes.shapes.cube import Cube
from BLL.classes.shapes.pyramid import Pyramid
from BLL.classes.shapes.sphere import Sphere


for i in range(5, 10):
    cube = Cube(i)
    cube.move(2, -2, -2)
    print("Cycle: " + str(i))
    shape_2d = cube.to_2d(False)

    for j in shape_2d:
        print("".join(str(j)))

# for i in range(cube.size):
#     for j in range(cube.size):
#         print(" ".join(map(str, cube.shape[i][j])))
#     print()

# pyramid = Pyramid(5)
#
# for i in range(pyramid.size * 2 - 1):
#     for j in range(pyramid.size):
#         print(" ".join(map(str, pyramid.shape[i][j])))
#     print()

# sphere = Sphere(10)
#
# for i in range(sphere.size):
#     for j in range(sphere.size):
#         print(" ".join(map(str, sphere.shape[i][j])))
#     print()