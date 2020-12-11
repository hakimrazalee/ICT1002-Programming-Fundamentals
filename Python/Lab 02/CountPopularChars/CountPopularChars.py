import sys
from collections import Counter


def CountPopularChars(n):
    result = []
    lowern = n.lower()
    sorted_string = sorted(lowern)
    counted_list = Counter(sorted_string)
    topfive = counted_list.most_common(5)
    for char in topfive:
        z = str("%s:%d" % char)
        result += [z]

    print(*result, sep=",")
    return


try:

    CountPopularChars(sys.argv[1])

except:
    print("Your input is invalid!")
