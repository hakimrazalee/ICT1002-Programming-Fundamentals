import sys


def sum_recursive(x):
    if x == 0:
        return 0
    else:
        return sum_recursive(x - 1) + x


def sum_iterative(x):
    numSum = 0
    for i in range(x):
        numSum += i + 1
    return numSum


y = sum_iterative(int(sys.argv[1]))
z = sum_recursive(int(sys.argv[1]))
print("The SUM value calculated by recursive is ", end="")
print(str(z), end="")
print(" and by iterative is ", end="")
print(str(y), end="")
print(".")

#print("The SUM value calculated by recursive is " + str(z) + " and by iterative is " + str(y) + ".")
