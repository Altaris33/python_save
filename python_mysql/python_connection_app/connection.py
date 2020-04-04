# python program to test db connection
#use_pure=False -> use of C implementation of Connector/Python use_pure=True -> use of Python implementation

import mysql.connector
from mysql.connector import errorcode

try:
    connection_var = mysql.connector.connect(user='root', password='password', host='127.0.0.1', database='characters', use_pure=True)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Sorry, something went wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Sorry, it seems the requested database does not exist.")
    else:
        print(err)
else:                
    connection_var.close()

# CREATING A TABLE
# engine used for storing data: innoDB
DB_NAME = 'characters'

TABLES = {}
TABLES['characters'] = (
    "CREATE TABLE `pirates` ("
    "`pirate_id` int(11) NOT NULL AUTO_INCREMENT,"
    "`name` varchar(40) NOT NULL,"
    "`bounty` decimal(19) NOT NULL,"
    "`ability` varchar(40),"
    " PRIMARY KEY (`pirate_id`)"
    ") ENGINE=InnoDB"
)



