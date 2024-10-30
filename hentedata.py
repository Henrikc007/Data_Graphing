
import pandas as pd
import hemmeligefiler
#herunder skal der indsættes ip adresse og kode til lokale sql server
ipadresse = "dinIpAdresse"
brugernavn ="root"
brugerpw = "hemmeligkode"
mindatabase = "northwind"
#connecte til lokal server og lave mysql dataarbejde på denne

#jeg skal lave secret fil, hvor mine koder er indlejret


import mysql.connector
from mysql.connector import Error

# Function to create a connection
def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password,
            database=db_name
        )
        print("Connection successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

#en funktion som henter data fre en kolonne og returnere dem i en array
def fetchDataframe(whatTable,whatColoumn):    
    nortwindConn=create_connection(ipadresse,brugernavn,brugerpw,mindatabase)
    cursor = nortwindConn.cursor()
    if whatColoumn == "ALL":
        enQuery = "select * from "
        enQuery = enQuery + whatTable
    else:
        #snyder en select disticnt istedet fror at lave mit eget valg af sql query
        enQuery = "select distinct " + whatColoumn + " from " + whatTable
        
    result_dataframe = pd.read_sql(enQuery,nortwindConn)
    cursor.close()
    nortwindConn.close()
    return result_dataframe


def fetchDataframeRestraint(whatTable,whatColoumn, whatrestraint):
    nortwindConn=create_connection(ipadresse,brugernavn,brugerpw,mindatabase)
    cursor = nortwindConn.cursor()
    enQuery = "select * from "
    enQuery = enQuery + whatTable
    result_dataframe = pd.read_sql(enQuery,nortwindConn)
    cursor.close()
    nortwindConn.close()
    return result_dataframe






