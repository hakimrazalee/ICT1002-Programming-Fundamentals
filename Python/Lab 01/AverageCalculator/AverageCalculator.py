import sys


def calculator(a, b, c):
    ave_value = (a + b + c) / 3
    print("Average:" + "%0.2f" % ave_value)
    return


try:

    calculator(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

except:

    print("Your input is invalid!")
