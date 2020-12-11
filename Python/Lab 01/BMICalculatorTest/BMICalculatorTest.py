import sys


def BMI(u, h, w):
    if u == 'metric':
        bmi = w / (h * h)

        if bmi > 40:
            print("%0.2f\tObese Class III" % bmi)

        elif 40 >= bmi >= 35:
            print("%0.2f\tObese Class II" % bmi)

        elif 35 >= bmi >= 30:
            print("%0.2f\tObese Class I" % bmi)

        elif 30 >= bmi >= 25:
            print("%0.2f\tOverweight" % bmi)

        elif 25 >= bmi >= 18.5:
            print("%0.2f\tNormal" % bmi)

        elif 18.5 >= bmi >= 17:
            print("%0.2f\tMild Thinness" % bmi)

        elif 17 >= bmi >= 16:
            print("%0.2f\tModerate Thinness" % bmi)

        elif bmi < 16:
            print("%0.2f\tSevere Thinness" % bmi)

        else:
            print("Your input is invalid")

    elif u == 'imperial':
        bmi = (703 * w) / (h * h)

        if bmi > 40:
            print("%0.2f\tObese Class III" % bmi)

        elif 40 >= bmi >= 35:
            print("%0.2f\tObese Class II" % bmi)

        elif 35 >= bmi >= 30:
            print("%0.2f\tObese Class I" % bmi)

        elif 30 >= bmi >= 25:
            print("%0.2f\tOverweight" % bmi)

        elif 25 >= bmi >= 18.5:
            print("%0.2f\tNormal" % bmi)

        elif 18.5 >= bmi >= 17:
            print("%0.2f\tMild Thinness" % bmi)

        elif 17 >= bmi >= 16:
            print("%0.2f\tModerate Thinness" % bmi)

        elif bmi < 16:
            print("%0.2f\tSevere Thinness" % bmi)

        else:
            print("Your input is invalid")
    else:
        print("Your input is invalid!")

    return


try:

    BMI(str(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3]))

except:
    print("Your input is invalid!")
