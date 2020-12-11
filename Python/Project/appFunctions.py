# ---                Packages required for program               ---#
import pandas as pd  # Package requiring PIP
import matplotlib.pyplot as plt  # Package requiring PIP
import numpy as np  # Package requiring PIP
import matplotlib.image as mpimg  # Package requiring PIP
import matplotlib.cm  # Package requiring PIP
import datetime as dt  # Built in Package
import math  # Built in Package
import var  # Custom Package

# ---                    End of Packages List                    ---#
'''
Here are the list for the functions of this document:
Non Visuals:
    1) maxAge(size = 5000)
    2) minAge(size = 5000)
    3) countNAVals(data), Required to pass a col as arg

Visuals:
    1)natDaysLineGraph()
    2)cfmCaseWeekBarChart()
    3)facilitiesGeogMap()
    4)facilitiesPieChart()
    5)srcLineGraph()
        i) srcAxes()            - Supplementary
        ii) srcLocalCounter()   - Supplementary
        iii) srcImportCounter() - Supplementary
    6)ageBarGraph()
        i) ageAxes()            - Supplementary
'''


# ---                Start of Non Visual Functions               ---#
def maxAge(size=5000, data=var.getAge()):
    """
    This function allows user to find the HIGHEST Aged patient.
    The default range to search is from CaseID (1) to caseID (5000).
    Users are able to define the size as desired to reduce the range.
    The reduced range will be from CaseID (1) to case ID (userSize + 1).
    """
    phList = []  # Place holder list to append ages
    for i in range(0, size, 1):
        phList.append(data[i])
    return max(phList)


def minAge(size=5000, data=var.getAge()):
    """
    This function allows user to find the LOWEST Aged patient.
    The default range to search is from CaseID (1) to caseID (5000).
    Users are able to define the size as desired to reduce the range.
    The reduced range will be from CaseID (1) to case ID (userSize + 1).
    """
    phList = []
    for i in range(0, size, 1):
        phList.append(data[i])
    return min(phList)


def countNAVals(data):
    """
    This function allows user to find the number of records unavailable due to lack of information.
    Function compares type and records with Nan (type = float) are considered unavailable.
    Users can check for the count by passing their desired columnsas the argument.
    This function is unable to check for placesVisited.
    """
    counter = 0
    dataToCheck = data.name
    if dataToCheck == "caseID":
        counter = 0  # All cases have a case ID
    elif dataToCheck == "Age":  # Only field with float type
        for i in range(0, len(data), 1):  # Iterates through data (ages)
            if math.isnan(data[i]) == True:  # Check if value == nan
                counter += 1  # Counts each values of nan
    elif dataToCheck == "Confirmed Date" or "Hospital" or "Discharged Date" or "Gender" or "Nationality" or "Transmission Type" or "Date of Death":  # Fields with str type
        for i in range(0, len(data), 1):  # Iterates through data with str type
            if type(data[i]) != str:  # Check if value type not equal to str (nan type = float)
                counter += 1  # Counts each values of nan
    return counter


# ---                End of Non Visual Functions               ---#


# ---                Start of Visual Functions                 ---#

# ---------- natDaysLineGraph()            Visual #1 - Plots a Line Graph to show (Singaporeans & PRS) & Foreigners over the days               ----------#
def natDaysLineGraph():
    natlist = []
    for i in var.getNat():
        natlist.append(str(i))

    datelist = []
    for i in var.getDateCfm():
        datelist.append(str(i))

    sgdate = {}
    fordate = {}
    a = 0
    countsg = 1
    countfor = 1

    for i in datelist:
        sgdate[i] = 0
        fordate[i] = 0

    while a < 5000:
        if natlist[a] == "Singapore Citizen" or natlist[a] == "Singapore Permanent Resident":
            sgdate[datelist[a]] += 1

        elif natlist[a] != "Singapore Citizen" and natlist[a] != "Singapore Permanent Resident":
            fordate[datelist[a]] += 1

        a += 1

    sgX = list(sgdate.keys())
    sgY = list(sgdate.values())

    foreignX = list(fordate.keys())
    foreignY = list(fordate.values())

    fig, ax = plt.subplots(1)
    ax.plot(sgX, sgY, label="Confirmed Singaporean and PR Cases")
    ax.plot(foreignX, foreignY, label="Confirmed Foreigner Cases")
    plt.xlabel("\nConfirmed cases over the days", size=10)
    plt.ylabel("Number of cases per day\n", size=10)
    plt.title("Trend of Singaporean and PR / Foreigner confirmed cases over the days\n\n23 Jan 2020 to 17 April 2020",
              size=11)
    ax.xaxis.set_visible(False)
    plt.xlim(1, 80)
    ax.legend()
    plt.grid(True)
    plt.show()


