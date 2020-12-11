import sys


def EvenOddCalculator(n):
    # initiator//before calculation
    raw_input_list = n.split(",")  # in string
    new_input_list = []  # in int
    odd_list = []
    even_list = []
    sumofeven = 0
    sumofodd = 0
    for num in raw_input_list:
        new_input_list += [int(num)]  # Converting all into integer form

    # EvenOddSummation calculator
    for num in new_input_list:
        if num % 2 == 0:
            # number is even // += adds to the var and also updates it
            even_list += [num]
            sumofeven += num
        else:
            # number is odd
            odd_list += [num]
            sumofodd += num
    evenlen = len(even_list)
    oddlen = len(odd_list)

    # Difference between biggest and smallest calculator
    sortedlist = sorted(new_input_list)
    # print(sortedlist[0])  # first one
    # print(sortedlist[-1])  # last?
    difference = sortedlist[-1] - sortedlist[0]

    # centered Average Calculator
    centavelist = sortedlist.copy()

    del centavelist[-1]
    del centavelist[0]
    centdivlen = len(centavelist)
    totalcent = 0
    for newlistnumber in centavelist:
        totalcent += newlistnumber
    centave = totalcent / centdivlen

    print("The sum of all even numbers is " + str(sumofeven) + ", the sum of all odd numbers is " + str(sumofodd) + ",",
          end="")
    print(" the difference between the biggest and smallest number is " + str(
        difference) + ", the total number of even numbers is " + str(
        evenlen) + ", the total number of odd numbers is " + str(
        oddlen) + ", the centered average is " + str(int(centave)))
    return


try:

    EvenOddCalculator(str(sys.argv[1]))


except:
    print("Please enter valid integers.")
