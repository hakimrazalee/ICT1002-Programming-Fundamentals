import smtplib
from email.message import EmailMessage
import pandas as pd
import var

recipient = ''


def clear_data(x):  # to clear any data in the treeview
    x.delete(*x.get_children())
    return None


def readData(x, y, z):  # x = Treeview, y= by What column, z=Asc or Descending

    df = pd.read_csv(var.file_path)  # reading and getting the dataframe
    df.sort_values(by=[y], inplace=True, ascending=z)  # sort function based on user inputs

    # This section populates the treeview frame that displays our data
    x["column"] = list(df.columns)
    x["show"] = "headings"
    for column in x["columns"]:
        x.heading(column, text=column)  # let the column heading = column name

    df_rows = df.to_numpy().tolist()  # turns the dataframe into a list of lists
    for row in df_rows:
        x.insert("", "end",
                 values=row)  # inserts each list into the treeview.
    return df.sort_values(by=[y], inplace=True, ascending=z)  # return the dataframe


def recipientKeyed(x, file):
    global recipient  # make recipient variable global to allow change
    recipient = x  # takes the recipient from user entry in GUI
    msg = EmailMessage()  # creating the email
    msg['Subject'] = 'Exported File from Group 45 Application'
    msg['From'] = 'ict1002grp45@gmail.com'
    msg['To'] = recipient
    msg.set_content("The attached was sent using [ICT1002]Group 45's application.")

    with open(file, 'rb') as f:  # read the file we want to export. rb = read byte
        file_data = f.read()  # reads the content
        file_name = 'Sorted Data Exported from Application.csv'

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream',
                       filename=file_name)  # to add an attachment to the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('ict1002grp45@gmail.com',
                   '(Your Password Here)')  # login information. (Simulated as imported from module would be preferred)
        smtp.send_message(msg)  # sends the email


def export(a, y, z):  # used to export and email
    df = pd.read_csv(var.file_path)  # get dataframe (in this case file is selected by user)
    df.sort_values(by=[y], inplace=True, ascending=z)  # sorted according to user
    df.to_csv('ICT1002Group45Project.csv', index=False)  # saves the user's sort option and exports the file
    recipientKeyed(a,
                   'ICT1002Group45Project.csv')  # file is saved as the specified name. executes the send email function after getting a(recipient)


def exportOnly(y, z):  # used to export ONLY
    df = pd.read_csv(var.file_path)  # get dataframe (in this case file is selected by user)
    df.sort_values(by=[y], inplace=True, ascending=z)  # sorted according to user
    df.to_csv('ICT1002Group45Project.csv', index=False)  # saves the user's sort option and exports the file
