# objecttier
# Builds Lobbyist-related objects from data retrieved through 
# the data tier.
# Original author: Ellen Kidane

# Dua'a Hussein
# 655469322 dhusse4
# This is the objecttier, which is meant to set up the classes and functions needed for
# the user to organize and set up the data that we collect from the datatier 
# into objects. We end up using this in the presentationtier, which we use to present
# and write out the data that we find.

import datatier
##################################################################
# Lobbyist:
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
class Lobbyist:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone):
        self._Lobbyist_ID = int(Lobbyist_ID)
        self._First_Name = str(First_Name)
        self._Last_Name = str(Last_Name)
        self._Phone = str(Phone)

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property 
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone
    
##################################################################
# LobbyistDetails:
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   Salutation: string
#   First_Name: string
#   Middle_Initial: string
#   Last_Name: string
#   Suffix: string
#   Address_1: string
#   Address_2: string
#   City: string
#   State_Initial: string
#   Zip_Code: string
#   Country: string
#   Email: string
#   Phone: string
#   Fax: string
#   Years_Registered: list of years
#   Employers: list of employer names
#   Total_Compensation: float
class LobbyistDetails:
    def __init__(self, Lobbyist_ID, Salutation, First_Name, Middle_Initial, Last_Name, Suffix, Address_1, Address_2, 
                 City, State_Initial, Zip_Code, Country, Email, Phone, Fax, Years_Registered, Employers, Total_Compensation):
        self._Lobbyist_ID = int(Lobbyist_ID)
        self._Salutation = str(Salutation)
        self._First_Name = str(First_Name)
        self._Middle_Initial = str(Middle_Initial)
        self._Last_Name = str(Last_Name)
        self._Suffix = str(Suffix)
        self._Address_1 = str(Address_1)
        self._Address_2 = str(Address_2)
        self._City = str(City)
        self._State_Initial = str(State_Initial)
        self._Zip_Code = str(Zip_Code)
        self._Country = str(Country)
        self._Email = str(Email)
        self._Phone = str(Phone)
        self._Fax = str(Fax)
        self._Years_Registered = Years_Registered
        self._Employers = Employers
        self._Total_Compensation = float(Total_Compensation)

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def Salutation(self):
        return self._Salutation

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Middle_Initial(self):
        return self._Middle_Initial

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Suffix(self):
        return self._Suffix

    @property
    def Address_1(self):
        return self._Address_1

    @property
    def Address_2(self):
        return self._Address_2

    @property
    def City(self):
        return self._City

    @property
    def State_Initial(self):
        return self._State_Initial

    @property
    def Zip_Code(self):
        return self._Zip_Code

    @property
    def Country(self):
        return self._Country

    @property
    def Email(self):
        return self._Email

    @property
    def Phone(self):
        return self._Phone

    @property
    def Fax(self):
        return self._Fax

    @property
    def Years_Registered(self):
        return self._Years_Registered

    @property
    def Employers(self):
        return self._Employers

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

##################################################################
# LobbyistClients:
# Constructor(...)
# Properties:
#   Lobbyist_ID: int
#   First_Name: string
#   Last_Name: string
#   Phone: string
#   Total_Compensation: float
#   Clients: list of clients
class LobbyistClients:
    def __init__(self, Lobbyist_ID, First_Name, Last_Name, Phone, Total_Compensation, Clients):
        self._Lobbyist_ID = int(Lobbyist_ID)
        self._First_Name = str(First_Name)
        self._Last_Name = str(Last_Name)
        self._Phone = str(Phone)
        self._Total_Compensation = float(Total_Compensation)
        self._Clients = Clients

    @property
    def Lobbyist_ID(self):
        return self._Lobbyist_ID

    @property
    def First_Name(self):
        return self._First_Name

    @property
    def Last_Name(self):
        return self._Last_Name

    @property
    def Phone(self):
        return self._Phone

    @property
    def Total_Compensation(self):
        return self._Total_Compensation

    @property
    def Clients(self):
        return self._Clients

##################################################################
# num_lobbyists:
# Returns: number of lobbyists in the database
#           If an error occurs, the function returns -1
def num_lobbyists(dbConn):
    # create the sql query and try to execute it
    try:
        sqlQuery = """
                   SELECT COUNT(Lobbyist_ID)
                   FROM LobbyistInfo;
                   """
        result = datatier.select_one_row(dbConn, sqlQuery, None)
        if(result):
            return result[0]
        else:
            return []

    # if it doesnt run throw the error  
    except Exception as e:
        print(f"Error: {e}")
        return -1
    
