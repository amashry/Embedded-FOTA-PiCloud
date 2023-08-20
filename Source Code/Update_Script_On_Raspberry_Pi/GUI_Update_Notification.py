#!/usr/bin/python3
    #Modules imported
    #time for delay function sleep
from time import sleep
    #Tkinter for GUI 
from tkinter import *
    #Script file to send hex file
from hexSendBootloader import *
import sys
import os

    #To get environment variable Display
if os.environ.get('DISPLAY','')=='':
    #Set Display Value to 0.0 to make tkinter gui work remoetly
    os.environ.__setitem__('DISPLAY',':0.0')
    #Switch 1 as input here and it's value is send by STM32
switch1=int()  
    #Main window
root = Tk()
    #Title of Main window
root.title('New Firmware Update')
    #size of Main window
root.geometry('450x200')
    #To Disallow Resizing of the window by user
root.resizable(0,0)
    #Top level window 
Top=Toplevel()
    #Top level window hiding
Top.withdraw()

#labels
label_update = Label(root, text='New update is available, please select an action: ',)
label_update.grid(row=0,column=0)
label_update.config(font=("Arial", 15))

#Top level Labels

label_switch1 = Label(Top, text='switch 1 must be off',)
label_switch1.grid(row=0,column=0)
label_switch1.config(font=("Arial", 15))

label_OK = Label(Top, text='OK',)
label_OK.config(font=("Arial", 15))

label_update_in_progress=Label(Top, text='Update in progress',)    
label_update_in_progress.config(font=("Arial", 15))

label_update_finished=Label(Top, text='Update is done',)    
label_update_finished.config(font=("Arial", 15))
#functions
#Function name:update
#function Desc:To be executed when button update on root window is clicked
#and to send hex file after checking on switch1
#No return
#No Argumets

def Update():
    global Top
    global switch1
    #Show Top Level window
    Top.deiconify()
    #size of Top level window
    Top.geometry("500x500")
    #Hide root Main window
    root.withdraw()
    #Send Serially to STM32 'NEW'
    ser.write('N'.encode('utf-8'))
    sleep(0.1)
    ser.write('E'.encode('utf-8'))
    sleep(0.1)
    ser.write('W'.encode('utf-8'))
    sleep(0.1)
    #refresh The toplevel window
    Top.update()
    #Reading Serially Switch 1 to be sent by STM32
    
    string=ser.readline()
    string=string.decode('utf-8')
    print(string)
    if(string=="Switch 1\n"):
  #if swicth 1 string is send then wait for switch 1 value to be sent
        print("hello")
        
        switch1=ser.read()
        print(switch1)
    #if switch 1 is turned off Show button to start update
        if(switch1==b'0'):
            label_OK.grid(row=0,column=5)
            bt_update_now.grid(row=5,column=3)
        elif(switch1!=b'0'):
            label_OK.grid_forget()
            bt_update_now.grid_forget()

#Function name: Snooze
#function Desc:To be executed when button Snooze on root window is clicked
#and to show the update gui back after 10 seconds
#No return
#No Argumets
    
def Snooze():
    global root
    root.withdraw()
    sleep(10)
    root.deiconify()

#Function name: back
#function Desc:To be executed when button back on root window is clicked
#and to notify STM32 with B character for the status of update request
#No return
#No Argumets

def back():
    global Top
    Top.withdraw()
    ser.write('B'.encode('utf-8'))
    root.deiconify()
    ser.reset_input_buffer()
    

#Function name: Reset_Request_then_flash
#function Desc:To be executed when button update_now on Top window is clicked
#and to notify STM32 with 1 character to reset and enter bootloader and then start to send hex file
#After Sending Finish Re-open Script of Getting update from server
#No return
#No Argumets

def Reset_Request_then_flash():
    global bt_update_now
    ser.write('1'.encode('utf-8'))
    label_update_in_progress.grid(row=5,column=0)
    bt_update_now.destroy()
    bt_back.destroy()
    Top.update()
    sleep(5)
    flash()
    label_update_finished.grid(row=7,column=0)
	Top.update()
    sleep(10)
    root.destroy()
    exec(open("/home/pi/Desktop/Update_Script/firebase_Get_Update_Script.py").read())
#buttons on toplevel

bt_back = Button(Top, text='back',font='Arial 10 bold',bg='lightyellow',height=4,width=15,command=back)
bt_back.grid(row=5,column=5)
    


#Buttons
bt_update = Button(root, text='update now',font='Arial 10 bold',bg='lightyellow',height=4,width=15,command=Update)
bt_update.grid(row=1,column=0)

bt_snooze = Button(root, text='snooze',font='Arial 10 bold',bg='light pink',height=4,width=15,command=Snooze)
bt_snooze.grid(row=2,column=0)
bt_update_now = Button(Top, text='update_now',font='Arial 10 bold',bg='lightyellow',height=4,width=15,command=Reset_Request_then_flash)

Top.update()

root.mainloop()

