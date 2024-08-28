import os       # for file handling  
import sys      # for writing/printing messages
import math
import pathlib  # Helpers for working with paths

import re    # for splitting input

from file_utils import remove_file, rename_file, clean_disk_directory
######### STENCIL CONSTANTS (DO NOT CHANGE) ######################
DISK_PATH = pathlib.Path("disk") # path to store files, relative to current directory
PRINT_SEP = "====" # used to separate messages when printing them out

######### YOUR CONSTANTS (unlimited number allowed) #######################
# (Add your own constants (if any) here!)


######### GLOBAL VARIABLES (at most 10 active at any time) ##############
# (Add your own global variables (if any) here!)

######### EXCEPTIONS #################################################
class MessagesFullExn(Exception):
    pass


####### CORE SYSTEM OPERATIONS ####################################

def connect(username: str) -> None:
    """
    Starts a connection to the system by the named user

    Parameters:
    username -- the name of the user who is connecting (they will be the
                poster of messages added until they disconnect)
    """
    # TODO: Fill in!
    # Note:  don't feel like you need to fill these in in order!  
    # Think about how you'll store messages first, and then consider
    # what connect()/disconnect() etc need to do.

def disconnect() -> None:
    """
    Disconnects the current user (this will depend on your design) and saves
    data as necessary so that the system can resume even if the Python program
    is restarted 
    """
    # TODO: Fill in!

def switch_user(username: str) -> None:
    """
    Switch to a different user (without disconnecting)
    """
    # TODO: Fill in!


def clean_reset() -> None:
    """
    Deletes all the disk files to start a clean run of the system.
    THIS FUNCTION WILL BE RUN BEFORE EACH TEST.  Use it to reset globals,
    constants, etc. back to a starting state when the BBS is empty.

    We've started this function for you:  clean_disk_directory()
    removes any files in DISK_PATH.  From here, you should also modify this
    function to reset any globals you use back to their starting state.
    """
    clean_disk_directory() # DO NOT REMOVE THIS

    # TODO:  If you need to reset other global variables, reset them here!


def post_msg(subj: str, msg: str) -> None:
    """
    Stores a new message (however it makes sense for your design). Your code
    should determine what ID to use for the message, and the poster of the
    message should be the user who is connected when this function is called

    Parameters:
    subj -- subject line
    msg -- message body
    """
   
    # TODO: Fill in!


def find_print_msg(id: int) -> str:
    """
    Prints contents of message for given ID. 

    Parameters:
    id -- message ID
    Returns:
    The string to be printed (for autograder).
    """

    # TODO: Fill in!


def remove_msg(id: int) -> None:
    """
    Removes a message from however your design is storing it. A removed message
    should no longer appear in summaries, be available to print, etc.
    """

    # TODO: Fill in!


def print_summary(term = "") -> str:
    """
    Prints summary of messages that have the search term in the who or subj fields.
    A search string of "" will match all messages.
    Summary does not need to present messages in order of IDs.

    Returns:
    A string to be printed (for autograder).
    """
    
    # TODO: Fill in!



######## HELPERS ##########################################
def print_msg(id: int, who: str, subj: str, msg: str) -> None:
    """
    Print out a message--use this function to print out messages
    to the terminal in the required format. 
    (We need everyone to use the same format when printing so we
    can test your work!)


    Parameters:
    id -- message id
    who -- poster
    subj -- subject line
    msg -- body text
    """
    print(PRINT_SEP)
    print("ID: " + str(id) + "\n")
    print("Poster: " + who + "\n")
    print("Subject: " + subj + "\n")
    print("Message: " + msg + "\n")
    print(PRINT_SEP)


def split_string_exclude_quotes(s) -> list[str]:
    """
    Splits a given string and splits it based on spaces, while also grouping
    words in double quotes together.

    Parameters:
    s -- string to be split
    Returns:
    A list of strings after splitting
    Example:
    'separate "these are together" separate` --> ["separate", "these are together", "separate"]
    """
    # This pattern matches a word outside quotes or captures a sequence of characters inside double quotes without including the quotes
    pattern = r'"([^"]*)"|(\S+)'
    matches = re.findall(pattern, s)
    # Each match is a tuple, so we join non-empty elements
    return [m[0] if m[0] else m[1] for m in matches]



############### MAIN PROGRAM ############################
# The following functions are used when running the program interactively,
# which you can do by running the following in your terminal:
#  python bbs.py  (or python3 bbs.py)
# This funs the main() function, which creates a REPL for a user
# to interact with your BBS.

def show_menu(): 
    """
    Prints the menu of options.
    """
    print("Please select an option: ")
    print("  - type A <subj> <msg> to add a message")
    print("  - type D <msg-num> to delete a message")
    print("  - type S for a summary of all messages")
    print("  - type S <text> for a summary of messages with <text> in title or poster")
    print("  - type V <msg-num> to view the contents of a message")
    print("  - type X to exit (and terminate the Python program)")
    print("  - type U to switch user")
    print("  - type R to to reset the BBS, deleting all posts!")

def main():
    """
    Loop to run the system. It does not do error checking on the inputs that
    are entered (and you do not need to fix that problem)
    """
    
    print("Welcome to our BBS!")
    print("What is your username?")
    connect(input())

    done = False
    while(not done):
        show_menu()
        whole_input = input() # read the user command
        choice = split_string_exclude_quotes(whole_input) #split into quotes
        match choice[0].upper():
            case "A": 
                post_msg(choice[1], choice[2]) # subject, text
            case "D": 
                remove_msg(int(choice[1]))
            case "S": 
                if len(choice) == 1:
                    print_summary("")
                else:
                    term = choice[1]
                    print_summary(term)
            case "V":
                find_print_msg(int(choice[1]))
            case "X": 
                disconnect()
                done = True
                exit()
            case "R":
                clean_reset()
                print("System reset!")
            case "W":
                # restart menu
                print("What's your username?")
                switch_user(input())
            case _: 
                print("Unknown command")


# This runs the main function when bbs.py 
# is run directly from the terminal 
if __name__ == "__main__":
    main()