##################################################################
# num_employers:
# Returns: number of employers in the database
#           If an error occurs, the function returns -1
def num_employers(dbConn):
    # create the sql query and try to execute it
    try:
        sqlQuery = """
                   SELECT COUNT(Employer_ID)
                   FROM EmployerInfo;
                   """
        result = datatier.select_one_row(dbConn, sqlQuery, None)

        if(result):
            return result[0]
        else:
            return [] 

    # if it doesnt run throw the error  
    except Exception as e:
        print(f"Error: {e}")
        return -1

##################################################################
# num_clients:
# Returns: number of clients in the database
# If an error occurs, the function returns -1
def num_clients(dbConn):
    # create the sql query and try to execute it
    try:
        sqlQuery = """
                   SELECT COUNT(Client_ID)
                   FROM ClientInfo;
                   """
        
        result = datatier.select_one_row(dbConn, sqlQuery, None)

        if(result):
            return result[0]
        else:
            return [] 

    # if it doesnt run throw the error  
    except Exception as e:
        print(f"Error: {e}")
        return -1

##################################################################
# get_lobbyists:
# gets and returns all lobbyists whose first or last name are "like"
# the pattern. Patterns are based on SQL, which allow the _ and % 
# wildcards.
# Returns: list of lobbyists in ascending order by ID; 
#          an empty list means the query did not retrieve
#          any data (or an internal error occurred, in
#          which case an error msg is already output).
def get_lobbyists(dbConn, pattern):
    # create the sql query
    sqlQuery = """
            SELECT Lobbyist_ID, First_Name, Last_Name, Phone
            FROM LobbyistInfo
            WHERE First_Name like ? or Last_Name like ?
            ORDER BY Lobbyist_ID asc;
            """

    # Pass the pattern with wildcard directly into the query
    result = datatier.select_n_rows(dbConn, sqlQuery, (pattern, pattern))
    lobbyists = []

    if result is None:
        return lobbyists
    else:
        for row in result:
            lobbyTemp = Lobbyist(row[0], row[1], row[2], row[3])
            lobbyists.append(lobbyTemp)
    return lobbyists

##################################################################
# get_lobbyist_details:
# gets and returns details about the given lobbyist
# the lobbyist id is passed as a parameter
# Returns: if the search was successful, a LobbyistDetails object
#          is returned. If the search did not find a matching
#          lobbyist, None is returned; note that None is also 
#          returned if an internal error occurred (in which
#          case an error msg is already output).
# RECOMMENDATION WAS: break apart the massive query into smaller queries
def get_lobbyist_details(dbConn, lobbyist_id):
    # set up the queries
    # basicInfo about the Lobbyist
    basicInfoQuery = """
                        SELECT Lobbyist_ID, Salutation, First_Name, Middle_Initial,
                               Last_Name, Suffix, Address_1, Address_2, City,
                               State_Initial, ZipCode, Country, Email, Phone, Fax
                        FROM LobbyistInfo
                        WHERE Lobbyist_ID = ?
                        ORDER BY Lobbyist_ID;
                     """
    
    # the total years Query
    yearsQuery = """
                    SELECT DISTINCT Year
                    FROM LobbyistYears
                    WHERE Lobbyist_ID = ?
                    ORDER BY Year;
                 """

    # the employers query
    employersQuery = """
                     SELECT DISTINCT Employer_Name
                     FROM LobbyistAndEmployer LAE
                     JOIN EmployerInfo ON LAE.Employer_ID = EmployerInfo.Employer_ID
                     WHERE LAE.Lobbyist_ID = ?
                     ORDER BY Employer_Name ASC;
                     """
    
    # the compensation query 
    totalCompensation = """
                        SELECT SUM(Compensation_Amount)
                        FROM Compensation
                        WHERE Lobbyist_ID = ?
                        GROUP BY Lobbyist_ID
                        ORDER BY Lobbyist_ID;
                        """

    # execute all the queries and store them into respective results, check if basicInfoRuns
    basicInfoResult = datatier.select_one_row(dbConn, basicInfoQuery, [lobbyist_id])

    if basicInfoResult is () or basicInfoResult is None:
        return None
    
    # if basicInfoResult is populated, run the other queries
    yearsResult = datatier.select_n_rows(dbConn, yearsQuery, [lobbyist_id])
    employerResult = datatier.select_n_rows(dbConn, employersQuery, [lobbyist_id])
    totalCompResult = datatier.select_one_row(dbConn, totalCompensation, [lobbyist_id])

    # years and employer are lists, and salary needs to be a float, so adjust
    yearsList = []
    employerList = []
    salary = totalCompResult[0] if totalCompResult else 0.00

    for info in yearsResult:
        yearsList.append(int(info[0]))

    for info in employerResult:
        employerList.append(info[0])

    # list(yearsList)
    # list(employersList)

    # get all the information into a LobbyistDetails Object
    LobbyistReturn = LobbyistDetails(basicInfoResult[0], basicInfoResult[1], basicInfoResult[2],
                                     basicInfoResult[3], basicInfoResult[4], basicInfoResult[5],
                                     basicInfoResult[6], basicInfoResult[7], basicInfoResult[8],
                                     basicInfoResult[9], basicInfoResult[10], basicInfoResult[11],
                                     basicInfoResult[12], basicInfoResult[13], basicInfoResult[14],
                                     yearsList, employerList, salary)

    return LobbyistReturn