# ----------            End of Codes for Visual #1                 ------------------------------------------------------------------#

# ---------- cfmCaseWeekBarChart()            Visual #2 - Plots a Bar Chart showing the count of confirmed patients over 7 days, over the 13 weeks                ----------#
def cfmCaseWeekBarChart():
    """
    This function plots a Bar Graph showing the number of cases over the weeks.
    Each bar represents the count of confirmed cases for a period of 7 days less the starting and ending week.
    """
    listDateCfm = []
    for i in var.getDateCfm():
        listDateCfm.append(str(i))

    dictDateCfm = {}
    for i in listDateCfm:
        dictDateCfm[i] = listDateCfm.count(i)

    countj19toj25 = 0
    countj26tof1 = 0

    countf2tof8 = 0
    countf9tof15 = 0
    countf16tof22 = 0
    countf23tof29 = 0

    countm1tom7 = 0
    countm8tom14 = 0
    countm15tom21 = 0
    countm22tom28 = 0
    countm29toa4 = 0

    counta5toa11 = 0
    counta12toa18 = 0

    format1 = '%d/%m/%Y'

    for i in listDateCfm:
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 1, 19).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 1, 25).date():
            countj19toj25 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 1, 26).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 2, 1).date():
            countj26tof1 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 2, 2).date() and dt.datetime.strptime(i,
                                                                                                              format1).date() <= dt.datetime(
                2020, 2, 8).date():
            countf2tof8 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 2, 9).date() and dt.datetime.strptime(i,
                                                                                                              format1).date() <= dt.datetime(
                2020, 2, 15).date():
            countf9tof15 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 2, 16).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 2, 22).date():
            countf16tof22 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 2, 23).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 2, 29).date():
            countf23tof29 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 3, 1).date() and dt.datetime.strptime(i,
                                                                                                              format1).date() <= dt.datetime(
                2020, 3, 7).date():
            countm1tom7 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 3, 8).date() and dt.datetime.strptime(i,
                                                                                                              format1).date() <= dt.datetime(
                2020, 3, 14).date():
            countm8tom14 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 3, 15).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 3, 21).date():
            countm15tom21 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 3, 22).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 3, 28).date():
            countm22tom28 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 3, 29).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 4, 4).date():
            countm29toa4 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 4, 5).date() and dt.datetime.strptime(i,
                                                                                                              format1).date() <= dt.datetime(
                2020, 4, 11).date():
            counta5toa11 += 1
        if dt.datetime.strptime(i, format1).date() >= dt.datetime(2020, 4, 12).date() and dt.datetime.strptime(i,
                                                                                                               format1).date() <= dt.datetime(
                2020, 4, 18).date():
            counta12toa18 += 1

    dictWeeks = {}
    dictWeeks["Week 04\nJan 19 -\nJan 25"] = countj19toj25
    dictWeeks["Week 05\nJan 26 -\nFeb 01"] = countj26tof1
    dictWeeks["Week 06\nFeb 02 -\nFeb 08"] = countf2tof8
    dictWeeks["Week 07\nFeb 09 -\nFeb 15"] = countf9tof15
    dictWeeks["Week 08\nFeb 16 -\nFeb 22"] = countf16tof22
    dictWeeks["Week 09\nFeb 23 -\nFeb 29"] = countf23tof29
    dictWeeks["Week 10\nMar 01 -\nMar 07"] = countm1tom7
    dictWeeks["Week 11\nMar 08 -\nMar 14"] = countm8tom14
    dictWeeks["Week 12\nMar 15 -\nMar 21"] = countm15tom21
    dictWeeks["Week 13\nMar 22 -\nMar 28"] = countm22tom28
    dictWeeks["Week 14\nMar 29 -\nApr 04"] = countm29toa4
    dictWeeks["Week 15\nApr 05 -\nApr 11"] = counta5toa11
    dictWeeks["Week 16\nApr 12 -\nApr 18"] = counta12toa18

    fig, ax = plt.subplots()
    plt.bar(range(len(dictWeeks)), list(dictWeeks.values()), width=0.5, color='#444444')
    plt.xticks(range(len(dictWeeks)), list(dictWeeks.keys()), size=7)

    for i, v in enumerate(list(dictWeeks.values())):
        ax.text(i, v + 50, str(v), fontweight='bold', ha='center', va='center')

    plt.xlabel("Weeks", size=10)
    plt.ylabel("Number of confirmed cases\n", size=10)
    plt.title("Trend of confirmed cases over the weeks\n", size=11)
    plt.grid(True)
    plt.show()


