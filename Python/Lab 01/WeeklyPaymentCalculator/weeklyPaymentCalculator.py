import sys


def calculateSalary(whours, nrate, orate):
    if 168 > whours < 41:
        # total 168 hours in a week
        n_salary = whours * nrate
        o_salary = orate * 0
        salary = n_salary + o_salary
        print("Normal Salary:%0.2f" % n_salary + ", Extra Salary:%0.2f," % o_salary + " Total Salary:%0.2f" % salary)

    elif 168 > whours > 40:
        o_salary = (whours - 40) * orate
        n_salary = (40 * nrate)
        salary = o_salary + n_salary
        print("Normal Salary:%0.2f" % n_salary + ", Extra Salary:%0.2f," % o_salary + " Total Salary:%0.2f" % salary)

    else:
        print("Your input is invalid!")

    return


try:

    calculateSalary(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))

except:

    print("Your input is invalid!")