##################################################################
# get_top_N_lobbyists:
# gets and returns the top N lobbyists based on their total 
# compensation, given a particular year
# Returns: returns a list of 0 or more LobbyistClients objects;
#          the list could be empty if the year is invalid. 
#          An empty list is also returned if an internal error 
#          occurs (in which case an error msg is already output).
def get_top_N_lobbyists(dbConn, N, year):
    try:
        # Construct the SQL query to retrieve top N lobbyists for the given year
        sql = """
              SELECT L.Lobbyist_ID, L.First_Name, L.Last_Name, L.Phone, SUM(C.Compensation_Amount) AS Total_Compensation 
              FROM Compensation C
              JOIN LobbyistInfo L ON L.Lobbyist_ID = C.Lobbyist_ID
              WHERE cast(strftime('%Y', Period_Start) as int) = ?
              GROUP BY L.Lobbyist_ID
              ORDER BY Total_Compensation DESC
              LIMIT ?;
              """

        # Execute the query to retrieve top N lobbyists for the given year
        rows = datatier.select_n_rows(dbConn, sql, (year, N))  # Ensure both parameters are provided

        # Initialize an empty list to store LobbyistClients objects
        top_lobbyists = []

        # Process the query results
        if rows:
            for row in rows:
                # Fetch clients associated with the current lobbyist
                clients_sql = """
                              SELECT DISTINCT C.Client_ID, C.Client_Name
                              FROM ClientInfo C
                              JOIN Compensation Comp on C.Client_ID = Comp.Client_ID
                              JOIN LobbyistInfo LI on LI.Lobbyist_ID = Comp.Lobbyist_ID
                              WHERE LI.Lobbyist_ID = ? AND cast(strftime('%Y', Period_Start) as int) = ?
                              ORDER BY C.Client_Name ASC;
                              """
                
                clients_rows = datatier.select_n_rows(dbConn, clients_sql, (row[0], year))
                
                # Extract client names from the query result
                clients = [client_row[1] for client_row in clients_rows]

                lobbyist_client = LobbyistClients(
                    Lobbyist_ID=row[0],
                    First_Name=row[1],
                    Last_Name=row[2],
                    Phone=row[3],
                    Total_Compensation=row[4],
                    Clients= clients
                )
                top_lobbyists.append(lobbyist_client)

        return top_lobbyists
    
    except Exception as e:
        print("Error retrieving top lobbyists:", e)
        return []  # Return an empty list if an error occurs

##################################################################
# add_lobbyist_year:
# Inserts the given year into the database for the given lobbyist.
# It is considered an error if the lobbyist does not exist (see below), 
# and the year is not inserted.
# Returns: 1 if the year was successfully added,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).
def add_lobbyist_year(dbConn, lobbyist_id, year):
    initialCheck = "SELECT * FROM LobbyistInfo WHERE Lobbyist_ID = ?"
    results = datatier.select_one_row(dbConn, initialCheck, [lobbyist_id])

    if results is None or results == ():
        return 0
    else:
        updateDB = "INSERT INTO LobbyistYears (Lobbyist_ID, Year) VALUES (?, ?)"
        result = datatier.perform_action(dbConn, updateDB, (lobbyist_id, year))

        if result == -1:
            return 0  # Internal error occurred during insertion
        elif result == 1:
            return 1  # Year successfully added

##################################################################
# set_salutation:
# Sets the salutation for the given lobbyist.
# If the lobbyist already has a salutation, it will be replaced by
# this new value. Passing a salutation of "" effectively 
# deletes the existing salutation. It is considered an error
# if the lobbyist does not exist (see below), and the salutation
# is not set.
# Returns: 1 if the salutation was successfully set,
#          0 if not (e.g. if the lobbyist does not exist, or if
#          an internal error occurred).

def set_salutation(dbConn, lobbyist_id, salutation):
    # Check if the lobbyist exists before updating the salutation
    existenceCheck = "SELECT COUNT(*) FROM LobbyistInfo WHERE Lobbyist_ID = ?"
    exists = datatier.select_one_row(dbConn, existenceCheck, (lobbyist_id,))

    if exists:
        # Lobbyist exists, proceed to update the salutation
        salutationUpdate = "UPDATE LobbyistInfo SET Salutation = ? WHERE Lobbyist_ID = ?"
        result = datatier.perform_action(dbConn, salutationUpdate, (salutation, lobbyist_id))
        if result:
            return 1  # Salutation successfully set
        else:
            return 0  # Lobbyist does not exist

