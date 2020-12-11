import myMath
import sys


def calculator(x):
    maxMinusMin = myMath.subtraction(myMath.maximum(x), myMath.minimum(x))
    sumMaxMin = myMath.add(myMath.maximum(x), myMath.minimum(x))

    intList = [int(i) for i in x]

    sumOfList = myMath.sumTotal(intList)
    evenNos = myMath.evenNum(intList)

    checkSmallest = myMath.minimum(intList)

    if checkSmallest < 5:
        clearedList = myMath.clear(intList)

    else:
        clearedList = intList

    print(
        "The difference is:%d" % maxMinusMin + " The summation is:%d" % sumMaxMin + " The summation of all input is:%d" % sumOfList + " The number of even numbers is:%d" % evenNos + " The values in the list are:",
        end=" ")
    print(clearedList)


# userInput = list(map(int, input().split(",")))
# print(userInput)

try:

    userinput = str(sys.argv[1])

    calculator(list(map(int, userinput.split(","))))

except:
    print("Your input is invalid!.")
