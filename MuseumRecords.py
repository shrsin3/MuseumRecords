# Museum Records

import csv
import pickle


# Functions for the Exhibit data text file

def AddExhibit():  # Add details of a new exhibit
    outfile = open("data.txt", "a")
    Name = input("Enter the name of the exhibit=")
    Floor = input("Enter the floor where exhibit is placed=")
    List = [Name, " :floor" + Floor + "\n"]
    outfile.writelines(List)
    outfile.close()
    print("Exhibit " + Name + " on floor " + Floor + " has been added to database")


def DisplayExhibit():  # Display Details of all the exhibits in the museum
    outfile = open("data.txt", "r")
    List = outfile.readlines()
    outfile.close()
    print(List)
    for L in List:
        namess = L.split(":floor")
        print(namess)
        print("\nExhibit Name:", namess[0])
        print("Floor on which the exhibit is placed:", namess[1])


def ModifyExhibit():  # Modify Details of exhibits in the museum by searching them by name
    while True:

        Name = input("Enter the name of exhibit=")

        outfile = open("data.txt", "r")
        List = outfile.readlines()
        outfile.close()

        Found = -1
        for i in range(len(List)):
            namess = List[i].split(":floor")
            print(namess)
            if (namess[0] == Name + " "):
                Found = i
                Floor = input("Enter the corrected floor where exhibit is placed: ")
                namess[1] = Floor
                List[i] = namess[0] + ":floor" + namess[1] + "\n"
                print(List)
                break

        if (Found == -1):
            print("Match not Found!!")
            break
        else:
            outfile = open("data.txt", "w")
            outfile.writelines(List)
            outfile.close()
            print("Data Updated!!")
            break


def DeleteExhibit():  # Delete record of an exhibit of the museum by searching them by name

    while True:

        Name = input("Enter the name of exhibit=")

        outfile = open("data.txt", "r")
        List = outfile.readlines()
        outfile.close()

        Found = -1
        for i in range(len(List)):
            namess = List[i].split(":floor")
            if (namess[0] == Name + " "):
                Found = i
                List.pop(i)
                break

        if (Found == -1):
            print("Match not Found!!")
            break
        else:
            outfile = open("data.txt", "w")
            outfile.writelines(List)
            outfile.close()
            print("Data Updated!!")
            break


############################################
############################################
############################################

# Functions for the visitors data binary file


def visitoradd():  # Add records of the visitors
    List = []
    Num = int(input("Enter the number of records to be added="))
    for i in range(Num):
        Name = input("Enter name of the Person: ")
        PhoneNo = int(input("Enter Phone Number of the Person: "))
        Data = [Name, PhoneNo]
        List.append(Data)

    outFile = open("visitors.dat", "ab")
    pickle.dump(List, outFile)
    outFile.close()


def visitorModify():  # Modify the records of a visitor

    FoundIndex = -1

    print("VISITOR FILE MODIFY MENU ")
    print("1. Modify by Name.\n")
    print("2. Modify by Phone Number.\n")
    Ch = int(input("Enter your choice: "))

    if (Ch == 1):
        Name = input("Enter Name of the Person to be modified: ")
    else:
        PhoneNo = int(input("Enter Phone Number of the Person to be modified: "))

    while True:
        try:
            inFile = open("visitors.dat", "rb")
            List = pickle.load(inFile)
            inFile.close()
            break
        except:
            List = []
            break

    for i in range(len(List)):
        L = List[i]

        if (Ch == 1 and Name == L[0]):  # Searching details by Name
            FoundIndex = i
            PhoneNo = List[i][1]
            newPhoneNo = int(input("Enter the Modified Phone Number of the Person: "))
            List[i][1] = newPhoneNo
            print(PhoneNo, " has been modified as ", newPhoneNo)
            break

        elif (Ch == 2 and PhoneNo == L[1]):  # Searching details by Phone No.
            FoundIndex = i
            Name = List[i][0]
            newName = input("Enter the Modified Name of the Person: ")
            List[i][0] = newName
            print(Name, " has been modified as ", newName)
            break

    if (FoundIndex == -1):
        print("No Match Found!")

    else:
        outFile = open("visitors.dat", "wb")
        pickle.dump(List, outFile)
        outFile.close()


