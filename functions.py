import tkinter
from tkinter import filedialog
import sqlite3
import DeviceUrlList

def run_extract_single_package(deviceid):
    #Folder Selection
    folder_path = filedialog.askdirectory(initialdir="/", title="Select file")


    #Download Driver Package to designated Folder

                    
#Make Entry in Database
def add_new_device(devicename, deviceurl):
    conn = sqlite3.connect("DeviceUrlList.db")
    c = conn.cursor()
    c.execute(""" INSERT INTO DeviceLIst VALUES (:devicename, deviceurl)""",
        {
        "devicename": devicename,
        "deviceurl": deviceurl
       })
    conn.commit()
    conn.close()

#Fetch DeviceList from Database and Format to List for OptionMenu
def fetch_and_format_devices():
    OptionList = []
    try:
        c = sqlite3.connect('DeviceUrlList.db')
        cursor = c.cursor()
        print("Connected to SQLite")

        sqlite_select_query = """SELECT * from DeviceList"""
        cursor.execute(sqlite_select_query)
        list = cursor.fetchall()
        print("Total rows are:  ", len(list))
        print("Printing each row")
        for row in list:
            print("Name: ", row[0])
            print("URL: ", row[1])
            print("\n")

        for row in list:
            OptionList.append(row[0] + " : "+row[1])

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from table", error)
    finally:
        if c:
            c.close()
            print("The Sqlite connection is closed")
    return OptionList


#Reset DeviceList to default
def reset_devicelist_to_default():
    conn = sqlite3.connect("DeviceUrlList.db")
    c = conn.cursor()
    #Delete all Entry in Database
    c.execute("DROP TABLE DeviceList")
    #Set Database to Default DeviceURLList
    sql = "INSERT INTO DeviceList (devicename, deviceurl) VALUES (%s, %s)"
    val = DeviceUrlList.DeviceUrls
    c.executemany(sql, val)
    conn.commit()
    conn.close()

