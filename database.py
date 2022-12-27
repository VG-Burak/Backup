import sqlite3
import DeviceUrlList

conn = sqlite3.connect("DeviceUrlList.db")

c = conn.cursor()


sql = "INSERT INTO DeviceList (devicename, deviceurl) VALUES (?, ?)"
val = DeviceUrlList.DeviceUrls

c.executemany(sql,val)

conn.commit()

conn.close()