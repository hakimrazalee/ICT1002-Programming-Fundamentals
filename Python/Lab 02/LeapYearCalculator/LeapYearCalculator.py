import sys


def LeapYearCalculator(y1, y2):
    yearsgiven = range(y1, y2 + 1)
    yearlist = []
    for year in yearsgiven:

        if year % 4 == 0:
            if year % 100 == 0:
                yearlist += [year]
            elif year % 400 == 0:
                yearlist += [year]
            else:
                yearlist += [year]
    count = str(len(yearlist))
    print("The number of Leap Years is " + count + ", the Leap Years are ", end="")
    print(*yearlist, sep=", ")
    return


try:

    LeapYearCalculator(int(sys.argv[1]), int(sys.argv[2]))

except:
    print("Your input is invalid!")
