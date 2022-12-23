import sqlite3

conn = sqlite3.connect("DeviceUrlList.db")

c = conn.cursor()


c.execute(""" CREATE TABLE DeviceList (
    devicename text,
    deviceurl text)""")

conn.commit()

conn.close()