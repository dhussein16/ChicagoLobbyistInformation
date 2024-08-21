# Dua'a Hussein, 655469322, dhusse4
# This project is meant to practice with a tiered project where
# the data accessing, data gathering, and data displaying are controlled
# by different files.
# We will be using this structure in order to access and modify 
# The lobbyist database, printing the data that is being requested by accessing 
# the object tier's functions

import sqlite3
import objecttier

##################################################################  
# general statistics: print out the general statistics of the lobbyist database
def display_general_statistics(dbConn):
    # use the functions inside of the objecttier to print out the general statistics
    print("General Statistics:")

    # call the num_lobbyists function
    lobbyists = objecttier.num_lobbyists(dbConn)
    print("  Number of Lobbyists:", "{:,}".format(lobbyists))

    # call the num employers function
    employers = objecttier.num_employers(dbConn)
    print("  Number of Employers:", "{:,}".format(employers))

    # call the num clients function
    clients = objecttier.num_clients(dbConn)
    print("  Number of Clients:", "{:,}".format(clients))

##################################################################  
# command one allows for the user to find the a lobbyist by their first
# or last name, with wildcards, and output matching lobbyists who match
# that input. If there are more than 100 lobbyists that match, the user
# will be asked to narrow their search
def command_one(dbConn):
    userInput = input("Enter lobbyist name (first or last, wildcards _ and % supported): \n")

    results = objecttier.get_lobbyists(dbConn, userInput)
    print("Number of lobbyists found:", len(results))
    print("") # new line for whitespace

    if len(results) == 0:
        return
    elif len(results) > 100:
        print("There are too many lobbyists to display, please narrow your search and try again...")
    else:
        for lobbyist in results:
            print(f"{lobbyist.Lobbyist_ID}",":", f"{lobbyist.First_Name}",
                  f"{lobbyist.Last_Name}", "Phone:", f"{lobbyist.Phone}")

################################################################## 
# command two will ask the user for a lobbyist id and then, if the
# lobbyist exists, prints out extensive and complete information about
# that lobbyist
def command_two(dbConn):
    userInput = input("Enter Lobbyist ID: \n")
    result = objecttier.get_lobbyist_details(dbConn, userInput)

    # if the object tier returns nothing, the lobbyist doesn't exist
    if result is None:
        print("No lobbyist with that ID was found.")

    else:
        # print out the corresponding information
        # include eveyrthing like the Middle Initial and Suffix too
        print(f"{result.Lobbyist_ID} :")
        print(f"  Full Name: {result.Salutation} {result.First_Name} {result.Middle_Initial} {result.Last_Name} {result.Suffix}")
        print(f"  Address: {result.Address_1} {result.Address_2} , {result.City} , {result.State_Initial} {result.Zip_Code} {result.Country}")
        print(f"  Email: {result.Email}")
        print(f"  Phone: {result.Phone}")
        print(f"  Fax: {result.Fax}")

        # Years Registered and Employers need to be handled differently since those
        # are lists. Combine the elements in those lists into a single string
        # that are separated by ,_ 
        yearsRegisteredString = ", ".join(map(str, result.Years_Registered))
        print(f"  Years Registered: {yearsRegisteredString}", end=', ')

        # Do the same to employers
        employersString = ", ".join(result.Employers)
        print(f"\n  Employers: {employersString}", end=', ')

        # print out the compensation with two spots after the decimal point
        print(f"\n  Total Compensation: ${result.Total_Compensation:,.2f}")

################################################################## 
# command three asks the user for a year, and should output the top n
# lobbyists based on their compensation for that year. 
# Note to self: check for N validity, not necessary for year
def command_three(dbConn):
    nInput = input("Enter the value of N: ")
    nInput = int(nInput)

    # check if the input was valid
    if nInput < 1:
        print("Please enter a positive value for N...")
        return
    
    # get the value for the year input
    yearInput = input("Enter the year: ")

    results = objecttier.get_top_N_lobbyists(dbConn, nInput, yearInput)

    # if there is nothing in results, nothing should print back
    if results:
        # set up a counter to keep track of the index, and use print statements
        # to print out the values associated with every lobbyist 
        # note to self: after the clients, a comma should be printed at the end.

        counter = 1
        for lobbyist in results:
            print(f"\n{counter} . {lobbyist.First_Name} {lobbyist.Last_Name}")
            print(f"  Phone: {lobbyist.Phone}")
            print(f"  Total Compensation: ${lobbyist.Total_Compensation:,.2f}")
            print(f"  Clients: {', '.join(lobbyist.Clients)}", end=', ')
            counter += 1


################################################################## 
# command four should register an existing lobbyist for a new year, where the user
# will be allowed to enter the ID of the lobbyist and the year and insert
# that infromation into the database, letting the user know if the lobbyist does
# not exist
def command_four(dbConn):
    # get the inputs
    yearInput = input("Enter year: ")
    idInput = input("Enter the lobbyist ID: ")

    # call the object tier in order to get the results
    # result should be either 0 or 1, 
    result = objecttier.add_lobbyist_year(dbConn, idInput, yearInput)

    # if the result was zero, there was either an error or the lobbyist doesn't exist
    # otherwise, it exists and is successfully registered
    if result == 1:
        print("\nLobbyist successfully registered.")

    else:
        print("\nNo lobbyist with that ID was found.")


################################################################## 
# command five should allow the user to set the salutation of a lobbyist, 
# replacing the old salutation if there is one. If the lobbyist does 
# not exist, let the user know
def command_five(dbConn):
    # get the user input
    lobbyistID = input("Enter the lobbyist ID: ")
    userSalutation = input("Enter the salutation: ")

    # call the objecttier set salutation function
    result = objecttier.set_salutation(dbConn, lobbyistID, userSalutation)

    # check the result and print the corresponding message
    if result == 1:
        print("\nSalutation successfully set.")
    else:
        print("\nNo lobbyist with that ID was found.")

##################################################################  
# main
print('** Welcome to the Chicago Lobbyist Database Application **')

# Connect the database
dbConn = sqlite3.connect("Chicago_Lobbyists.db")

# print the general statistics by calling the function
display_general_statistics(dbConn);

# ask the user for initial input 
userInput = 'a'

while (userInput != 'x'):
    # check the user's input
    print()
    print("Please enter a command (1-5, x to exit): ")
    userInput = input()

    # call the corresponding command functions
    if userInput == '1':
        command_one(dbConn)
    elif userInput == '2':
        command_two(dbConn)
    elif userInput == '3':
        command_three(dbConn)
    elif userInput == '4':
        command_four(dbConn)
    elif userInput == '5':
        command_five(dbConn)
    elif userInput == 'x':
        break
    else:
        print("**Error, unknown command, try again...")



