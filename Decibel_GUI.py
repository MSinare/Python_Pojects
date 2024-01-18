# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 12:20:59 2024

@author: sinar
Description: Following code is designed to convert DB to Voltage Gain and Power Gain, to and from
It also includes a link to a webpage for information related to the dB to gain conversion
"""

#import tkinter
import tkinter as tk
#import a webbrowser module
import webbrowser
#importa math module
import math

#create a window
w = tk.Tk()

#Title to the GUI
w.title("Decibel Converter")


#Define a callback function with a weblink
def callback():
   webbrowser.open_new_tab("https://ece.northeastern.edu/courses/eece2150/2017fa/supplementary/db.pdf")


#create a button widget to open the information link
button1 = tk.Button(master = w, text = 'Related Information', command = callback)
button1.grid(row = 3, column = 1, padx = 5, pady = 5)


#Label for Decibels
label1 = tk.Label(master = w, text = "Gain in Decibels", fg = 'black')
label1.grid(row=0,column=0, padx = 5, pady = 5)

# create an entry widget to get Decibel and Display Decibels
entryD = tk.Entry(master = w, fg = 'black', bg = 'white', width = 20)
entryD.grid(row=1,column=0, padx = 5, pady = 5)

# create an entry widget to get Gain and Display Decibels
entryP = tk.Entry(master = w, fg = 'black', bg = 'white', width = 20)
entryP.grid(row=1,column=2, padx = 5, pady = 5)


#create a callback function to convert decibels to Gain
def convertDtoG():
        entryP.delete(0, tk.END)             #clear the gain box
        if (clicked.get() == "Power Gain"):
            value = (10**(float(entryD.get())/10))  #read the value of entry widget for decibel
        else:
            value = (10**(float(entryD.get())/20))  #read the value of entry widget for decibel
        entryP.insert(0,str(value))      #update the value
        
        
#create a callback function to convert Gain to Decibels
def convertGtoD():
        entryD.delete(0, tk.END)             #clear the decibels box
        if (clicked.get() == "Power Gain"):
            value = (10*math.log10(float(entryP.get())))  #read the value of entry widget for gain
        else:
            value = (20*math.log10(float(entryP.get())))  #read the value of entry widget for gain
        entryD.insert(0,str(value))      #update the value
    
    
#create a button widget to convert decibel to gain and display
button2= tk.Button(master = w, text = '\N{RIGHTWARDS BLACK ARROW}', command = convertDtoG)
button2.grid(row = 1, column = 1, padx = 5, pady = 2)

#create a button widget to convert gain to decibels and display
button3 = tk.Button(master = w, text = '\N{LeftWARDS BLACK ARROW}', command = convertGtoD)
button3.grid(row = 2, column = 1, padx = 5, pady = 2)

# Dropdown menu options 
options = [ 
    "Power Gain", 
    "Voltage Gain"
    
] 
  
# datatype of menu text 
clicked = tk.StringVar() 
  
# initial menu text 
clicked.set( "Power Gain" ) 
  
# Create Dropdown menu 
drop = tk.OptionMenu( w , clicked , *options ) 
drop.grid(row = 0, column = 2) 



#run the event loop
w.mainloop()