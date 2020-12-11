from tkinter import *
import var


# store row details as an object
class Details:
    def __init__(self, caseID, confirmed, hospital, discharged, gender, age, nationality, transmission, dod, places,
                 lat, long):
        self.caseID = caseID
        self.confirmed = confirmed
        self.hospital = hospital
        self.discharged = discharged
        self.gender = gender
        self.age = age
        self.nationality = nationality
        self.transmission = transmission
        self.dod = dod
        self.places = places
        self.lat = lat
        self.long = long


frame = ''


def getFrameFromGui(x):
    global frame
    frame = x


def showAll(dataframe):
    """show all records in list view"""
    top200 = dataframe.head(200)
    for row in top200.iterrows():
        value = row[1]

        particulars = Details(value[0], value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8],
                              value[9], value[10], value[11])

        Label(frame, text="CaseID:", font=20).pack(anchor=W)
        Label(frame, text=particulars.caseID, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Confirmed Date:", font=20).pack(anchor=W)
        Label(frame, text=particulars.confirmed, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Hospital:", font=20).pack(anchor=W)
        Label(frame, text=particulars.hospital, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Discharged Date:", font=20).pack(anchor=W)
        Label(frame, text=particulars.discharged, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Gender:", font=20).pack(anchor=W)
        Label(frame, text=particulars.gender, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Age:", font=20).pack(anchor=W)
        Label(frame, text=str(particulars.age), font=("courier",10)).pack(anchor=W)

        Label(frame, text="Nationality:", font=20).pack(anchor=W)
        Label(frame, text=particulars.nationality, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Transmission Source:", font=20).pack(anchor=W)
        Label(frame, text=particulars.transmission, font=("courier",10)).pack(anchor=W)

        Label(frame, text="Date of Death:", font=20).pack(anchor=W)
        Label(frame, text=str(particulars.dod), font=("courier",10)).pack(anchor=W)

        Label(frame, text="Places Visited:", font=20).pack(anchor=W)
        Label(frame, text=str(particulars.places), font=("courier",10)).pack(anchor=W)
        Label(frame, text="\n").pack()


def showSearchData(x, y):
    showSearch(var.convertToDF(var.file_path), x, y)


def showSearch(dataframe, column, condition):
    """show records based on condition"""
    column_list = list(dataframe.columns)
    column = column.strip("'")
    column = column.strip("'")

    if column in column_list:
        if condition in list(dataframe[column].unique()):

            buffer = dataframe[dataframe[column] == condition]

            showAll(buffer)
        else:
            print("Please enter valid condition")

    else:
        print("Please enter valid column")
