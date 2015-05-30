"""
Destiny Checklist is a simple utility for 
tracking your game progression manually

Created on 2015-05-26

@author: Alexandre
"""

from tkinter import Tk, Label, LabelFrame, Button, Widget
from tkinter.constants import FALSE
import os.path
import requests

def createWindow(paddingX,paddingY):
    """ Creates the window with a grid layout
    
    paddingX: Horizontal padding of the window
    paddingY: Vertical padding of the window
    
    returns the window
    """
    window = Tk()
    window.resizable(width=FALSE, height=FALSE)
    window.iconbitmap("Icon.ico")
    window.title("Destiny Application")
    window.config(bg="#85A0D7")
    configureGrid(window,3,6,paddingX,paddingY)
    return window

def fillWindow(window,buttonsList):
    """ Fills the window with each character
    
    window: The window to fill
    buttonsList: The buttons to keep track of
    """
    heroicLevels = getHeroicLevels()
    # Fill each character
    fillCharacter(window,buttonsList,heroicLevels,0)
    fillCharacter(window,buttonsList,heroicLevels,1)
    fillCharacter(window,buttonsList,heroicLevels,2)
    # Save button at the end
    addButton(window,buttonsList,1,21,["Save"],column=1,row=5)
    changeButtonCommand(getLastButton(buttonsList), \
                        lambda:save(getLastButton(buttonsList),buttonsList))
    
def fillWeekly(window,buttonsList,heroicLevels,columnValue):
    """ Puts the weekly section
    
    window: The window to contain the section
    buttonsList: The buttons to keep track of
    heroicLevels: The different activity levels to display
    columnValue: The column of the character
    """
    label = LabelFrame(window,text="Weekly Strikes")
    label.config(bg=window["background"])
    configureGrid(label,2,1,25,25)
    addButton(label,buttonsList,1,21, \
              ["Weekly Heroic Strike", \
               "Weekly Heroic Strike ("+heroicLevels[0]+")", \
               "Weekly Heroic Strike ("+heroicLevels[1]+")", \
               "Weekly Heroic Strike ("+heroicLevels[2]+")"], \
              column=0,row=0)
    addButton(label,buttonsList,1,21,["Weekly Nightfall Strike", \
                                      "Weekly Nightfall Strike"], \
              column=1,row=0)
    label.grid(column=columnValue,row=1)
    
def fillVaultOfGlass(window,buttonsList,columnValue):
    """ Puts the Vault of Glass section
    
    window: The window to contain the section
    buttonsList: The buttons to keep track of
    columnValue: The column of the character
    """
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
    """ Puts the Crota's End section
    
    window: The window to contain the section
    buttonsList: The buttons to keep track of
    columnValue: The column of the character
    """
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
    """ Puts the Prison of Elders section
    
    window: The window to contain the section
    buttonsList: The buttons to keep track of
    columnValue: The column of the character
    """
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
    
def fillCharacter(window,buttonsList,heroicLevels,columnValue):
    """ Fills the character inside the window
    
    window: The window to contain the character
    buttonsList: The buttons to keep track of
    heroicLevels: The different activity levels to display
    columnValue: The column of the character
    """
    # Character identifier
    charText = "Character "+str(columnValue+1)
    label = Label(window,font=("serif",18),text=charText)
    label.config(bg=window["background"])
    label.grid(column=columnValue,row=0)
    
    # Start filling the main grid with subsections
    fillWeekly(window,buttonsList,heroicLevels,columnValue)
    fillVaultOfGlass(window,buttonsList,columnValue)
    fillCrotasEnd(window,buttonsList,columnValue)
    fillPrisonOfElders(window,buttonsList,columnValue)
    