# ----------            End of Codes for Visual #2                 ------------------------------------------------------------------#

# ---------- facilitiesGeogMap()            Visual #3 - Overlays Singapore Geographical Map with Statistic of Number of patients in facilities                ----------#

def facilitiesGeogMap():
    '''
    This function plots bubbles over the geographical map of Singapore based on the Longitude and Latitude.
    Each bubble's size corresponds to the number of patients in that facility.
    '''
    singapore_img = mpimg.imread('sg.jpg')
    # plot the data

    list1 = []
    list2 = []
    list3 = []
    dict1 = {}
    dict2 = {}
    dict3 = {}
    for i in var.getHospitals():
        if i != 0 and i != 'MEN':
            list1.append(i)

    for i in list1:

        if i not in dict1:
            dict1[i] = list1.count(i)

    for i in var.getLat():
        list2.append(i)
    for i in list2:
        if i not in dict2:
            dict2[i] = list2.count(i)

    for i in var.getLong():
        list3.append(i)
    for i in list3:
        if i not in dict2:
            dict3[i] = list3.count(i)
    mylist = dict.fromkeys(list2)
    mylist1 = dict.fromkeys(list3)

    fig, ax = plt.subplots()
    ax.scatter(list(mylist1.keys()), list(mylist.keys()))

    for i, txt in enumerate(list(dict1.values())):
        ax.annotate(txt, (list(mylist1.keys())[i], list(mylist.keys())[i] + 0.005), fontsize=7, va="center",
                    ha="center")

    for i, txt in enumerate(list(dict1.keys())):
        ax.annotate(str(txt)[0:15], (list(mylist1.keys())[i], list(mylist.keys())[i] + 0.0010), fontsize=5, va="center",
                    ha="right")

    plt.title('Allocations of Covid Patients in Singapore Hospitals')
    # use our map with it's bounding coordinates
    plt.imshow(singapore_img, extent=[103.5, 104, 1.15, 1.50], alpha=0.5)
    # add axis labels
    plt.ylabel("Latitude", fontsize=10)
    plt.xlabel("Longitude", fontsize=10)
    # set the min/max axis values - these must be the same as above
    plt.ylim(1.15, 1.50)
    plt.xlim(103.5, 104)
    plt.show()


# ----------            End of Codes for Visual #3                 ------------------------------------------------------------------#

# ---------- facilitiesPieChart()            Visual #4 - Plots a Pie Chart for showing distribution of facilities used to isolate patients                ----------#

def facilitiesPieChart():
    '''
    This function plots a Pie Chart displaying the various Facilities used to isolate COVID patients as well as its distribution.
    '''
    dict1 = {}
    list1 = []
    for i in var.getHospitals():
        if i != 0 and i != 'MEN':
            list1.append(i)

    for i in list1:
        if i not in dict1:
            dict1[i] = list1.count(i)

    fig = plt.figure();
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('equal')
    plt.title("Percentage of the allocation of covid patients in Singapore")
    ax.pie(list(dict1.values()), labels=list(dict1.keys()), autopct='%1.2f%%')
    plt.show()


# ----------            End of Codes for Visual #4                 ------------------------------------------------------------------#


