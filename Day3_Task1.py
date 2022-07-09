from datetime import datetime
# Before importing pyodbc ensure to install its utilities
# Goto File>Settings>main.py>Python Interpreter>The '+' then search for pyodbc and click Install
# The above are steps to be used for Pycharm IDE
import pyodbc

# microsoft access database connection to store values that need to be accessed at later stages like
# whether a door isclosed or open
# You can change the path after the 'DBQ=' to where the database will be stored on your machine
# The database is included in the file
conn_str = (
    r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
    r'DBQ=C:\Users\Joyce Nakhanu\PycharmProjects\PLPHackathon_Task1Day3\Day3_Task1.accdb;')
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

# function to implement the door commands


def doorFuncs(userCmd):
    global openStamp
    if userCmd == 'open':
        cursor.execute(''' SELECT doorState from Table1 ''')
        storedDoorState = cursor.fetchval()
        if storedDoorState == "Open":
            print('The door is already open!!')
            openStamp = datetime.now()
            print('Door last opened at:', openStamp)
        else:
            openStamp = str(datetime.now())
            cursor.execute('''
            UPDATE Table1 SET doorState = 'Open', openTime= ? WHERE userPassword='0000'
            ''', openStamp)
            cursor.commit()
            print('The door is now open. Time: ', openStamp)

    elif userCmd == 'close':
        cursor.execute(''' SELECT doorState from Table1 ''')
        storedDoorState = cursor.fetchval()
        if storedDoorState == "Locked":
            print('The door is already locked!!')
            cursor.execute(''' SELECT openTime from Table1 ''')
            openStamp = cursor.fetchval()
            print('Door last opened at: ', openStamp)
        else:
            cursor.execute(
                ''' UPDATE Table1 SET doorState = 'Locked' WHERE userPassword='0000' ''')
            cursor.commit()
            print('The door is now locked. Time: ', datetime.now())

    elif userCmd == 'quit':
        exit('Thank you for using the System!!')

    else:
        print('Invalid Input!!!')


# Allowing user to set password then proceed to log in
passWord = int(input("Set a password: "))
userPass = int(input("Enter Password to continue: "))
while userPass != passWord:
    print('Invalid Password!! Try Again')
    userPass = int(input('Password:'))
else:
    print("Welcome to the system")
    userInput = input("Enter command: ")
    doorFuncs(userInput)
