Program that take note and save you progress in the current weekly chalenges of Destiny
Created by Alexandre Guay
28 May 2015

Install (Windows)
_____________________________________
1. Download and install python3 at (https://www.python.org/)
2. Download Requests (https://github.com/kennethreitz/requests/zipball/master)
3. Extract it and run the setup.py 
		#python setup.py install
4. Execute the Checklist.py with the command in the program folder:
		#python Application.py

Install (Linux Ubuntu)
_____________________________________
1. Enter in console to download and install Python : sudo apt-get install python3.4
2. Enter in console to download and install Requests lib: pip install requests
3. Execute the Checklist.py with the command in the program folder:
		$python Application.py

		
How to use
______________________________________
Click on the matching button to change the state of completition it is.
Gray = not done 
Yellow = partially done
Green = Completly done

(N) = Normal Difficulty
(H) = Hard Difficulty


Note : the program should save your actual state into "~/DestinyChecklist/values.cfg"
if you hit the save button and will load on launch.
