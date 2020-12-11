import pandas as pd

file_path = 'mastercopy_5000_cleaned.csv'


def convertToDF(x):
    global file_path
    file_path = x
    file_name = file_path  # In same Folder
    file = pd.read_csv(file_name, sep=",")  # Opens CSV in same folder as the .py file
    df = pd.DataFrame(file)  # Converts to dataframe for easier handling
    df.columns = ["Case ID", "Confirmed Date", "Hospital", "Discharged Date", "Gender", "Age", "Nationality",
                  "Transmission Type", "Date of Death", "Places Visited", "Latitude", "Longitude"]  # Rename Columns
    return df


def getCaseID():
    df = convertToDF(file_path)
    caseID = df.get("Case ID")  # Type == str
    return caseID


def getDateCfm():
    df = convertToDF(file_path)
    dateCfm = df.get("Confirmed Date")  # Type == str
    return dateCfm


def getHospitals():
    df = convertToDF(file_path)
    hospitals = df.get("Hospital")  # Type == str
    return hospitals


def getDateDis():
    df = convertToDF(file_path)
    dateDis = df.get("Discharged Date")  # Type == str
    return dateDis


def getGender():
    df = convertToDF(file_path)
    gender = df.get("Gender")  # Type == str
    return gender


def getAge():
    df = convertToDF(file_path)
    age = df.get("Age")  # Type == float
    return age


def getNat():
    df = convertToDF(file_path)
    nat = df.get("Nationality")  # Type == str
    return nat


def getTypeTrans():
    df = convertToDF(file_path)
    typeTrans = df.get("Transmission Type")  # Type == str
    return typeTrans


def getDateDeath():
    df = convertToDF(file_path)
    dateDeath = df.get("Date of Death")  # Type == str
    return dateDeath


def getPlacesVisited():
    df = convertToDF(file_path)
    placesVisited = df.get("Places Visited")  # Type == str
    return placesVisited


def getLong():
    df = convertToDF(file_path)
    longitude = df.get("Longitude")  # Type == str
    return longitude


def getLat():
    df = convertToDF(file_path)
    latitude = df.get("Latitude")  # Type == str
    return latitude
