# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 18:41:08 2024

@author: sinar
Description: Following program takes temperature input in celcius and converts and displays it in Farenheight
Tkinter GUI toolkit is used
"""

#import tkinter
import tkinter as tk

#create a window
w = tk.Tk()

#Title to the GUI
w.title("Temperature Converter")


#Create a frame widget
frame = tk.Frame(master = w, width = 450, height = 350, relief = 'sunken', borderwidth = 1)
frame.grid(row=0,column=5, padx = 5, pady = 5)

#Label for celsius
label1 = tk.Label(master = frame, text = "Temp in Celsius", bg = 'gray', fg = 'black')
label1.grid(row=0,column=0, padx = 5, pady = 5)

# create an entry widget to get text from user
entryC = tk.Entry(master = frame, fg = 'black', bg = 'white', width = 20)
entryC.grid(row=1,column=0, padx = 5, pady = 5)


#label for farenheight
label2 = tk.Label(master = frame, text = "Temp in Farenheight", bg = 'gray', fg = 'black')
label2.grid(row=0,column=2, padx = 5, pady = 5)

# create an entry widget to get text from user
entryF = tk.Entry(master = frame, fg = 'black', bg = 'white', width = 20)
entryF.grid(row=1,column=2, padx = 5, pady = 5)


def convertCtoF():
        entryF.delete(0, tk.END)             #clear the farenhheight box
        value = (float(entryC.get()) * 9/5) + 32  #read the value of label text
        entryF.insert(0,str(value))      #update the value
    
    
#create a button widget to convert and display
button1 = tk.Button(master = frame, text = '\N{RIGHTWARDS BLACK ARROW}', command = convertCtoF)
button1.grid(row = 2, column = 1, padx = 5, pady = 5)


def convertFtoC():
        entryC.delete(0, tk.END)             #clear the farenhheight box
        value = (float(entryF.get()) -32) * 5/9  #read the value of label text
        entryC.insert(0,str(value))      #update the value
    
    
#create a button widget to convert and display
button2 = tk.Button(master = frame, text = '\N{LEFTWARDS BLACK ARROW}', command = convertFtoC)
button2.grid(row = 3, column = 1, padx = 5, pady = 5)


#run the event loop
w.mainloop()

