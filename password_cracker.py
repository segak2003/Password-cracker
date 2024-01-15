import hashlib
import itertools
import string
import time
from colorama import Fore, Style

def print_colored(message, color):
    print(color + message + Style.RESET_ALL)

def brute_force(hashedPasswrd, starting_time, pause_time, output_chars):

    char_set = string.printable[:-5]     # list of every string character (Excludes the last 6 whitespace characters)
    num_tries = 0                        # counts how many brute force attempts were made
    start = starting_time - pause_time   # "resumes" the timer

    # Iterate through every possible combinations of characters up to a length of 9
    for i in range(9):
        for guess_string in [''.join(element) for element in itertools.product(char_set, repeat=i+1)]: 

            hashed_guess_obj = hashlib.md5(guess_string.encode())
            hashed_guess = hashed_guess_obj.hexdigest()
            num_tries += 1

            if output_chars == 'y':
                # Optionally output each guess (significantly increases runtime)
                print(guess_string)
            
            # Terminate if operation exceeds 100 seconds
            if((time.time() - starting_time - pause_time) >= 100):
                print("the time has exceeded 100 seconds")
                return None
            
            # Check if the current guess matches the hashed password
            if(hashed_guess == hashedPasswrd):
                end_time = time.time()
                time_elapsed =  end_time - starting_time - pause_time
                print_colored(f"Password cracked using brute force in {time_elapsed:.3f} seconds!", Fore.RED)
                print(f"It took {num_tries} tries to crack it")
                return guess_string
    return None

# Main execution starts here
plainTxtPasswrd = input("type the password you would like to crack: ")
start_time = time.time()    # starts the timer (counts how long the password cracker takes to crack the password)
passwrdCracked = False
count = 0

#this is a hash object of the user's password
hashedPasswrdObj = hashlib.md5(plainTxtPasswrd.encode())
#this gets the string version of the hashed password 
hashedPasswrd = hashedPasswrdObj.hexdigest()

# Opens the dictionary containing the 4000 most common passwords
with open("common_passwords.txt", "r") as file:
    common_passwrds_dict = file.read().splitlines()

# starts the dictionary attack (checks if the hashed password matches any common password)
for common_passwrd in common_passwrds_dict:
    tempHash = hashlib.md5(common_passwrd.encode())
    hashedTemp = tempHash.hexdigest()
    count += 1    #counter to keep track of how common the password is
    if hashedPasswrd == hashedTemp:
        end_time = time.time()
        passwrdCracked = True
        break

# If password was cracked using dictionary attack
if passwrdCracked:
    time_elapsed = end_time - start_time
    print_colored(f"your password has been cracked using a dictionary attack in {time_elapsed:.3f} seconds!", Fore.RED)
    print("Your password is:", common_passwrd) 
    tempCount = count

    # logic to determine the correct ordinal suffix 
    if tempCount < 10:
        if tempCount == 1:
            print(f"your password is the most common password" )
        elif tempCount == 2:
            print(f"your password is the {count}nd most common password" )
        elif tempCount == 3:
            print(f"your password is the {count}rd most common password" )
        else:
            print(f"your password is the {count}th most common password" )

    if tempCount > 9:

        if tempCount >= 100:
            tempCount = tempCount % 100

        if tempCount >= 10 and tempCount <= 19:
            print(f"your password is the {count}th most common password" )

        else:
            tempCount %= 10
            if tempCount == 1:
                print(f"your password is the {count}st most common password" )
            elif tempCount == 2:
                print(f"your password is the {count}nd most common password" )
            elif tempCount == 3:
                print(f"your password is the {count}rd most common password" )
            else:
                print(f"your password is the {count}th most common password" )

# if dictionary attack was unsuccessful commence the brute force
if passwrdCracked == False:

    ''' pause timer because we don't want to account for the time it takes for the user takes to decide whether 
        to output test characters to our timer
    '''
    pause_timer = time.time()
    output_chars = input("output the test characters, (y/n)? (doing so will increase the runtime significantly)")
    while output_chars != 'y' and output_chars != 'n':
        output_chars = input("invalid input, please type y for yes, or n for no. ")

    # now that the user is done deciding, resume timer
    resume_timer = time.time()
    total_paused_time = resume_timer - pause_timer
    guess = brute_force(hashedPasswrd, start_time, total_paused_time, output_chars)

    # checks if brute force was succesfull
    if guess != None:
        passwrdCracked = True
        print("your password is:", guess)
    else:
        print_colored("good job, we couldn't crack your password withoug exceeding the time limit", Fore.GREEN)
        
#close the dictionary file
file.close()
