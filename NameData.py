#NameData.py
#To check first names in finland's name data

#Libraries
import sys
from matplotlib import pyplot as plt

#Own libraries
import FileManager

#Functions

def TopFive(dict1,dict2): #Shows top 5 first names
    i = 0
    print("Men: ")
    for key in dict1:
        if i == 5:
            i = 0
            break
        print(key)
        i += 1
    print("\nWomen: ")
    for key in dict2:
        if i == 5:
            print("")
            break
        print(key)
        i += 1


def CheckName(dict): #Checks if the name is on the list and gives details if found.
    name = input("Name to check: ")
    name = name[0].upper() + name[1:].lower()
    if "-" in name: #fix formatting if name has "-" in it
        x = 0
        for i in name:
            x += 1
            if i == "-":
                name = name[0].upper() + name[1:x].lower() + name[x].upper() + name[x+1:].lower()
                break

    if name in dict:
        print("Found name with following details:")
        print("{0} people have \'{1}\' as their first name.".format(dict[name], name))
    else:
        print("Couldn't find \'{0}\' in the name list".format(name))
    print("")

def ShowTop(dict):#Shows top X names (user given value)
    try:
        top = int(input("How many names from the top: "))
    except:
        print("Not proper value")
        return
    i = 0
    names = []
    values = []

    for key, value in sorted(dict.items(), key = lambda dict: dict[1], reverse=True):
        if i != top:
            names.append(key)
            values.append(value)
            i += 1

    plt.bar(names,values)
    plt.show()
    print("")

def ShowSpecific(dict): #Shows specific name among top 10
    name = input("What name would you like to show: ")
    name = name[0].upper() + name[1:].lower()
    if "-" in name: #fix formatting if name has "-" in it
        x = 0
        for i in name:
            x += 1
            if i == "-":
                name = name[0].upper() + name[1:x].lower() + name[x].upper() + name[x+1:].lower()
                break
    names = []
    values=[]
    top = 10
    i = 0

    for key, value in sorted(dict.items(), key = lambda dict: dict[1], reverse=True):
        if i != top:
            names.append(key)
            values.append(value)
            i += 1
        if key == name:
            names.append(key)
            values.append(value)
    if len(names) != top + 1:
        print("Didn't find given name.")
        print("")
        return

    plt.bar(names[:-1],values[:-1])
    plt.bar(names[-1],values[-1],color="y")
    plt.show()
    print("")


def Menu(): #Start menu
    print("1) Check names")
    print("2) Visualize data")
    print("3) Show top 5 names from male, and female")
    print("0) Exit")
    choice = int(input("Select: "))
    return choice

def VisMenu(): #Visualization menu
    print("***** Visualization options *****")
    print("1) Show top names")
    print("2) Show specific name among top names")
    print("0) Back to previous menu")
    choice = int(input("Select: "))
    print("")
    return choice

#Main
def Main(dict):
    print("Finland's first name data, last updated 03.09.2018")
    while True:
        try:
            option = Menu()
        except:
            pass
        if option == 1:
            CheckName(dict)
        elif option == 2:
            print("")
            try:
                VISoption = VisMenu()
            except:
                print("Unknown command.")
                print("")
                VISoption = 0
            if VISoption == 1:
                ShowTop(dict)
            elif VISoption == 2:
                ShowSpecific(dict)
            elif VISoption == 0:
                Main(dict)
            else:
                print("Unknown command.")
        elif option == 3:
            TopFive(FullDictionary.Men,FullDictionary.Women)
        elif option == 0:
            print("Good bye.")
            sys.exit()
        else:
            print("Unknown command.")

#running program
FullDictionary = FileManager.OpenFile()
AllData = FullDictionary.Full
Main(AllData)
