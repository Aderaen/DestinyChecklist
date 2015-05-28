'''
Created on 2015-05-28

@author: Alexandre
'''

from tkinter import *
import os.path
from tkinter.tix import COLUMN


def createWindow(paddingX,paddingY):
    window = Tk()
    window.title("Destiny Checklist")
    window.geometry("900x600")
    configureGrid(window,3,5,paddingX,paddingY)
    return window


def fillWindow(window,buttonsList):
    fillCharacter(window,buttonsList,0)
    fillCharacter(window,buttonsList,1)
    fillCharacter(window,buttonsList,2)
    
def fillCharacter(window,buttonsList,columnValue):
    label = LabelFrame(window,text="Weekly Strikes")
    configureGrid(label,2,1,25,0)
    addButton(label,buttonsList,"Weekly Heroic Strike",column=columnValue,row=0)
    addButton(label,buttonsList,"Weekly Nightfall Strike",column=columnValue,row=0)
    label.grid(column=columnValue,row=0)
    
    addButton(window,buttonsList,"Oracles",column=columnValue,row=1)
    addButton(window,buttonsList,"Templar",column=columnValue,row=1)
    addButton(window,buttonsList,"Gorgons",column=columnValue,row=1)
    addButton(window,buttonsList,"Gatekeeper",column=columnValue,row=1)
    addButton(window,buttonsList,"Atheon",column=columnValue,row=1)
    
def addButton(window,buttonsList,name,**options):
    button = Button(window,text=name)
    button.grid(options)
    buttonsList.append(button)
    
def configureGrid(frame,columns,rows,paddingX,paddingY):
    column = 0
    while column < columns:
        frame.columnconfigure(column,pad=paddingX)
        row = 0
        while row < rows:
            frame.rowconfigure(row,pad=paddingY)
            row += 1
        column += 1

window = createWindow(250, 25)
buttonsList = []
fillWindow(window,buttonsList)
window.mainloop()