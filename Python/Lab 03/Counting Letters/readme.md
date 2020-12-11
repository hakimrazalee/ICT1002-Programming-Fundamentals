# Counting Letters

In this task, you are going to develop one letter game to count the number of letters for given strings.

Step1: Write one function letter_count(str) that take in one word and returns a dictionary with the
frequency counts of the various letters. Upper and lower-case characters are considered to be different
characters.

Sample execution:
>>letter_count(‘This’)

{ ‘h’:1, ‘T’:1, ‘i’:1, ‘s’:1}

>>letter_count(‘Thisisit’)

{‘h’:1, ‘T’:1, ‘i’:3, ‘s’:2, ‘t’:1}

Step 2: write one function double_count(str1,str2) that takes in two words and returns a dictionary with
the frequency counts of the various letters. Upper and lower-case characters are considered to be different
characters.

Sample execution:
>> double_count(‘This’, ‘isit’)

{‘h’:1, ‘T’:1, ‘i’:3, ‘s’:2, ‘t’:1}

**HINT: In Python, using “def func(\*str): list1=str”, list1 is able to obtain any number of
arguments and stores it as a list. You can further get each element from the list and count each
word independently. You can implement another function to merge two dictionaries.**

Step 4: Write one program to allow users to input different number of words and output each
character’s frequency.

Some of codes read as follows. Please print your results in the characters’ ASCII descending order
according to this format.

>>     for item in sorted_total:

>>          print '%s:%d' % (item[0], item[1]),