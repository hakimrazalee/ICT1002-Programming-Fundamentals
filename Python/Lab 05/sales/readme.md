# Developing Sales

As a programmer, you are given a list of sales numbers from different sales departments. Based on this
list of numbers, you are request to develop one program to assistant your sales manager to analyse and get
different representations of the data. The task you have to perform is listed below:
1) Given a list of sales numbers, you need to write functions scale(list1, x) to return another list of
scaled numbers, where list1 is the list of sales numbers and x is the scale factor. The scaled
number can be calculated by using the input number multiplied by the scale factor. Below are
some sample executions of the function:
2) Given a list of sales number, you are required to write one function sort(list1) to return one list of
sorted sales numbers. Different to the normal sorting, the sales manager request you to sort the
number based on their last digit. Below are some sample executions of the function:
3) Given a list of sales numbers, you re required to write one function to output all the good
sales. The sales number is considered to be good if it is above the average of the total
sales numbers.
4) Develop one program to allow users to input the sequence of the sales number and the
scale factor. Then call all the functions to show use the scaled data, sorting result and
good sales. Below are the sample executions of the program:

**Remark:** for functions 1, 2 and 3, you can optimize the function body with at most 2 line codes by
using filter, map, reduce, sorted and lambda expression. See how short your code can be.)

**Running example:** (Your output should be in ONE line)

**C:\ICT1002\Lab5\Sales> python sales.py 10,20,30,40,50,60 2**

The scaled number is: [20, 40, 60, 80, 100, 120] The sorted sales
numbers are: [10, 20, 30, 40, 50, 60] The good sales numbers are:
[40, 50, 60]