import sys


def digit_recursion(x):
    if x < 1:
        return 0
    else:
        return 1 + digit_recursion(x / 10)


def digit_iterative(x):
    digits = 1
    while x / 10 >= 1:
        x = x / 10
        digits += 1
    else:
        return digits


i = digit_iterative(int(sys.argv[1]))
r = digit_recursion(int(sys.argv[1]))

print("The number of digit(s) calculated by recursive is " + str(r) + " and by iterative is " + str(i) + ".")