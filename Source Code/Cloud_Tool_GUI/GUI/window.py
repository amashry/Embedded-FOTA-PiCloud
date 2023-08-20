'''
 * 
 *
 *  Created on: Feb 15, 2022
 *      Author: Ahmed Ashry
 ''' 


from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("1000x600")

#Background Stuff
window.configure(bg = "#f1f1f1")
canvas = Canvas(
    window,
    bg = "#f1f1f1",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    576.0, 229.5,
    image=background_img)
	


#Entry Browse
entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    744.0, 210.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d4d4d4",
    highlightthickness = 0)

entry0.place(
    x = 580.5, y = 185,
    width = 327.0,
    height = 49)


#Entry Version Number
entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    501.0, 325.5,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d4d4d4",
    highlightthickness = 0)

entry1.place(
    x = 440.5, y = 300,
    width = 121.0,
    height = 49)


#Button Browse 
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 405, y = 171,
    width = 143,
    height = 79)


#Button Upload 
img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 768, y = 300,
    width = 165,
    height = 51)

window.resizable(False, False)
window.mainloop()
