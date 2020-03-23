import pymysql
pymysql.install_as_MySQLdb()
import MySQLdb



from pymongo import MongoClient
#include pprint for readabillity of the 
from pprint import pprint
#change the MongoClient connection string to your MongoDB database instance
client = MongoClient(port=27017)
db=client.proj20DB


#for handling keyboard reactions and pausing
import keyboard  # using module keyboard
import os


"""For menu options 4 and 5 the information should be read from the database only once
Eg If the user choose 4 (View Countries by Name) or 5 (View Countries by Population)
the countries are read from the database and stored in the program.

If the user chooses 4 or 5 again, the information is not read from the database again.
Instead, the information read the first time option 4 or 5 was chosen is used"""


"""
if 'c' not in Countries_By_Name_Dictionary.keys():
    Countries_By_Name_Dictionary['c'] = 300
    # Adding a new key value pair
    Countries_By_Name_Dictionary.update( {'before' : 23} )
""" 





#to store countries by name
Countries_By_Name_Dictionary = {}

#to store countries by population
Countries_By_Population_Dictionary = {}



# Main function
def main():
    # Initialise array
    array = []

    display_menu()


    while True:
        choice = input("Enter choice: ")
            
        if (choice == "1"):
            View_People()
            display_menu()
        elif (choice == "2"):
            View_Countries_By_Independence_Year()
            display_menu()
        elif (choice == "3"):
            Add_New_Person()
            display_menu()
        elif (choice == "4"):
            View_Countries_By_Name()
            display_menu()
        elif (choice == "5"):
            View_Countries_By_Population()
            display_menu()
        elif (choice == "6"):
            Find_Students_By_Address()
            display_menu()
        elif (choice == "7"):
            Add_New_Course()
            display_menu()
        elif (choice == "x"):
            break;
        else:
            display_menu()

def View_People():
    print("Choice 1")
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM person")

    # print all the first cell of all the rows
    count = 0
    for row in cur.fetchall():
        print(row[0],row[1],row[2])
        if (count % 2 == 1):
            os.system("""bash -c 'read -s -n 1 -p "Press any key to continue or q to quit..."'""")
            print("\n")
            if keyboard.is_pressed('q'):  # if key 'q' is pressed
                print('You Pressed q Key!')
                break



        count +=1










    db.close()


def View_Countries_By_Independence_Year():
    print("Choice 2")
    print("Countries_By_Independence_Year")
    print("------------------------------")
    independence_year = input("Enter year:")

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT Name, Continent , IndepYear FROM country WHERE IndepYear = " + independence_year)

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0],row[1],row[2])

    os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")
    print("\n")



    db.close()


def Add_New_Person():

    #to store duplicate name check for adding new people to database
    Duplicate_Name_Check = []
    
    print("Add_New_Person")


    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM person")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        namecheck = row[1]

        Duplicate_Name_Check.insert(0, namecheck)

    db.close()

    """https://pynative.com/python-mysql-insert-data-into-database-table/"""

    
    NewNameForDatabase = input("Name:")

    

   
    while NewNameForDatabase in Duplicate_Name_Check:
        print("*** ERROR ***: " + NewNameForDatabase + " already exists")
        NewNameForDatabase = input("Name:")
 

    
    NewAgeForDatabase = input("Age")


    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    cur.execute("INSERT INTO person(personname,age) VALUES('" + NewNameForDatabase + "'," + NewAgeForDatabase +")")
    db.commit()

    db.close()
   

def View_Countries_By_Name():
    print("Choice 4")
    print("Countries_By_Name")
    print("------------------------------")
    country_name = input("Enter Country Name:")

    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM country WHERE Name LIKE '%" + country_name + "%'")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0],row[1],row[2])

        dictvalue  = []
        dictkey = row[0]
        dictdata1 = row[1]
        dictdata2 = row[2]

        dictvalue.append(dictdata1)
        dictvalue.append(dictdata2)
  
        Countries_By_Name_Dictionary.update({dictkey : dictvalue})
    print("Countries_By_Name_Dictionary")
    print(Countries_By_Name_Dictionary)


    db.close()


def View_Countries_By_Population():
    print("Choice 5")
    print("Countries_By_Population")
    print("-----------------------")


    if len(Countries_By_Population_Dictionary) == 0:
        print("Loading Country Population data from the World database to Python Program dictionary")
 
        db = MySQLdb.connect(host="localhost",    # your host, usually localhost
        user="root",         # your username
        passwd="root",  # your password
        db="world")        # name of the data base

        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        cur = db.cursor()

        # Use all the SQL you like
        cur.execute("SELECT Name, Continent, Population FROM country")

        # print all the first cell of all the rows
        for row in cur.fetchall():


            dictkey = row[2] #Make population dictionary key
            dictdata1 = row[0]
            dictdata2 = row[1]

            """myDict.update( {‘myList’: []} )"""
            
            dictvalue = "[" + dictdata1 + "," + dictdata2 + "]"
            Countries_By_Population_Dictionary.update({dictkey : dictvalue})
        db.close()
        


    denominator = input("Enter <> or = :")
    while denominator != "<" or "<" or "=":
        if denominator == "<":
            break
        elif denominator == ">":
            break
        elif denominator == "=":
            break
        else:
            denominator = input("Enter <> or = :")
            

    country_population = input("Enter population:")



    #Code used to retrieve data from Countries_By_Population_Dictionary

    dictionary_result_count = 0
    
    if denominator == "<":
        for k,v in Countries_By_Population_Dictionary.items():
            if k < int(country_population):
                print(v[0], v[1], k)
                dictionary_result_count += 1

    if denominator == ">":
        for k,v in Countries_By_Population_Dictionary.items():
            if k > int(country_population):
                print(v[0], v[1], k)
                dictionary_result_count += 1

    if denominator == "=":
        for k,v in Countries_By_Population_Dictionary.items():
            if k == int(country_population):
                print(v[0], v[1], k)
                dictionary_result_count += 1


    print("Dictionary Result Count: " , dictionary_result_count)





def Find_Students_By_Address():
    addressquery = input("Input Address:")
    print("RESULTS BY ADDRESS")
    collection  = db.docs
    # Make a query to list all the documents

    for doc in collection.find({"details.address":"" + addressquery + ""}): #just find the records where age 21

        #Print each document

        print(doc)

def Add_New_Course():
    print("Add New Course")
    db = MySQLdb.connect(host="localhost",    # your host, usually localhost
    user="root",         # your username
    passwd="root",  # your password
    db="world")        # name of the data base

    # you must create a Cursor object. It will let
    #  you execute all the queries you need
    cur = db.cursor()

    # Use all the SQL you like
    cur.execute("SELECT * FROM person")

    # print all the first cell of all the rows
    for row in cur.fetchall():
        print(row[0],row[1],row[2])

    db.close()


def display_menu():
    print("World DB")
    print("--------")
    print("MENU")
    print("====")
    print("1 – View People")
    print("2 – View Countries by Independence Year")
    print("3 – Add New Person")
    print("4 – View Countries by name")
    print("5 – View Countries by population")
    print("6 – Find Students by Address")
    print("7 – Add New Course")
    print("x – Exit application")


if __name__ == "__main__":
    # execute only if run as a script
    main()


