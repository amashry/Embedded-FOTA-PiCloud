#===========================================================#
#	Imported Liberaries										#
#	You can choose from tkinter import *					#
#	I only imported some functions from tkinter				#
#	seperatly because of error messages						#
#	Author : Mahmoud and Ahmed								#
#===========================================================#
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyrebase

#===========================================================#
#	A dictionary for cloud server project configuration		#
#===========================================================#
config = {
 "apiKey": "AIzaSyDbI-O-xVXjs0QuQWo0MpcXZdYE4a8MmAs",
  "authDomain": "fota-ebe0a.firebaseapp.com",
  "databaseURL": "https://fota-ebe0a-default-rtdb.firebaseio.com",
  "projectId": "fota-ebe0a",
  "storageBucket": "fota-ebe0a.appspot.com",
  "serviceAccount":"privatekey.json",
  "messagingSenderId": "1056175280604",
  "appId": "1:1056175280604:web:02f91b65ffe904abd0ff19",
  "measurementId": "G-QRVSKDM3E7"
}

#===================================================================#
#	Initializing cloud server project app and link it to python		#
#	Defining variable in which I saved firebse referrence in		#
#===================================================================#
Firebase = pyrebase.initialize_app(config)

#===================================================================#
#	A variable for cloud server project storage referrence			#
#===================================================================#
Storage = Firebase.storage()

#===================================================================#
#	A variable for referrence to project realtime database			#
#===================================================================#
Database = Firebase.database()

#===========================================================#
#	A variable for cloud server project folders path		#
#===========================================================#
Cloud_Path = "Files/Update.hex"

#===========================================================#
#	A function to create a file dialog for file browsing	#
#	None return function type								#
#	Takes no arguments										#
#===========================================================#
def Browse():
	
	main_window.filename = filedialog.askopenfilename(initialdir = "/", title = "Browse Your File", filetypes = (("all files", "*.*"), ("hex files", "*.hex")))
	
	Local_Path.set(main_window.filename)
#===========================================================#
#	A function to upload hex file to server					#
#	None return function type								#
#	Takes no arguments										#
#===========================================================#
def Upload():
	#===========================================================#
	#	Variable to save the local path in it					#
	#===========================================================#
	Local_Path_var = ""
	#===========================================================#
	#	Variable to save the version value in it				#
	#===========================================================#
	Version_Number_var = 0
	#===========================================================#
	#	"get" A function to get the enterd string in entry		#
	#	Assigning the local path to variable					#
	#===========================================================#	
	Local_Path_var = Local_Path.get()
	#===========================================================#
	#	Casting the version value to integer					#
	#	Assigning the version value to the variable				#
	#===========================================================#	
	Version_Number_var = int(Version_Number.get())
	#===========================================================#
	#	"child" A function to create a database child			#
	#	None return function type								#
	#	Takes string											#
 	#															#
	#	"set" is a function to set the value of the child		#
	#	None return function type								#
	#	Takes child value										#
	#===========================================================#
	Database.child("version").set(Version_Number_var)
	
	Storage.child(Cloud_Path).put(Local_Path_var)
	Message_Text = ""
	if Database.child("version").get().val() == Version_Number_var:
		#Lable Upload complete font = 10, times new roman
		label_Successful_Update.place(x = 500, y = 400)
		label_UnSuccessful_Update.forget()
	else :
		#Lable Error please upload again font = 10, times new roman
		label_UnSuccessful_Update.place(x = 500, y = 400)
		label_Successful_Update.forget()
#=======================================#
#	Creating the GUI Window				#
#=======================================#
main_window = tk.Tk()
main_window.geometry("1000x600+200+200")
main_window.iconphoto(False, PhotoImage(file = "Upload.png"))
main_window.title("FOTA Cloud Server")
main_window.configure(bg = "#f1f1f1")
main_window.resizable(False, False)



#=======================================#
#	Background Stuff					#
#=======================================#
Background_Image_Path = PhotoImage(file = "Background.png")

Background = Canvas(main_window, bg = "#f1f1f1", height = 600, width = 1000,
				bd = 0, highlightthickness = 0, relief = "ridge")
Background.place(x = 0, y = 0)

Background.create_image( 576.0, 229.5, image = Background_Image_Path)
#=======================================#
#Creating labels for Upload result		#
#=======================================#
label_Successful_Update = Label(Background,bg="#f1f1f1", text='New update is Successfully Uploaded ',)
label_Successful_Update.config(font=("Times Roman", 15))

label_UnSuccessful_Update = Label(Background,bg="#f1f1f1", text='New update is Successfully Uploaded ',)
label_UnSuccessful_Update.config(font=("Times Roman", 15))

#=======================================#
#	Local Path Entry					#
#=======================================#
Local_Path = tk.StringVar()
Path_Entry_Image = PhotoImage(file = "LocalPathEntry.png")
Path_Entry_Background = Background.create_image(744.0, 210.5, image = Path_Entry_Image)
Path_Entry = tk.Entry(bd = 0, bg = "#d4d4d4", textvariable = Local_Path,
					  highlightthickness = 0)
Path_Entry.place(x = 580.5, y = 185, width = 327.0, height = 49)

#=======================================#
#	Version Number Entry				#
#=======================================#
Version_Number = tk.StringVar()
Version_Entry_Image = PhotoImage(file = "VersionEntryImage.png")
Version_Entry_Background = Background.create_image(501.0, 325.5, image = Version_Entry_Image)
Version_Entry = tk.Entry(bd = 0, bg = "#d4d4d4", textvariable = Version_Number,
						 highlightthickness = 0)
Version_Entry.place(x = 440.5, y = 300, width = 121.0, height = 49)

#=======================================#
#	Browse Button						#
#=======================================#
Browse_Button_Image = PhotoImage(file = "BrowseButton.png")
Browse_Button = tk.Button(image = Browse_Button_Image, borderwidth = 0,
						  highlightthickness = 0, command = Browse,
						  relief = "flat")

Browse_Button.place(x = 405, y = 171, width = 143, height = 79)

#=======================================#
#	Upload Button						#
#=======================================#
Upload_Button_Image = PhotoImage(file = "UploadButton.png")

Upload_Button = tk.Button(image = Upload_Button_Image, borderwidth = 0,
						  highlightthickness = 0, command = Upload,
						  relief = "flat")

Upload_Button.place(x = 768, y = 300, width = 165, height = 51)

main_window = tk.mainloop()