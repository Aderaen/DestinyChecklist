'''
Created on 2015-05-28

@author: Alexandre
'''

from tkinter import Tk, Label, LabelFrame, Button, PhotoImage
from tkinter.constants import FALSE
import base64
import os.path
import requests

def createWindow(paddingX,paddingY):
    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.iconbitmap("Icon.ico")
    window.title("Destiny Checklist")
    window.config(bg="#85A0D7")
    configureGrid(window,3,6,paddingX,paddingY)
    return window

def fillWindow(window,buttonsList):
    ## Gets the image url from Bungie
    #url = "https://www.bungie.net/platform/destiny/advisors/?definitions=true"
    #request = requests.get(url, \
    #          headers={'X-API-Key':'8147443ac3d64b238d680f89b912e285'})
    #json = request.json()
    #activityHash = str(json['Response']['data']['nightfallActivityHash'])
    #image = json['Response']['definitions']['activities'][activityHash]['pgcrImage']
    #url = "https://www.bungie.net"+image
    #request = requests.get(url, stream=True)
    
    ## Saves the image to a file (works)
    #f = open(os.path.expanduser('~/DestinyChecklist.jpg'), 'wb')
    #f.write(request.content)
    #f.close()
    
    ## Tries to display the image (doesn't work)
    #image = base64.encodestring(request.content)
    #backgroundImage = PhotoImage(data=request.content)
    #background_label = Label(window, image=backgroundImage)
    #background_label.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Fill each character
    fillCharacter(window,buttonsList,0)
    fillCharacter(window,buttonsList,1)
    fillCharacter(window,buttonsList,2)
    
    # Save button at the end
    addButton(window,buttonsList,1,21,["Save"],column=1,row=5)
    changeButtonCommand(getLastButton(buttonsList),lambda:save(buttonsList))
    
def fillWeekly(window,buttonsList,columnValue):
    label = LabelFrame(window,text="Weekly Strikes")
    label.config(bg=window["background"])
    configureGrid(label,2,1,25,25)
    addButton(label,buttonsList,1,21,["Weekly Heroic Strike", \
                                      "Weekly Heroic Strike (26)", \
                                      "Weekly Heroic Strike (30)", \
                                      "Weekly Heroic Strike (32)"], \
              column=0,row=0)
    addButton(label,buttonsList,1,21,["Weekly Nightfall Strike", \
                                      "Weekly Nightfall Strike"], \
              column=1,row=0)
    label.grid(column=columnValue,row=1)
    
def fillVaultOfGlass(window,buttonsList,columnValue):
    label = LabelFrame(window,text="Vault of Glass")
    label.config(bg=window["background"])
    configureGrid(label,3,2,25,25)
    addButton(label,buttonsList,1,12,["Oracles", \
                                      "Oracles (N)", \
                                      "Oracles (H)"], \
              column=0,row=0)
    addButton(label,buttonsList,1,12,["Templar", \
                                      "Templar (N)", \
                                      "Templar (H)"], \
              column=1,row=0)
    addButton(label,buttonsList,1,12,["Gorgons", \
                                      "Gorgons (N)", \
                                      "Gorgons (H)"], \
              column=2,row=0)
    addButton(label,buttonsList,1,12,["Gatekeeper", \
                                      "Gatekeeper (N)", \
                                      "Gatekeeper (H)"], \
              column=0,row=1)
    addButton(label,buttonsList,1,12,["Atheon", \
                                      "Atheon (N)", \
                                      "Atheon (H)"], \
              column=2,row=1)
    label.grid(column=columnValue,row=2)
    
def fillCrotasEnd(window,buttonsList,columnValue):
    label = LabelFrame(window,text="Crota's End")
    label.config(bg=window["background"])
    configureGrid(label,2,2,25,25)
    addButton(label,buttonsList,1,21,["Abyss", \
                                      "Abyss (N)", \
                                      "Abyss (H)"], \
              column=0,row=0)
    addButton(label,buttonsList,1,21,["Bridge", \
                                      "Bridge (N)", \
                                      "Bridge (H)"], \
              column=1,row=0)
    addButton(label,buttonsList,1,21,["Deathsinger", \
                                      "Deathsinger"], \
              column=0,row=1)
    addButton(label,buttonsList,1,21,["Crota", \
                                      "Crota (N)", \
                                      "Crota (H)"], \
              column=1,row=1)
    label.grid(column=columnValue,row=3)
    