# ---------- srcLineGraph()            Visual #5 - Plots a Line Graph for showing trend of Local/Imported cases over Weeks                ----------#
def srcAxes(src=var.getTypeTrans(), dateList=var.getDateCfm()):
    '''
    This function returns 2 values for populating the Line Graph.
    The first return value can be accessed by the index [0].
    The first return value can be accessed by the index [1].
    '''
    # List of dates to check, from week 1 (First Confirmed case) to week 13 (Date confirmed for 5000th patient)
    listCheckWeek1 = ["23/1/2020", "24/1/2020", "25/1/2020"]
    listCheckWeek2 = ["26/1/2020", "27/1/2020", "28/1/2020", "29/1/2020", "30/1/2020", "31/1/2020", "1/2/2020"]
    listCheckWeek3 = ["2/2/2020", "3/2/2020", "4/2/2020", "5/2/2020", "6/2/2020", "7/2/2020", "8/2/2020"]
    listCheckWeek4 = ["9/2/2020", "10/2/2020", "11/2/2020", "12/2/2020", "13/2/2020", "14/2/2020", "15/2/2020"]
    listCheckWeek5 = ["16/2/2020", "17/2/2020", "18/2/2020", "19/2/2020", "20/2/2020", "21/2/2020", "22/2/2020"]
    listCheckWeek6 = ["23/2/2020", "24/2/2020", "25/2/2020", "26/2/2020", "27/2/2020", "28/2/2020", "29/2/2020"]
    listCheckWeek7 = ["1/3/2020", "2/3/2020", "3/3/2020", "4/3/2020", "5/3/2020", "6/3/2020", "7/3/2020"]
    listCheckWeek8 = ["8/3/2020", "9/3/2020", "10/3/2020", "11/3/2020", "12/3/2020", "13/3/2020", "14/3/2020"]
    listCheckWeek9 = ["15/3/2020", "16/3/2020", "17/3/2020", "18/3/2020", "19/3/2020", "20/3/2020", "21/3/2020"]
    listCheckWeek10 = ["22/3/2020", "23/3/2020", "24/3/2020", "25/3/2020", "26/3/2020", "27/3/2020", "28/3/2020"]
    listCheckWeek11 = ["29/3/2020", "30/3/2020", "31/3/2020", "1/4/2020", "2/4/2020", "3/4/2020", "4/4/2020"]
    listCheckWeek12 = ["5/4/2020", "6/4/2020", "7/4/2020", "8/4/2020", "9/4/2020", "10/4/2020", "11/4/2020"]
    listCheckWeek13 = ["12/4/2020", "13/4/2020", "14/4/2020", "15/4/2020", "16/4/2020", "17/4/2020"]
    # Place Holder Lists
    srcWeek1 = []
    srcWeek2 = []
    srcWeek3 = []
    srcWeek4 = []
    srcWeek5 = []
    srcWeek6 = []
    srcWeek7 = []
    srcWeek8 = []
    srcWeek9 = []
    srcWeek10 = []
    srcWeek11 = []
    srcWeek12 = []
    srcWeek13 = []
    wk1srcCount = []
    wk2srcCount = []
    wk3srcCount = []
    wk4srcCount = []
    wk5srcCount = []
    wk6srcCount = []
    wk7srcCount = []
    wk8srcCount = []
    wk9srcCount = []
    wk10srcCount = []
    wk11srcCount = []
    wk12srcCount = []
    wk13srcCount = []

    # Append transmissionSource to their respective list based on dates
    for i in range(0, len(dateList), 1):
        if dateList[i] in listCheckWeek1:
            srcWeek1.append(src[i])
        elif dateList[i] in listCheckWeek2:
            srcWeek2.append(src[i])
        elif dateList[i] in listCheckWeek3:
            srcWeek3.append(src[i])
        elif dateList[i] in listCheckWeek4:
            srcWeek4.append(src[i])
        elif dateList[i] in listCheckWeek5:
            srcWeek5.append(src[i])
        elif dateList[i] in listCheckWeek6:
            srcWeek6.append(src[i])
        elif dateList[i] in listCheckWeek7:
            srcWeek7.append(src[i])
        elif dateList[i] in listCheckWeek8:
            srcWeek8.append(src[i])
        elif dateList[i] in listCheckWeek9:
            srcWeek9.append(src[i])
        elif dateList[i] in listCheckWeek10:
            srcWeek10.append(src[i])
        elif dateList[i] in listCheckWeek11:
            srcWeek11.append(src[i])
        elif dateList[i] in listCheckWeek12:
            srcWeek12.append(src[i])
        elif dateList[i] in listCheckWeek13:
            srcWeek13.append(src[i])
        else:  # If confirm dates are not specified
            print("Unspecified date result found!")
    # Variables to store count values for Local/Imported
    wk1Local = srcLocalCounter(srcWeek1)
    wk1Import = srcImportCounter(srcWeek1)

    wk2Local = srcLocalCounter(srcWeek2)
    wk2Import = srcImportCounter(srcWeek2)

    wk3Local = srcLocalCounter(srcWeek3)
    wk3Import = srcImportCounter(srcWeek3)

    wk4Local = srcLocalCounter(srcWeek4)
    wk4Import = srcImportCounter(srcWeek4)

    wk5Local = srcLocalCounter(srcWeek5)
    wk5Import = srcImportCounter(srcWeek5)

    wk6Local = srcLocalCounter(srcWeek6)
    wk6Import = srcImportCounter(srcWeek6)

    wk7Local = srcLocalCounter(srcWeek7)
    wk7Import = srcImportCounter(srcWeek7)

    wk8Local = srcLocalCounter(srcWeek8)
    wk8Import = srcImportCounter(srcWeek8)

    wk9Local = srcLocalCounter(srcWeek9)
    wk9Import = srcImportCounter(srcWeek9)

    wk10Local = srcLocalCounter(srcWeek10)
    wk10Import = srcImportCounter(srcWeek10)

    wk11Local = srcLocalCounter(srcWeek11)
    wk11Import = srcImportCounter(srcWeek11)

    wk12Local = srcLocalCounter(srcWeek12)
    wk12Import = srcImportCounter(srcWeek12)

    wk13Local = srcLocalCounter(srcWeek13)
    wk13Import = srcImportCounter(srcWeek13)

    # Lists for counts for all 13 weeks (Local and Imported)
    localCount13Weeks = [wk1Local, wk2Local, wk3Local, wk4Local, wk5Local, wk6Local, wk7Local, wk8Local, wk9Local,
                         wk10Local, wk11Local, wk12Local, wk13Local]
    importCount13Weeks = [wk1Import, wk2Import, wk3Import, wk4Import, wk5Import, wk6Import, wk7Import, wk8Import,
                          wk9Import, wk10Import, wk11Import, wk12Import, wk13Import]

    # Return Local Count as [0] and Import Count as [1]
    return localCount13Weeks, importCount13Weeks


