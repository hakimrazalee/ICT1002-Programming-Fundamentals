def add(x, y):
    x = int(x)
    y = int(y)

    return x + y


def subtraction(x, y):
    x = int(x)
    y = int(y)
    return x - y


def evenNum(x):
    evenList = []
    for numbers in x:

        if numbers % 2 == 0:
            evenList.append(numbers)
    evenNumLen = len(evenList)
    return evenNumLen


def maximum(x):
    return max(x)


def minimum(x):
    return min(x)


def absolute(x):
    return abs(x)


def sumTotal(x):
    sumOfTotal = 0
    for numbers in x:
        sumOfTotal += numbers
    return sumOfTotal


def clear(x):
    cleared = []
    for numbers in x:
        element = 0
        cleared.append(element)
    return cleared


# 'TEST'
# rint(add(10, 2))
# print(subtraction(10, 2))
#print(evenNum([12, 10, 11, 23, 25, 2]))
# print(maximum([12, 10, 11, 23, 25, 2]))
# print(minimum([12, 10, 11, 23, 25, 2]))
# print(abs(10000))
# print(sumTotal([2, 3, 4, 5, 6, 7]))
# print(clear([2, 3, 4, 5, 6, 7]))
