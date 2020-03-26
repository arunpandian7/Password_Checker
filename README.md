# Password_Checker
  Password Checker is a python application which can identify stolen or compromised passwords. It is based of a leaked or compromised passwords Database collected by Daniel Meissler. It has GUI which is also built using tkinter library on top of python.The python script will run through the massive sized database of leaked password list in a very short span of time to retrieve result.

## Requirements

* Python3
* Tkinter
* PIL
* ImageIO

## About SecList Leaked Password DataBase
  The Passwords directory will hold a number of password lists that can be used by multiple tools when attempting to guess credentials for a given targeted service. This will include a number of very popular lists in cooperation with their maintainers, including the RockYou lists maintained by Rob Bowes.

<a href src="https://github.com/danielmiessler/SecLists/tree/master/Passwords"> SecList-Leaked Database</a>

## Instructions
* Clone the repository 
```
git clone https://github.com/ArunRK7Codie/Password_Checker.git
```
* Change the directory to the repository
```
cd Password_Checker
```
* Run the *requirement.txt* to install the dependencies
```
pip install -r requirements.txt
```
* Run the *paswd_cracker_gui.py* to start the application
```
python paswd_cracker_gui.py
```
* Now you can play around with the application

## Screenshoots

![Screenshot of application](https://github.com/ArunRK7Codie/Password_Checker/blob/master/screenshot_01.png)

> "Passwords are like toothbrushes. They are best when new and should never be shared."
