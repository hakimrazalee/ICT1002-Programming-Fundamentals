from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import var
import appFunctions
import tableFunctions
import emailFunctions
import searchFunctions
# imported modules used for GUI to function


def fileBrowser():
    """This function will only run after user presses browse-a-file button"""

    def hideFrames():
        """This function is used to clear all the contents in the frame after navigating to a new function"""
        contentFrame.pack_forget()  # forgets the frame storing content temporarily until it is being packed again.
        for widget in contentFrame.winfo_children():  # loops through all the widgets used in the content frame and destroy all of them
            widget.destroy()

        mainMenuFrame.pack_forget()  # forgets the mainMenuFrame which is different from the frame storing content.
        for widget in mainMenuFrame.winfo_children():
            widget.destroy()

        return

    MainPageLabel1.destroy()  # From this point on, the gui is remodelling itself by destroying past created labels and buttons
    MainPageLabel2.destroy()
    browseButton.destroy()

    # stores the file path of the user selected data-set to be used with our other functions
    file_path = filedialog.askopenfilename(initialdir="",
                                           title="Select Dataset File",
                                           filetypes=((".csv Files", "*.csv"), ("All Files", "*.*")))

    # sending file path to var so other functions can use the file path
    var.convertToDF(file_path)  # parse file path

    # Window that updates after selecting CSV file
    console.geometry("1000x650")

    def graphData():
        """Upon Navigating to the 'Generate Graph' Button, this function will run"""
        hideFrames()
        # To disable button from being able to be pressed again.
        buttonFrame.pack()
        mainframe.pack(fill=BOTH, expand=1)
        contentFrame.pack(fill=BOTH, expand=1)
        dataType = [  # dropdown list options
            "Bar Graph projecting Age of COVID-19 patients in Singapore",
            "Bar Graph projecting Confirmed COVID-19 patients in Singapore over 13 weeks",
            "Line Graph projecting the Nationality of COVID-19 patients in Singapore",
            "Line Graph projecting the Transmission Type of COVID-19 patients in Singapore",
            "Map Plots projecting No. Of COVID-19 Patients using facilities in Singapore",
            "Pie Chart projecting Facilities used by Patients of COVID-19 in Singapore",

        ]

        clicked = StringVar()
        clicked.set(dataType[0])

        def selectedDataType(event):
            """This function listens to the 'event' and displays the graph based on the datatype selected using the combobox"""
            if combo.get() == "Bar Graph projecting Age of COVID-19 patients in Singapore":
                appFunctions.ageBarGraph()

            elif combo.get() == "Bar Graph projecting Confirmed COVID-19 patients in Singapore over 13 weeks":
                appFunctions.cfmCaseWeekBarChart()

            elif combo.get() == "Line Graph projecting the Nationality of COVID-19 patients in Singapore":
                appFunctions.natDaysLineGraph()

            elif combo.get() == "Line Graph projecting the Transmission Type of COVID-19 patients in Singapore":
                appFunctions.srcLineGraph()

            elif combo.get() == "Map Plots projecting No. Of COVID-19 Patients using facilities in Singapore":
                appFunctions.facilitiesGeogMap()

            elif combo.get() == "Pie Chart projecting Facilities used by Patients of COVID-19 in Singapore":
                appFunctions.facilitiesPieChart()

        combo = ttk.Combobox(contentFrame, value=dataType, font=(20), width=80)  # using tkinter's combobox as the drop down lsit
        combo.current(0)  # displays the default selected option
        combo.bind("<<ComboboxSelected>>", selectedDataType)  # bind any event to a selection
        ddListLabel = Label(contentFrame, text="Choose your data type for the graph to be generated:", font=(30))

        # packing area (Used to pack any functions from tkinter into the screen)
        ddListLabel.pack(pady=50)
        combo.pack()

    def tableData():
        """This function runs when users navigate to the 'View Covid-19 data' Button"""
        hideFrames()

        def hideLocal():  # function to hide local button to prevent users from generating multiple tables
            tableFunctions.lclicked()
            buttonLocal.destroy()
            buttonImported.destroy()
            infoTable.destroy()
            return

        def hideImported():  # function to hide imported button to prevent users from generating multiple tables
            tableFunctions.impclicked()
            buttonLocal.destroy()
            buttonImported.destroy()
            infoTable.destroy()
            return

        tableFunctions.getFrame(
            contentFrame)  # passes information on the selected frame to display the table through parameters
        infoTable = Label(contentFrame, text="Click on one of the buttons below to view data of 'Local' or 'Imported' cases.", font=(30))
        buttonLocal = Button(contentFrame, text="Display Local Cases Table", font=(200), width=100, bg="white",
                             command=hideLocal)  # clicking one button to display local/imported data will hide buttons and display table, vice versa
        buttonImported = Button(contentFrame, text="Display Imported Cases Table", command=hideImported, font=(200), width=100, bg="white")

        # function packing area
        infoTable.pack(fill=BOTH, pady=50)
        buttonLocal.pack(pady=20)
        buttonImported.pack(pady=20)

        # default packing area
        buttonFrame.pack()  # Navigation bar buttons
        mainframe.pack(fill=BOTH, expand=1)  # frame to store contentFrame
        contentFrame.pack(fill=BOTH, expand=1)  # frame storing content

    def searchData():
        """This function is used to search for column-specific data"""
        hideFrames()  # to reset frame
        topFrame = Frame(contentFrame, height=100, width=100,
                         relief=SUNKEN)  # top frame used to seperate between frame that is used to search and frame that displays data
        Label(topFrame,
              text="Search and display specific data by selecting the columns and conditions below: ", font=(30)).grid(row=0, pady=10)

        columnChoice = [  # Drop down options
            "Case ID",
            "Confirmed Date",
            "Hospital",
            "Discharged Date",
            "Gender",
            "Age",
            "Nationality",
            "Transmission Source",
            "Date of Death",
            "Places Visited",
        ]

        clicked = StringVar()  # used to store the value of the dropdown list
        clicked.set(columnChoice[0])  # current default value
        columnChoose = OptionMenu(topFrame, clicked, *columnChoice)  # specifies the dropdown list options
        Label(topFrame, text="Column (example: CaseID): ", font=10).grid()
        columnChoose.grid()  # places the dropdown list in the gui using grid method
        Label(topFrame, text="Value (example: case-1): ", font=10).grid()

        v = StringVar()  # initialise variable to store user input
        Entry(topFrame, textvariable=v).grid(padx=10)  # user input box

        def searchColumns():
            userInput = v.get()  # gets the user input
            columnInput = clicked.get()  # gets the dropdown list option selected
            searchFunctions.showSearchData(columnInput, userInput)  # execute search/sort by using the user inputs
            return

        searchButton = Button(topFrame, text="Search",
                              command=searchColumns)  # executes the serach columns function
        searchButton.grid()  # places the search button on the gui

        class ScrollableFrame(Frame):  # This class generates the frame that is used to store the data being displayed
            def __init__(self, container, *args, **kwargs):
                super().__init__(container, *args, **kwargs)
                canvas = Canvas(self)
                scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
                self.scrollable_frame = ttk.Frame(canvas)

                self.scrollable_frame.bind(
                    "<Configure>",
                    lambda e: canvas.configure(
                        scrollregion=canvas.bbox("all")
                    )
                )

                canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

                canvas.configure(yscrollcommand=scrollbar.set)

                canvas.pack(side="left", expand=True)
                scrollbar.pack(side="right", fill="y")

        scrollFrame = ScrollableFrame(contentFrame)  # places the displaying data frame into the content holding frame
        searchFunctions.getFrameFromGui(
            scrollFrame.scrollable_frame)  # sends information to the function on where to place the data

        # function packing area
        topFrame.pack()  # display/packs the top frame on screen
        scrollFrame.pack(fill=BOTH, expand=1)

        # default packing area
        buttonFrame.pack()
        mainframe.pack(fill=BOTH, expand=1)
        contentFrame.pack(fill=BOTH, expand=1)

        return

    def sendEmail():
        """This function is used to export and send the data through E-mail in the GUI"""
        hideFrames()  # resets the frame

        treeFrame = LabelFrame(contentFrame, text="Data")  # create a frame to store displayed data
        treeview1 = ttk.Treeview(treeFrame)  # uses the treeview widget
        treeview1.place(relheight=1, relwidth=1)
        treeScrolly = Scrollbar(treeFrame, orient="vertical",
                                command=treeview1.yview)  # command means update the yaxis view of the widget
        treeScrollx = Scrollbar(treeFrame, orient="horizontal",
                                command=treeview1.xview)  # command means update the xaxis view of the widget
        treeview1.configure(xscrollcommand=treeScrollx.set,
                            yscrollcommand=treeScrolly.set)  # assign the scrollbars to the Treeview Widget

        emailMainLabel = Label(contentFrame, text="Sort Table based on: ")

        sortType = [  # dropdown/sorting list options
            "Ascending",
            "Descending",
        ]

        def sortData(event):
            """Sorts the data and sends it to the emailFunctions file"""
            emailFunctions.clear_data(treeview1)  # Clear any data available
            if sortedData.get() == "Ascending":
                emailFunctions.readData(treeview1, column.get(), True)
            elif sortedData.get() == "Descending":
                emailFunctions.readData(treeview1, column.get(), False)

        sortedData = ttk.Combobox(contentFrame,
                                  value=sortType)  # combobox listens to the option being selected and executes the command
        sortedData.current(0)  # set default drop down box value
        sortedData.bind("<<ComboboxSelected>>", sortData)  # bind the combobox with the options

        columnType = [  # radio button selections
            ("CaseID", "CaseID"),
            ("Confirmed Date", "Confirmed Date"),
            ("Hospital", "Hospital"),
            ("Discharged Date", "Discharged Date"),
            ("Gender", "Gender"),
            ("Age", "Age"),
            ("Nationality", "Nationality"),
            ("Transmission Source", "Transmission Source"),
            ("Date of Death", "Date of Death"),
            ("Places Visited", "Places Visited",)
        ]

        column = StringVar()  # string var to store the option that will be selected
        column.set("CaseID")  # set default selected value to caseID
        radioButtonFrame = Frame(contentFrame, height=30, width=100)  # generates a frame to store the radio buttons

        i = 0  # counter for column placement
        for text, mode in columnType:  # for every option there is for columns, generate a radio button
            i += 1
            Radiobutton(radioButtonFrame, text=text, variable=column, value=mode).grid(row=0,
                                                                                       column=i)  # radio button generated and placed according to their position (i)

        def sendEmailTo():  # send email function
            """Sends the recipient info and the sorted data table settings to the emailFunction file to be sent"""
            a = recipient.get()  # get the user input
            if sortedData.get() == "Ascending":  # sorts according to drop down list option
                emailFunctions.export(a, column.get(), True)
            elif sortedData.get() == "Descending":
                emailFunctions.export(a, column.get(), False)

        def exportOnly():  # export function
            """Sends the sorted data table settings to the emailFunction file to be exported"""
            if sortedData.get() == "Ascending":  # sorts according to drop down list option
                emailFunctions.exportOnly(column.get(), True)
            elif sortedData.get() == "Descending":
                emailFunctions.exportOnly(column.get(), False)

        emailTo = Label(contentFrame, text="Input Recipient e-mail address: ")
        recipient = Entry(contentFrame)  # user input for recipient
        sendButton = Button(contentFrame, text='Export and Send file as E-mail (Following format chosen above)',
                            command=sendEmailTo)
        exportButton = Button(contentFrame, text='Export the file ONLY (Following format chosen above)', command=exportOnly)

        # function packing area
        radioButtonFrame.pack()
        emailMainLabel.pack()
        sortedData.pack()
        emailTo.pack()
        recipient.pack()
        exportButton.pack(pady=5)
        sendButton.pack(pady=5)
        treeFrame.pack(fill=BOTH, expand=1)
        treeScrollx.pack(side="bottom", fill="x")  # make the scrollbar fill the x axis of the Treeview widget
        treeScrolly.pack(side="right", fill="y")  # make the scrollbar fill the y axis of the Treeview widget

        # default packing area
        buttonFrame.pack()
        mainframe.pack(fill=BOTH, expand=1)
        contentFrame.pack(fill=BOTH, expand=1)

    def exitWindow():
        """This function forces the app to exit/quit"""
        console.quit()

    def startFromMenu():
        """This function re-does the gui navigation bar and frames after navigating from the menu page"""
        mainMenuFrame.pack_forget()  # removes any frame used for the main menu page
        graphData()  # brings user to the graph data page

        # creating of navigation bars
        homePageMenu = Button(buttonFrame, text="Main Menu", command=mainMenu, padx=20, pady=10)
        barGraphButtonMenu = Button(buttonFrame, text="Generate Graph", padx=20, pady=10, command=graphData)
        displayDataTableMenu = Button(buttonFrame, text="Read Covid-19 Data", padx=30, pady=10, command=tableData)
        sendEmailButtonMenu = Button(buttonFrame, text="Sort, export and send data as e-mail", padx=30, pady=10,
                                     command=sendEmail)
        listDataButtonMenu = Button(buttonFrame, text="List Data", padx=30, pady=10, command=searchData)
        exitButtonMenu = Button(buttonFrame, text="QUIT the Application", padx=30, pady=10, command=exitWindow)

        # default pack/grid area to place the buttons back
        homePageMenu.grid(row=0, column=0)
        barGraphButtonMenu.grid(row=0, column=1)
        displayDataTableMenu.grid(row=0, column=2)
        listDataButtonMenu.grid(row=0, column=3)
        sendEmailButtonMenu.grid(row=0, column=4)
        exitButtonMenu.grid(row=0, column=5)

    def fileBrowserFromMenu():  # will run if user selects the option to reupload dataset from the menu page
        """This function runs if user selects the option to reupload dataset from the menu page"""
        fileBrowser()  # prompts user to select file again
        mainMenuFrame.pack_forget()  # removes the mainmenuframe

    def mainMenu():
        """Function runs when users navigate to the main menu"""
        mainframe.pack_forget()  # hides any frames used for the content page/navigation bar
        buttonFrame.pack_forget()
        for widget in buttonFrame.winfo_children():  # removes all the buttons in the navigation bar
            widget.destroy()

        mainMenuFrame.pack(fill=BOTH, expand=1)  # create a new frame specifically for the main menu page
        Label(mainMenuFrame, text="MAIN MENU", font=("fixedsys", 44), bg="Black", fg="White").pack(
            anchor=N, expand=1)
        Label(mainMenuFrame, text="ICT1002 Project: Group 45", font=("fixedsys", 25), bg="Black", fg="White").pack(
            anchor=N, expand=1)
        startUse = Button(mainMenuFrame, text="Start Application", font=("fixedsys", 15), padx=44, pady=10,
                          command=startFromMenu)  # create start application button
        reUpload = Button(mainMenuFrame, text="Upload A New Data-set", font=("fixedsys", 15), padx=24, pady=10,
                          command=fileBrowserFromMenu)  # create reupload button
        exitFromMenu = Button(mainMenuFrame, text="QUIT", padx=30, font=("fixedsys", 15), pady=10,
                              command=exitWindow)  # create exit button

        # button packing area
        startUse.pack()
        reUpload.pack()
        exitFromMenu.pack(expand=1)

        return

    # default Frames Creation
    mainMenuFrame = Frame(console, relief=SUNKEN, height=800, width=1000, background='Black')
    buttonFrame = Frame(console, height=100, width=1000, borderwidth=10, relief=GROOVE, background='Black')
    mainframe = Frame(console, height=550, width=1000, borderwidth=10, relief=SUNKEN, background='Black')
    contentFrame = Frame(mainframe, height=600, width=1000, borderwidth=10)

    # Main Buttons creation section
    homePage = Button(buttonFrame, text="Main Menu", command=mainMenu, padx=20, pady=10)
    barGraphButton = Button(buttonFrame, text="Generate Graph", padx=20, pady=10, command=graphData)
    displayDataTable = Button(buttonFrame, text="Read Covid-19 Data", padx=30, pady=10, command=tableData)
    sendEmailButton = Button(buttonFrame, text="Sort, export and send data as e-mail", padx=30, pady=10, command=sendEmail)
    listDataButton = Button(buttonFrame, text="List Data", padx=30, pady=10, command=searchData)
    exitButton = Button(buttonFrame, text="QUIT the Application", padx=30, pady=10, command=exitWindow)

    # packing/grid area to display into the gui
    homePage.grid(row=0, column=0)
    barGraphButton.grid(row=0, column=1)
    displayDataTable.grid(row=0, column=2)
    listDataButton.grid(row=0, column=3)
    sendEmailButton.grid(row=0, column=4)
    exitButton.grid(row=0, column=5)
    buttonFrame.pack()
    mainframe.pack(fill=BOTH, expand=1)
    contentFrame.pack()
    Label(contentFrame, text="Start by navigating to one of our functions", font=("fixedsys", 20), fg='white', bg='black').pack(padx=50)  # Welcome page


# initialise starting GUI Window
console = Tk()
console.iconbitmap('icons/SIT_logo_2.ico')
console.title("1002 Python Project")
console.geometry("300x200")

# Create Label to instruct users to browse for data
MainPageLabel1 = Label(console, text="Welcome to our program!")
MainPageLabel2 = Label(console, text="Click on the button above to browse for a Dataset!")
# Button to browse for Dataset
browseButton = Button(console, text="Browse", padx=30, pady=10, command=fileBrowser)

# PACK SECTION
MainPageLabel1.pack(ipadx=20, ipady=20)
browseButton.pack()
MainPageLabel2.pack(ipadx=20, ipady=20)

console.mainloop()

