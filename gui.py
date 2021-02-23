#importing tkinter and functions from requestfiles
import tkinter as tk
from reqfiles import loadjson, makeList

#making master window
root = tk.Tk()
master = tk.Canvas(root, width = 600, height = 500)
master.pack()
root.title("Currency Converter")

#accepting input for dropdown window
def key_in(event):
    ch=event.char.upper()

#takingin key, and getting the rate
def takeininp(arg):
    global inpcurr
    inpcurr = 0.0
    global inrate
    data = loadjson()
    for key,value in data.items():
        if key == arg.lower():
            inrate = value['name']
            inpcurr = value['rate']

#takingin key, and getting the rate for output currency
def takeinoutp(arg):
    global outpcurr
    outpcurr = 0.0 
    global outrate 
    data = loadjson()
    for key,value in data.items():
        if key == arg.lower():
            outrate = value['name']
            outpcurr = value['rate']

#validating integer commands for entry box and outputting value
def convertCurrency():
    try:
        if inpcurr == 0.0 or outpcurr == 0.0:
            outputlabel = tk.Label(root, text = "Currency has not been selected")
        else:
            x1 = entry1.get()
            if x1.isnumeric():
                value = float(x1)
                val = value * (outpcurr/inpcurr)
                strval = "{:.3f}".format(val)
                text = str(value) + " " + inrate + "s are equal to " + strval + " " + outrate + "s."
                outputlabel = tk.Label(root, text = text)
            else:
                outputlabel = tk.Label(master, text = "Invalid input. Please try again")
    except:
        outputlabel = tk.Label(root, text = "Please enter all values correctly.")
    finally:
        master.create_window(300,250,window = outputlabel)

#-------------------------------------------------------------
#creating a title
title = tk.Label(root, 
		 text="Welcome to the Currency Converter!",
		 fg = "dark blue",
		 font = "Helvetica 20 bold italic")
master.create_window(300, 50, window = title)
#-------------------------------------------------------------

#------------------------------------------------------------
#input currency widget
#value holder for input 
variable = tk.StringVar(master)
#getting the list that holds currencies
options=makeList()
#creating the option menu in master, using variable and list, and doing take in on accepting
incurr=tk.OptionMenu(master, variable, *options, command = takeininp)
master.create_window(300,150,window = incurr)
#setting default to choose your variable
variable.set("Choose input Currency")

#binding and focussing
incurr.bind('<Key>', key_in)
incurr.focus_set()
#-------------------------------------------------------------------

#------------------------------------------------------------
#output currency widget
#value holder for output 
variable2 = tk.StringVar(master)
#creating the option menu in master, using variable and list, and doing take in on accepting
outcurr=tk.OptionMenu(master, variable2, *options, command = takeinoutp)
master.create_window(300,175,window = outcurr)
#setting default to choose your variable
variable2.set("Choose output currency")
#binding and focussing
outcurr.bind('<Key>', key_in)
outcurr.focus_set()
#-------------------------------------------------------------------

#-------------------------------------------------------------
#entry value widget
entry1 = tk.Entry(root)
master.create_window(300,200,window = entry1)
#-------------------------------------------

#-------------------------------------------------------------
#output widget
#making a button
try:
    calcbutton = tk.Button(text = "Calculate value.", command = convertCurrency)
    master.create_window(300,225,window = calcbutton)
except:
    label2 = tk.Label(master, text = "Please enter your values.")
#-------------------------------------------

#--------------------------------------------------------
#to exit the window
exitbutton = tk.Button(master, text="Exit", fg="dark red",command=master.quit)
master.create_window(300,275,window = exitbutton)
#---------------------------------------------------------

#calling masterloop to run tkinter window
master.mainloop()