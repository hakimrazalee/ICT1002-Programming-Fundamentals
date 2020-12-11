import sys


def letter_count(str):
    dict = {}
    for elements in str:
        dict[elements] = elements.count(elements)
    return dict


def double_count(str1, str2):
    dict = {}
    differentWords = []
    wordcountlist = []

    for elements in str1, str2:
        differentWords.append(elements)

    for x in differentWords:
        for i in x:
            wordcountlist.append(i)

    for e in wordcountlist:
        dict[e] = wordcountlist.count(e)

    return dict


def various_count(*str):
    dict = {}
    differentWords = []
    wordcountlist = []

    for elements in str:
        differentWords.append(elements)

    for x in differentWords:
        for i in x:
            wordcountlist.append(i)

    for e in wordcountlist:
        dict[e] = wordcountlist.count(e)

    return dict


def countingLetters(*str):
    dict = {}
    differentWords = []
    wordcountlist = []

    for elements in str:
        differentWords.append(elements)

    for x in differentWords:
        for i in x:
            wordcountlist.append(i)

    for e in wordcountlist:
        dict[e] = wordcountlist.count(e)

    sorted_total = (sorted(dict.items(), reverse=True))
    for item in sorted_total:
        print('%s:%d' % (item[0], item[1]), end=" ")


def listToString(s):
    # initialize an empty string
    str1 = ""

    # traverse in the string
    for ele in s:
        str1 += ele

        # return string
    return str1


userinput = sys.argv[1].split(",")
nocommas = listToString(userinput)
countingLetters(nocommas)
