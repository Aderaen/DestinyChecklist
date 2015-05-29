"""
Application launcher for Destiny Checklist

Created on 2015-05-26

@author: Alexandre
"""

import DestinyChecklist

def launch():
    """ Launches the application """
    window = DestinyChecklist.createWindow(25, 25)
    buttonsList = [[],[],[]]
    DestinyChecklist.load(buttonsList)
    DestinyChecklist.fillWindow(window,buttonsList)
    window.mainloop()

launch()