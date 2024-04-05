import os    # for file handling  
import sys   # for writing/printing messages
import math

import re    # for splitting input

######### CONSTANTS (unlimited number allowed) #######################
SEP = "====" # used to separate messages when printing them out


######### VARIABLES (at most 10 active at any time) ##################

######### EXCEPTIONS #################################################
class MessagesFullExn(Exception):
    pass

######### SYSTEM SETUP, SHUTDOWN, AND RESET ##########################

def connect(username: str, restart: bool) -> None:
    """
    Starts a connection to the system by the named user

    Parameters:
    username -- the name of the user who is connecting (they will be the
                poster of messages added until they disconnect)
    restart -- if the program has just connected to the server
    """
    # TODO: Fill in!

def disconnect() -> None:
    """
    Disconnects the current user (this will depend on your design) and saves
    data as necessary so that the system can resume even if the Python program
    is restarted 
    """
    # TODO: Fill in!

def soft_disconnect() -> None:
    """
    Disconnects the current user (this will depend on your design)
    """
    # TODO: Fill in!


def clean_reset(msg_max_val=200, msg_per_file_val=10) -> None:
    """
    Deletes all the disk files to start a clean run of the system.
    Supports setting different constant values.
    Useful for testing.

    Parameters:
    msg_max_val -- max number of messages system can hold
    msg_per_file_val -- max number of messages each file can hold

    """
    
    # TODO: Fill in with what makes sense for your design.
    # It might relate to how you store your necessary info
    # between (dis)connections to the server!
    # Feel free to pass in different values when testing for clean_reset,
    # 200 and 10 are just the default. (You do not need to edit
    # the method header to do this. Just pass different values in when calling)


######## DESIGN HELPERS ##########################################
def write_msg(f, id: int, who: str, subj: str, msg: str, labeled=False) -> None:
    """
    Writes a message to the given file handle. e.g., If you want to print to a
    file, open the file and use fh from the following code as the first argument

           with open(FILENAME, mode) as fh

    If you want to print to the console/screen, you can pass the following as 
    the first argument

            sys.stdout

    msg can be passed as false to suppress printing the text/body of the message.

    Parameters:
    f -- file descriptor
    id -- message id
    who -- poster
    subj -- subject line
    msg -- body text
    labeled -- boolean deciding if labels should also be used
    """
    f.write(SEP + "\n")
    f.write("ID: " + str(id) + "\n")
    if labeled:
        f.write(who)
        f.write(subj)
        if msg: f.write(msg)
    else: # needs labels
        f.write("Poster: " + who + "\n")
        f.write("Subject: " + subj + "\n")
        if msg: f.write("Text: " + msg + "\n")


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


####### CORE SYSTEM OPERATIONS ####################################


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
    print("  - type softX to exit (and keep the Python program running)")


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


############### SAMPLE FROM HANDOUT ######################

# Our test cases will look like this, with assertions intertwined

def sample():
    connect("kathi")
    post_msg("post homework?", "is the handout ready?")
    post_msg("vscode headache", "reinstall to fix the config error")
    soft_disconnect()  # keep the python programming running and connect another user
    connect("nick")
    print_summary("homework")
    find_print_msg(1)
    post_msg("handout followup", "yep, ready to go")
    remove_msg(1)
    print_summary()
    disconnect()

############### MAIN PROGRAM ############################

# If you want to run the code interactively instead, use the following:

def start_system():
    """
    Loop to run the system. It does not do error checking on the inputs that
    are entered (and you do not need to fix that problem)
    """
    
    print("Welcome to our BBS!")
    print("What is your username?")
    connect(input(), True)

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
            case "SOFTX":
                soft_disconnect()

                # restart menu 
                print("What's your username?")
                connect(input(), False)
            case _: 
                print("Unknown command")

# uncomment next line if want the system to start when the file is run
# start_system()