def srcLocalCounter(l):
    '''
    This function checks the list passed through and counts if they are "Local"
    '''
    localCounter = 0
    for i in l:
        localCounter = l.count("Local")

    return localCounter


def srcImportCounter(l):
    '''
    This function checks the list passed through and counts if they are "Imported"
    '''
    importcounter = 0
    for i in l:
        importCounter = l.count("Imported")
    return importCounter


def srcLineGraph():
    '''
    This function plots the Line Graph of Transmission Type for the first 5000 COVID patients in periods of weeks.
    The x and y axis are populated with the function srcAxes.
    '''
    grp1 = srcAxes()[0]
    grp2 = srcAxes()[1]
    xAxis = ["Wk1", "Wk2", "Wk3", "Wk4", "Wk5", "Wk6", "Wk7", "Wk8", "Wk9", "Wk10", "Wk11", "Wk12", "Wk13"]
    plt.plot(xAxis, grp1, label="Community Cases in Singapore")
    plt.plot(xAxis, grp2, label="Imported Cases")
    plt.xlabel("Weeks")
    plt.ylabel("Count of Transmission Type")
    plt.title("Count of Transmission Type (Community Cases/Imported) with weeks\n\n 23 Jan 2020 to 17 Apr 2020")
    plt.legend()
    plt.grid(True)
    plt.show()


# ----------            End of Codes for Visual #5                 ------------------------------------------------------------------#

# ---------- ageBarGraph()           Visual #6 - Plots a Bargraph to show Age Count for the first 5000 Covid Patients                ----------#

def ageAxes(data=var.getAge()):
    '''
    This function returns 2 values for populating the Bar Graph.
    The first return value can be accessed by the index [0].
    The first return value can be accessed by the index [1].
    '''
    phList = []
    for i in range(0, len(data), 1):
        if math.isnan(data[i]) == False:
            phList.append(data[i])
    setAges = set(phList)
    uniqueAgeList = list(setAges)

    phCountList = []
    for i in phList:
        count = phList.count(i)
        phCountList.append(count)

    dictAgeCount = dict()
    for i in range(0, len(phList), 1):
        dictAgeCount[phList[i]] = phCountList[i]
    return dictAgeCount.keys(), dictAgeCount.values()


def ageBarGraph():
    '''
    This function plots the Bar Graph of Age Count for the first 5000 COVID patients.
    The x and y axis are populated with the function ageAxes.
    '''
    axes = ageAxes()
    xAxis = axes[0]  # The first of 2 return values accessed
    yAxis = axes[1]  # The second of 2 return values accessed
    plt.bar(xAxis, yAxis, color="#444444", label="covid")
    plt.xlabel("Age")
    plt.ylabel("Age Count")
    plt.title("Age group of first 5000 COVID-19 Patients")
    plt.show()
# ----------            End of Codes for Visual #6         -----------------------------------------------------------------------#

# ---                End of Visual Functions                   ---#
