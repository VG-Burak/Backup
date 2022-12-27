import tkinter
import customtkinter
from tkinter import filedialog
import functions
from tkinter import ttk

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("750x500")

#Creating Tabs
tabControl = customtkinter.CTkTabview(app, width=app.winfo_screenwidth(), height=app.winfo_screenheight())

tabMain = tabControl.add("tabMain")
tabEntry = tabControl.add("tabEntry")

tabControl.pack(expand = 1, fill ="both")
#Fetch Data from Database for OptionMenu and ListBox


#Tab Main
Button_one_Device = customtkinter.CTkButton(tabMain, text="Run and Extract",command= lambda : functions.run_extract_single_package(selected_device.get()))
Button_one_Device.grid(pady=10, padx=10)

selected_device = tkinter.StringVar(app)

formatedDeviceList = functions.fetch_and_format_devices()

Dropdown_all_Devices = customtkinter.CTkOptionMenu(tabMain, values=formatedDeviceList)
Dropdown_all_Devices.grid(pady=10, padx=10)



#Tab Entry
#Label for Entry
Label_devicename = customtkinter.CTkLabel(tabEntry, text="Device Name")
Label_devicename.grid(row=0, column=0, padx=60)

Label_deviceurl = customtkinter.CTkLabel(tabEntry, text="Device Url")
Label_deviceurl.grid(row=1, column=0,padx=10)

#Entry for Database 
Entry_devicename = customtkinter.CTkEntry(tabEntry, width=300)
Entry_devicename.grid(row=0, column=1,padx=20)

Entry_deviceurl = customtkinter.CTkEntry(tabEntry, width=300)
Entry_deviceurl.grid(row=1, column=1,padx=20)

#Submit Button to Add Device
Entry_submit_Button = customtkinter.CTkButton(tabEntry, text="Submit", width=150)
Entry_submit_Button.grid(row=1, column=2, padx=20)

#Reset to Default Button
Entry_reset_to_default = customtkinter.CTkButton(tabEntry, text="Reset to Default Device List", width = 150)
Entry_reset_to_default.grid(row=4, column=1, padx=20)

#Divide Element
Entry_divide_element = customtkinter.CTkFrame(tabEntry, width=450, height=10)
#Entry_divide_element.grid(row=2, column=1, padx=20)

#ListBox for Device Entries
langs = ('Java', 'C#', 'C', 'C++', 'Python',
         'Go', 'JavaScript', 'PHP', 'Swift')

var = tkinter.Variable(value=formatedDeviceList)
Entry_listbox = tkinter.Listbox(tabEntry, listvariable=var, height=20, width=100,
    selectmode=tkinter.EXTENDED
)

Entry_listbox.grid(row=3, column=0, pady=20, columnspan=3)

app.mainloop()