import sqlite3, hashlib, random, string
from user import user

connection = sqlite3.connect("RolsaTech.db", check_same_thread=False) #Connects to the DB file using SQLITE3 Connections

#Establishing Connection to Database

cur = connection.cursor()

def hash(phrase): #This is a function used to hash a new password
 
    object = hashlib.md5(str(phrase).encode())
    object = object.hexdigest()
 
    return object


def createUser(username, email, password):

    password = hash(password) #Uses the hash function on the password before its executed to the database

    len = 15
    
    id = ''.join(random.choices(string.ascii_letters + string.digits, k=len))


    cur.execute("INSERT INTO Users(ID, Username, Email, Password) VALUES (?,?,?,?)", (id, username, email, password))
    connection.commit()

    


    return user(id, username, email, password)


def checkUser(email,password):

    password = hash(password)

    cur.execute("SELECT * FROM Users WHERE Email = ? AND Password = ?", (email, password))

    return cur.fetchall()

def add_consultation(date, time, quantity):
    id = cur.lastrowid
    cur.execute('INSERT INTO Consultations (ID, consultation_date, time, quantity) VALUES (?, ?, ?, ?)', (id, date, time, quantity))
    connection.commit()
    
    
def add_solar_installation(date, time, quantity):
    id = cur.lastrowid
    cur.execute('INSERT INTO SolarPanelInstallations (ID, installation_date, time, quantity) VALUES (?, ?, ?, ?)', (id, date, time, quantity))
    connection.commit()
    



def viewConsultations():

    # Fetch consultation bookings
    cur.execute('SELECT * FROM Consultations')

    
    return cur.fetchall()

def viewInstallations():
    
    # Fetch installation bookings
    cur.execute('SELECT * FROM SolarPanelInstallations')

    
    return cur.fetchall()

def twoFactorEnabled():

    string1= "True"
    



    cur.execute("INSERT INTO Users (TwoFactorEnabled) VALUES (?)", (string1))
    connection.commit()
   

def twoFactorDisabled():
    string2 = "False"

    cur.execute("INSERT INTO Users (TwoFactorEnabled) VALUES (?)", (string2))
    connection.commit()
    