def fillPrisonOfElders(window,buttonsList,columnValue):
    label = LabelFrame(window,text="Prison of Elders")
    label.config(bg=window["background"])
    configureGrid(label,2,2,25,25)
    addButton(label,buttonsList,1,21,["Level 32 Challenge", \
                                      "Level 32 Challenge"], \
              column=0,row=0)
    addButton(label,buttonsList,1,21,["Level 34 Challenge", \
                                      "Level 34 Challenge"], \
              column=1,row=0)
    addButton(label,buttonsList,1,21,["Skolas's Revenge", \
                                      "Skolas's Revenge"], \
              column=0,row=1)
    addButton(label,buttonsList,1,21,["Weekly Queen's Chest", \
                                      "Weekly Queen's Chest"], \
              column=1,row=1)
    label.grid(column=columnValue,row=4)
    
def fillCharacter(window,buttonsList,columnValue):
    # Character identifier
    charText = "Character "+str(columnValue+1)
    label = Label(window,font=("serif",18),text=charText)
    label.config(bg=window["background"])
    label.grid(column=columnValue,row=0)
    
    # Start filling the main grid with subsections
    fillWeekly(window,buttonsList,columnValue)
    fillVaultOfGlass(window,buttonsList,columnValue)
    fillCrotasEnd(window,buttonsList,columnValue)
    fillPrisonOfElders(window,buttonsList,columnValue)
    
def addButton(window,buttonsList,heightValue,widthValue,states,**options):
    button = Button(window,font=("serif",8),
                    relief="flat",highlightbackground="#CCCCCC", \
                    height=heightValue,width=widthValue,text=states[0], \
                    command=lambda:changeButtonState(button))
    button.grid(options)
    buttonsList[0].append(button)
    length = len(buttonsList[0])
    if len(buttonsList[1]) < length:
        buttonsList[1].append(states)
        buttonsList[2].append(0)
    else:
        buttonsList[1][length - 1] = states
        state = buttonsList[2][length - 1]
        button.config(text=states[state])
        changeButtonBackground(button,state,len(buttonsList[1][length - 1]))
        
def getLastButton(buttonsList):
    return buttonsList[0][len(buttonsList[0]) - 1]
        
def changeButtonCommand(button,callback):
    button.config(command=callback)
    
def changeButtonBackground(button,state,length):
    if state == 0:
        button.config(bg=getDefaultBackground())
    elif state == length - 1:
        button.config(bg=getCompletedBackground())
    else:
        button.config(bg=getStartedBackground())
    
def configureGrid(frame,columns,rows,paddingX,paddingY):
    column = 0
    while column < columns:
        frame.columnconfigure(column,pad=paddingX)
        row = 0
        while row < rows:
            frame.rowconfigure(row,pad=paddingY)
            row += 1
        column += 1
        
def changeButtonState(button):
    index = buttonsList[0].index(button)
    names = buttonsList[1][index]
    length = len(names)
    state = buttonsList[2][index]
    state += 1
    state %= length
    changeButtonBackground(button,state,length)
    button.config(text=names[state])
    buttonsList[2][index] = state

def save(buttonsList):
    file = open(getConfigPath(),"w")
    length = len(buttonsList[0])
    index = 0
    while index < length - 1:
        file.write(buttonsList[1][index][0]+":"+str(buttonsList[2][index])+"\n")
        index += 1

def load(buttonsList):
    if os.path.isfile(getConfigPath()):
        file = open(getConfigPath(),"r")
        for line in file:
            values = line.split(':')
            buttonsList[1].append(values[0])
            buttonsList[2].append(int(values[1]))

def getConfigPath():
    return os.path.expanduser('~/DestinyChecklist.cfg')

def getDefaultBackground():
    return "#FFFFFF"

def getStartedBackground():
    return "#FFFF00"

def getCompletedBackground():
    return "#00FF00"

window = createWindow(25, 25)
buttonsList = [[],[],[]]
load(buttonsList)
fillWindow(window,buttonsList)
window.mainloop()