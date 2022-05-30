import sqlite3

myConnection = sqlite3.connect('database/dbWTFinance.db')
myCursor = myConnection.cursor()

def createTable():
    myCursor.execute("CREATE TABLE COINS (NAME VARCHAR(10), PRICE VARCHAR(10), PERCENT_CHANGE_24H VARCHAR(10))")

def insertCoins(coins):
    myCursor.executemany("INSERT INTO COINS VALUES (?, ?, ?)", coins)
    myConnection.commit()
    myConnection.close()