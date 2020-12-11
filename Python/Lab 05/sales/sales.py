import sys
from functools import reduce


def scale(z, x):
    return list(map(lambda i: i * x, z))


def sort(z):
    return list(map(lambda x: int(x), list(sorted(list(map(lambda x: str(x), z)), key=lambda x: x[:0:-1]))))


def goodSales(x):
    ave = reduce(lambda b, y: b + y, x) / len(x)
    return list(filter(lambda h: h > ave, x))


def sales(x, y):
    scaled = scale(x, y)
    isSorted = sort(x)
    goodNums = goodSales(x)
    return 'The scaled number is: ' + str(scaled) + ' The sorted sales numbers are: ' + str(isSorted) + ' The good sales numbers are:' + str(goodNums)


# print(scale([10, 20, 30, 40], 2))
# print(sort([55, 70, 61, 34, 72, 59]))
# print(goodSales([3, 2, 8, 6, 7]))
try:
    #x = [10,20,30] HI HAZWAN IF YOU WANNA TRY CHANGE THE VALUES MANUALLY HERE AND COMMENT OUT THE X AND Y
    #y = 2
    x = list(map(int, sys.argv[1].split(',')))
    y = int(sys.argv[2])
    print(sales(x, y))
except:
    print("Your input is invalid.")
