import pandas as pd
from pandastable import Table, TableModel
from tkinter import *
import var


def getFrame(x):
    global framed
    framed = x


def lclicked():
    class localApp(Frame):
        def __init__(self, parent=framed):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.parent
            f = Frame(self.main)
            f.pack(fill=BOTH, expand=1)
            self.table = pt = Table(f, dataframe=local,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()
            return

    df = var.convertToDF(var.file_path)
    localCases = df.loc[df['Transmission Type'] == "Local"]  # Retrieve local cases
    caseIDL = localCases.get("Case ID")
    dateCfmL = localCases.get("Confirmed Date")
    hospitalsL = localCases.get("Hospital")
    genderL = localCases.get("Gender")
    ageL = localCases.get("Age").dropna().astype('int64')
    natL = localCases.get("Nationality")
    placesVisitedL = localCases.get("Places Visited")
    frame = {'Confirmed Date': dateCfmL, 'Hospital': hospitalsL, 'Gender': genderL, 'Age': ageL, 'Nationality': natL,
             'Places Visited': placesVisitedL}
    local = pd.DataFrame(frame, dtype=object)
    localApp()
    # res = "There are total of %d local cases" % (numlocalCases(len(df), data=typeTrans))

    # lbl.configure(text=res)


def impclicked():
    class importApp(Frame):
        def __init__(self, parent=framed):
            self.parent = parent
            Frame.__init__(self)
            self.main = self.parent
            f = Frame(self.main)
            f.pack(fill=BOTH, expand=1)
            self.table = pt = Table(f, dataframe=imported,
                                    showtoolbar=True, showstatusbar=True)
            pt.show()
            return

    df = var.convertToDF(var.file_path)
    importCases = df.loc[df['Transmission Type'] == "Imported"]  # Retrieve dataFrame for imported cases only
    caseIDI = importCases.get("Case ID")
    dateCfmI = importCases.get("Confirmed Date")
    hospitalsI = importCases.get("Hospital")
    genderI = importCases.get("Gender")
    ageI = importCases.get("Age").dropna().astype('int64')  # convert to int for display
    natI = importCases.get("Nationality")
    placesVisitedI = importCases.get("Places Visited")
    frame = {'Confirmed Date': dateCfmI, 'Hospital': hospitalsI, 'Gender': genderI, 'Age': ageI, 'Nationality': natI,
             'Places Visited': placesVisitedI}
    imported = pd.DataFrame(frame, dtype=object)
    importApp()
    # res = "There are total of %d imported cases" % (numImpCases(len(df), data=typeTrans))
    # lbl.configure(text=res)