def visitorDelete():  # Delete record of a visitor

    FoundIndex = -1

    print("VISITOR FILE DELETE MENU")
    print("1. Delete by Name.\n")
    print("2. Delete by Phone Number.\n")
    Ch = int(input("Enter your choice: "))

    if (Ch == 1):
        Name = input("Enter Name of the Person to be deleted: ")
    else:
        PhoneNo = int(input("Enter Phone Number of the Person to be deleted: "))

    while True:
        try:
            inFile = open("visitors.dat", "rb")
            List = pickle.load(inFile)
            inFile.close()
            break
        except:
            List = []
            break

    for i in range(len(List)):
        L = List[i]
        if (Ch == 1 and Name == L[0]):  # Searching details by Name
            FoundIndex = i
            break
        elif (Ch == 2 and PhoneNo == L[1]):  # Searching details by Name
            FoundIndex = i
            break

    if (FoundIndex == -1):
        print("No Match Found!")
    else:
        Data = List.pop(FoundIndex)
        print(Data, " has been deleted!")
        outFile = open("visitors.dat", "wb")
        pickle.dump(List, outFile)
        outFile.close()


def visitorDisplay():  # Display details of all the visitors

    inFile = open("visitors.dat", "rb")
    List = pickle.load(inFile)
    inFile.close()
    for i in range(len(List)):
        print("Name=", List[i][0])
        print("Phone Number=", List[i][1])


######################################################
######################################################
######################################################

# Functions of a csv file containing  museum tours data


def addLang():  # Adding a new language

    outfile = open('languages.csv', 'a', newline='')
    File = csv.writer(outfile)
    Lang = input('Enter language: ')
    NumAvailable = int(input('Enter Number of tours available in this language: '))
    Data = [Lang, NumAvailable]
    File.writerow(Data)
    outfile.close()


def DisplayLang():  # Displaying the language and number of tours in each available

    outfile = open('languages.csv', 'r', newline='\r\n')
    RFile = csv.reader(outfile)

    for A in RFile:
        print(A[0], "-", A[1])

    outfile.close()


######################################################
######################################################
######################################################

# Menu for whole rogram


while True:
    print("\n\nMuseum Records Menu")
    print("1. Exhibit Records")
    print("2. Visitors Records")
    print("3. Museum tours Records")
    print("4. Exit.")

    try:
        Choice = int(input("\nEnter the record you want to access="))
    except ValueError:
        print("Invalid Input!!")
        continue

    if (Choice == 1):
        while True:
            print("\nOperations Menu for Exhibit Record")
            print("1. Add data for a new exhibit")
            print("2. Display data of all exhibits")
            print("3. Modify data of an exhibit")
            print("4. Delete data of an exhibit")
            print("5. Exit.")

            try:
                Ch = int(input("Enter your choice="))
            except ValueError:
                print("Invalid Input!!")
                continue


            if (Ch == 1):
                AddExhibit()
            elif (Ch == 2):
                DisplayExhibit()
            elif (Ch == 3):
                ModifyExhibit()
            elif (Ch == 4):
                DeleteExhibit()
            elif (Ch == 5):
                break
            else:
                print("Invalid Operation!!")
                n = input("Press any key!!")
    elif (Choice == 2):
        while True:
            print("\nOperations Menu for Visitor Record")
            print("1. Add details of visitors")
            print("2. Modify details of visitor.")
            print("3. Delete Details of visitor")
            print("4. Display Details of visitors")
            print("5. Exit")

            try:
                Ch = int(input("Enter your choice="))
            except ValueError:
                print("Invalid Input!!")
                continue

            if (Ch == 1):
                visitoradd()
            elif (Ch == 2):
                visitorModify()
            elif (Ch == 3):
                visitorDelete()
            elif (Ch == 4):
                visitorDisplay()
            elif (Ch == 5):
                break
            else:
                print("Invalid Operation!!")
                n = input("Press any key!!")

    elif (Choice == 3):
        while True:
            print("\nOperations Menu for Museum tour Record")
            print("1. Add a new language")
            print("2. Display all languages in which tour is available.")
            print("3. Exit.")

            try:
                Ch = int(input("Enter your choice="))
            except ValueError:
                print("Invalid Input!!")
                continue

            if (Ch == 1):
                addLang()
            elif (Ch == 2):
                DisplayLang()
            elif (Ch == 3):
                break
            else:
                print("Invalid Operation!!")
                n = input("Press any key!!")
    elif (Choice == 4):
        print("Thank You !!")
        break

    else:
        print("Invalid Operation!!")
        n = input("Press any key!!")





























