import sys


def patternSearching(str1, str2):
    pattern = []
    #find the length of the str
    for charPosition in range(len(str1)):
        # check if match, starts from every position not just the main starting point
        if str1.startswith(str2, charPosition):
            pattern.append(charPosition)
    count = len(pattern)
    return print("Pattern appears " + str(count) + " time!")


patternSearching(str(sys.argv[1]), str(sys.argv[2]))
