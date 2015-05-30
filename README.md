Destiny Checklist
=================
An app that saves your progress in the current weekly 
challenges of the videogame Destiny

>Created by Alexandre Guay,
May 28 2015

Installation (Windows)
----------------------
1. Download and install Python 3.x at their [Website](https://www.python.org/)
2. Download Requests on [Github](https://github.com/kennethreitz/requests/zipball/master)
3. Extract it and run the setup.py
        python setup.py install
4. Execute the Checklist.py with the command in the program folder: 
        python Application.py 

Installation (Linux Ubuntu)
---------------------------
1. Enter in console to download and install Python and other packages:
        sudo apt-get install python3.4 python3-requests python3-tk
3. Execute the Checklist.py with the command in the program folder:
		python3.4 Application.py 

How to use
----------
Click on the activities to change their state of completition:
- Gray = Not done 
- Yellow = Partially done
- Green = Completly done
- White = Reset
- (N) = Normal Difficulty
- (H) = Hard Difficulty

Note: The program should save your actual state into "~/DestinyChecklist/values.cfg"
if you hit the save button and will load the same state on launch.
