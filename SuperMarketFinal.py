from os import system
from time import sleep
from csvToDict import csvToDict

stocks = {}

def exportCSVend(stcks):
    fName = "stocks.csv"
    csvFile = open(fName, 'w')
    csvFile.write("Items,Available")
    csvFile.write("\n")
    for item in stcks:
        csvFile.write(f"{item},")
        csvFile.write(f"{stcks[item]},\n")
    csvFile.close()

# To get int
def getInt(statement):
    while True:
        try:
            integer = int(input(statement))
            return(integer)
        except:
            print("Not an integer...Try Again!")

# To reveal complete stocks Option1
def revStocks1(dict):
    print("Item Name\t\t\tAvailable\n")
    for items in dict:
        print(items, "\t\t\t\t", dict[items])

# To search in stocks Option2
def searchStock(whatToSearch, dict):
    remaining = dict[whatToSearch]
    print(f"There are currently {remaining} {whatToSearch} available.")

# To add item to stocks Option3
def addItem(stcks):
    while True:    
        addItem = input("Enter items name: ")
        addQuantity = getInt(f"Enter Quantity of {addItem}: ")
        stcks[addItem] = addQuantity
        x = input("Add more items? ").upper()
        if x == 'N':
            revStocks1(stcks)
            return(stcks)
        else:
            pass

# To overwrite items, Option4
def overWrite(stcks):
    revStocks1(stcks)
    while True:
        itemName = input("Above are the list of stocks, which one do you want to modify? ")
        try:
            print(f"Current quantity of {itemName} is {stcks[itemName]}")
            modifyTo = getInt("Modify To: ")
            stcks[itemName] = modifyTo
            system("cls")
            print("Updated Successfully...")
            revStocks1(stcks)
            return(stcks)
        except:
            print(f"No records found for {itemName}, please enter valid item name...")

# To delete a entry, Option5
def delStock(stcks):
    while True:    
        delItem = input("Which item do you want to delete from the entry? ")
        try:
            confirm = input(f"You are about to delete {delItem} from the stocks, Press Y to continue: ").upper()
            if confirm == 'Y':
                del stcks[delItem]
                print("Latest Entries:")
                revStocks1(stcks)
                return(stcks)
            else:
                print("Alright, Operation Cancelled...")
                sleep(1)
                return(stcks)
        except:
            print("No entry with that name please try again...")

# Export as CSV, Option6
def exportCSV(stcks):
    fName = input("Enter file name to export to: ") + ".csv"
    csvFile = open(fName, 'w')
    csvFile.write("Items,Available\n")
    for item in stcks:
        csvFile.write(f"{item},")
        csvFile.write(f"{stcks[item]}\n")
    print(f"Successfully exported to {fName}")
    csvFile.close()

# Read from a CSv Option7
def readCSV(stcks):
    while True:
        try:
            fileName = "stocks.csv"
            csvToDict(stcks, fileName)
            revStocks1(stcks)
            return(stcks)
        except:
            print("No file with that name!\n")
            print("Reasons for this error:")
            print("\t1) stocks.csv file not found!")
            print("\t2) Make sure the file is present in the same directory as this program.")
            print("\t3) Make sure the cases(Upper/Lower) are exactly the same as in the file name.")
            print("\t3) You can create another file named 'stocks.csv' and start fresh too.\n")
            ask = input("Try Again? ").upper()
            if ask == 'Y':
                readCSV(stcks)
            else:
                print("Ok, Operation Cancelled...")
                return(stcks)

# To get users choice of operation
def getChoice():
    while True:
        try:
            cho = int(input("INPUT: "))
            return(cho)
        except:
            print("Not a integer, Try Again...")

# If else to run user's choice of input and handle exceptions
def selector(x, stcks):
    if x == 1:
        system("cls")
        revStocks1(stcks)
    elif x == 2:
        user = input("What do you want to search? ")
        try:
            searchStock(user, stcks)
        except KeyError:
            print("There is no item with that name...")
    elif x == 3:
        stcks = addItem(stcks)
    elif x == 4:
        stcks = overWrite(stcks)
    elif x == 5:
        system("cls")
        stcks = delStock(stcks)
    elif x == 6:
        system("cls")
        exportCSV(stcks)
    elif x == 7:
        stcks = readCSV(stcks)
    return(stcks)

# Asks if user wants continue running the program or exit...
# def runAgain():
#     x = input("Return Home? ").upper()
#     if x == "Y":
#         main()
#     else:
#         print("Closing Program...")
#         sleep(1)
#         system("cls")

system("cls")
ask = input("Restart previous session? (Y/N): ").upper()
if ask == 'Y':
    readCSV(stocks)
else:
    print("Starting Fresh...")
    sleep(1)

while True:    
    system('cls')
    print("Available Options: ")
    print("1) View Complete stocks\t\t2) Search in stocks\t\t3) Add a new item")
    print("4) Overwrite existing stock\t5) Delete from stock\t\t6) Export as CSV")
    print("7) Read from a CSV")
    
    choice = getChoice()
    stocks = selector(choice, stocks) # Select Option
    
    exportCSVend(stocks)
    ch = input("Run Again? ").upper()
    if ch == "Y":
        pass
    else:
        break