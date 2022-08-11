# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# EBrown,8.10.2022,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("/Users/emily/Documents/Python Class/Assignment05/ToDoList.txt", "r")
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Item":lstRow[0].strip(),"Priority":lstRow[1].strip()}
    lstTable.append(dicRow)
objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        for dicRow in lstTable:
            print("Item = " + dicRow["Item"] + ", " + "Priority = " + dicRow["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        NewItem = input("Enter item:")
        NewPriority = input("Enter priority:")
        dicRow = {"Item": NewItem.strip(), "Priority": NewPriority.strip()}
        lstTable.append(dicRow)
        print("New item added!")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        RemoveItem = input("Item to be removed:")
        RowNumber = 0
        while RowNumber < len(lstTable):
            if RemoveItem == list(dict(lstTable[RowNumber]).values())[0]:
                del lstTable[RowNumber]
                print("Item removed!")
            RowNumber = RowNumber + 1

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("/Users/emily/Documents/Python Class/Assignment05/ToDoList.txt", "w")
        for dicRow in lstTable:
            objFile.write(dicRow["Item"] + "," + dicRow["Priority"] + "\n")
        print("Data saved to ToDoList.txt!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print("Program will end now. Thank you!")
        break  # and Exit the program
