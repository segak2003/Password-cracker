# Password-cracker
## Password cracker made to research password vulnerability

##brief description
This project contains a Python script that demonstrates the principles of password cracking using both dictionary and brute-force attack methods. The script attempts to crack a given password by first using a dictionary attack with a list of the 4000 most common passwords in the world and then resorts to a brute-force attack if the dictionary attack fails.

##Features
Dictionary Attack: Checks the given password against a list of common passwords.
Brute-Force Attack: Tries every possible combination of characters up to a certain length.
Time Tracking: Measures the time taken to crack the password.
Character Output Option: Optionally outputs each guess during brute-force (increases runtime).

##Installation
No additional libraries are required for the dictionary attack feature. For the brute-force feature, ensure you have the following Python package installed:

colorama
You can install it using pip:
pip install colorama

##Usage
Run the script in a Python environment. You will be prompted to enter the password you want to crack. Optionally, you can choose to display each brute-force attempt, however this will drastically increase the runtime.

##Disclaimer
This tool is intended for educational purposes only. The use of this script for testing, educational, or ethical hacking purposes should be done on passwords or systems you own or have explicit permission to test.

##Contributing
Contributions to the project are welcome. Please ensure your pull requests are concise and clear, and explain the purpose of the change.


