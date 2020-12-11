import sys


def double(x):
    return 2 * x


def square(x):
    return x ** 2


def cube(x):
    return x ** 3


def DoTwice(x, y):
    result = []
    if y == 1:  # Double Operation
        result.append(double(x))
        return list(map(lambda g: double(g), result))[0]

    elif y == 2:  # Square Operation
        result.append(square(x))
        return list(map(lambda g: square(g), result))[0]

    elif y == 3:  # Cube Operation
        result.append(cube(x))
        return list(map(lambda g: cube(g), result))[0]

    else:
        return 'It cannot be supported!'


print(DoTwice(int(sys.argv[1]), int(sys.argv[2])))
