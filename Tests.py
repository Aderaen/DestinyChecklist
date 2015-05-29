"""
Unit tests for Destiny Checklist

Created on 2015-05-26

@author: Alexandre
"""

import DestinyChecklist
#import sys

def addButtonTests():
    """ Tests for the function addButton() """
    isPassed = True
    window = DestinyChecklist.createWindow(25, 25)
    buttonsList = [[],[],[]]
    names = ["1"]
    try:
        DestinyChecklist.addButton(window, buttonsList, 0, 0, names)
        #print("Success: The button was created")
    except:
        isPassed = False
        print("Error: Valid button does not pass")
        pass
    try:
        DestinyChecklist.addButton(None, buttonsList, 0, 0, names)
        isPassed = False
        print("Error: Null window should not be valid")
    except:
        #print("Success: "+str(sys.exc_info()[0]))
        pass
    try:
        DestinyChecklist.addButton(window, [], 0, 0, names)
        isPassed = False
        print("Error: Invalid buttonsList should be catched")
    except:
        #print("Success: "+str(sys.exc_info()[0]))
        pass
    try:
        DestinyChecklist.addButton(window, buttonsList, 0, 0, [])
        isPassed = False
        print("Error: Invalid buttonsList should be catched")
    except:
        #print("Success: "+str(sys.exc_info()[0]))
        pass
    if isPassed:
        print("Success: addButton ran correctly")
        
def getHeroicLevelsTests():
    """ Tests for the function getHeroicLevels() """
    isPassed = True
    try:
        values = DestinyChecklist.getHeroicLevels()
        if values == ["26","30","32"]:
            #print("Success: The values were correctly fetched")
            pass
        else:
            print("Error: The values were not right")
    except:
        isPassed = False
        print("Error: There was a connection error")
        pass
    if isPassed:
        print("Success: getHeroicLevels ran correctly")
    

addButtonTests()
getHeroicLevelsTests()