def addButton(window,buttonsList,heightValue,widthValue,states,**options):
    """ Adds a button to the window
    
    window: The window in which to add the button
    buttonsList: The list of all buttons
    heightValue: The height of the button
    widthValue: The width of the button
    states: The possible names of the button
    **options: Grid positioning options
    """
    if not isinstance(window, Tk) and not isinstance(window, Widget):
        raise TypeError('The window must be an instance of Tkinter')
    if not len(states) > 0:
        raise ValueError('The button must have at least one state')
    button = Button(window,font=("serif",8),
                    relief="flat",highlightbackground="#CCCCCC", \
                    height=heightValue,width=widthValue,text=states[0], \
                    command=lambda:changeButtonState(button,buttonsList))
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
    """ Returns the last added button
    
    buttonsList: The list to fetch
    
    returns the last button in the list
    """
    return buttonsList[0][len(buttonsList[0]) - 1]
        
def changeButtonCommand(button,callback):
    """ Changes the callback method of a button
    
    button: The button to modify
    callback: The method to call instead
    """
    button.config(command=callback)
    
def changeButtonBackground(button,state,length):
    """ Changes the background color of the button
    
    button: The button to modify
    state: The state's numeric identifier
    length: The total number of states
    """
    if state == 0:
        button.config(bg=getDefaultBackground())
    elif state == length - 1:
        button.config(bg=getCompletedBackground())
    else:
        button.config(bg=getStartedBackground())
    
def configureGrid(frame,columns,rows,paddingX,paddingY):
    """ Creates a grid from a set number of columns and rows
    
    frame: The frame in which to create the grid
    columns: The number of columns
    rows: The number of rows
    paddingX: Horizontal padding of the cells
    paddingY: Vertical padding of the cells
    """
    column = 0
    while column < columns:
        frame.columnconfigure(column,pad=paddingX)
        row = 0
        while row < rows:
            frame.rowconfigure(row,pad=paddingY)
            row += 1
        column += 1
        
def changeButtonState(button,buttonsList):
    """ Changes the state of the button
    
    button: The button to modify
    """
    index = buttonsList[0].index(button)
    names = buttonsList[1][index]
    length = len(names)
    state = buttonsList[2][index]
    state += 1
    state %= length
    changeButtonBackground(button,state,length)
    button.config(text=names[state])
    buttonsList[2][index] = state

def save(button,buttonsList):
    """ Saves all buttons to a file
    
    button: The current save button
    buttonsList: A list of all the buttons
    """
    os.makedirs(getConfigPath(), exist_ok=True)
    file = open(getConfigPath()+"values.cfg","w")
    length = len(buttonsList[0])
    index = 0
    while index < length - 1:
        file.write(buttonsList[1][index][0]+ \
                   ":"+ \
                   str(buttonsList[2][index])+ \
                   "\n")
        index += 1

def load(buttonsList):
    """ Loads saved buttons from a file
    
    buttonsList: the list of buttons to fill
    """
    if os.path.isfile(getConfigPath()+"values.cfg"):
        file = open(getConfigPath()+"values.cfg","r")
        for line in file:
            values = line.split(':')
            buttonsList[1].append(values[0])
            buttonsList[2].append(int(values[1]))
            
def getHeroicLevels():
    """ Returns the weekly activity levels from Bungie
    
        Inspired by dinklebot.net : https://github.com/BinarMorker/Dinklebot
     """
    url = "https://www.bungie.net/platform/destiny/advisors/?definitions=true"
    request = requests.get(url, \
              headers={'X-API-Key':'8147443ac3d64b238d680f89b912e285'})
    json = request.json()
    activityHashes = json['Response']['data']['heroicStrikeHashes']
    easyHeroicLevel = json['Response']['definitions']['activities']\
                          [str(activityHashes[0])]['activityLevel']
    normalHeroicLevel = json['Response']['definitions']['activities']\
                            [str(activityHashes[1])]['activityLevel']
    hardHeroicLevel = json['Response']['definitions']['activities']\
                          [str(activityHashes[2])]['activityLevel']
    return [str(easyHeroicLevel), \
            str(normalHeroicLevel), \
            str(hardHeroicLevel)]

def getConfigPath():
    """ Returns the path of the configuration file """
    return os.path.expanduser('~/DestinyChecklist/')

def getDefaultBackground():
    """ Returns the default button color """
    return "#FFFFFF"

def getStartedBackground():
    """ Returns the started button color """
    return "#FFFF00"

def getCompletedBackground():
    """ Returns the completed button color """
    return "#00FF00"