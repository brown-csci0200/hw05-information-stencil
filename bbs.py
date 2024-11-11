# bbs.py
# Implementation for Bulletin Board System (BBS)!
#

import os       # for file handling  
import sys      # for writing/printing messages
import math
import pathlib  # Helpers for working with paths

import re    # for splitting input

from file_utils import remove_file, rename_file, clean_disk_directory, file_exists

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


####### CORE API FUNCTIONS ####################################

# Note:  don't feel like you need to fill these in in order!  
# Think about how you'll store messages first, and then consider
# what connect()/disconnect() etc need to do.

def connect(username: str):
    """
    Starts a connection to the system by the named user.

    You may assume the username is well-formed (ie, within the character
    limits).

    Parameters:
    username -- the name of the user who is connecting (they will be the
                poster of messages added until they disconnect)
    """
    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!

def disconnect():
    """
    Disconnects the current user and saves data as necessary so that the system
    can resume even if the Python program is restarted.
    
    What you do here will depend on your design:
     - You may want to wait to implement this until you implement post_msg
     - It's not wrong if this function does nothing (your design might do the
       same work in other functions)
    """
    # TODO: Fill in!

def switch_user(username: str):
    """
    Switch to a different user (without disconnecting)

    You may assume the username is well-formed (ie, within the character limits)
    """
    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!


def clean_reset():
    """
    Deletes all the disk files to start a clean run of the system.  
    THIS FUNCTION WILL BE RUN BEFORE EACH TEST.  Use it to reset globals,
    constants, etc. back to a starting state when the BBS is empty.

    We've started this function for you:  clean_disk_directory() removes any
    files in DISK_PATH.  In addition, you should add to this function to reset
    any globals you use back to their starting state.
    """
    clean_disk_directory() # DO NOT REMOVE THIS

    # TODO:  If you need to reset other global variables, reset them here!


def post_msg(subj: str, msg: str) -> int:
    """
    Stores a new message (however it makes sense for your design). Your code
    should determine what ID to use for the message, and the poster of the
    message should be the user who is connected when this function is called.

    You can assume that both the subj and msg fields are within
    the character limits.

    Parameters:
    subj -- subject line
    msg -- message body

    Returns:  the ID number of the message created (for autograder)
    """
   
    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!


def find_print_msg(id: int) -> str:
    """
    Prints contents of message for given ID. 

    Parameters:
    id -- message ID

    Returns:
    The string to be printed (for autograder).  If the message is not found,
    returns an empty string.
    """

    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!


def remove_msg(id: int):
    """
    Removes a message from however your design is storing it. A removed message
    should no longer appear in summaries, be available to print, etc.

    You may assume the message exists.
    """

    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!


def print_summary(term="") -> str:
    """
    Prints summary of messages that have the search term in the who or subj fields.
    A search string of "" will match all messages.
    Summary does not need to present messages in order of IDs.

    Returns:
    A string to be printed with the summary text (for autograder)
    If there are no messages, return an empty string.
    """
    
    # TODO: Fill in!
    raise NotImplementedError("TODO") # Remove this when you're ready to test!






######## HELPERS ##########################################

def format_print_msg(id: int, who: str, subj: str, msg: str=None, do_print=False) -> str:
    """
    Create a string representing a message in the correct format to print
    to the terminal:
       - if msg=None, only summary is printed.
       - if do_print=True, prints the message to a terminal as well

    DO NOT MODIFY THIS FUNCTION.  We need everyone to use the same format when
    printing so we can test your work in the autograder!

    Parameters:
    id -- message id
    who -- poster
    subj -- subject line
    msg -- body text (optional, only summary printed if set to None)
    do_print - if true, print the message to the string as well

    Returns:
    string of the message in correct format (for autograder)
    """
    output_str = ""
    output_str += PRINT_SEP
    output_str += f"\nID: {id}"
    output_str += f"\nPoster: {who}"
    output_str += f"\nSubject: {subj}\n"

    if msg is not None:
        output_str += f"Message: {msg}\n"

    output_str += PRINT_SEP

    if do_print:
        print(output_str)

    return output_str

def print_msg(id: int, who: str, subj: str, msg: str=None) -> str:
    """
    Print a message to the terminal in the correct format
    (This is just a shortcut for calling format_msg with print=True)

    DO NOT MODIFY THIS FUNCTION.  We need everyone to use the same format when
    printing so we can test your work in the autograder!

    Parameters:
    id -- message id
    who -- poster
    subj -- subject line
    msg -- body text (optional, use msg=None to only print summary)
        
    Returns:
    string of the message in correct format (for autograder)
    """
    return format_print_msg(id, who, subj, msg, print=True)

def split_string_exclude_quotes(s) -> list[str]:
    """
    Splits a given string and splits it based on spaces, while also grouping
    words in double quotes together.

    DO NOT MODIFY THIS FUNCTION.  This is a helper for you to use if you
    like, but it's not required.

    Parameters:
    s -- string to be split
    Returns:
    A list of strings after splitting
    Example:
    'separate "these are together" separate` --> ["separate", "these are together", "separate"]
    """
    # This pattern matches a word outside quotes or captures a sequence of
    # characters inside double quotes without including the quotes
    pattern = r'"([^"]*)"|(\S+)'
    matches = re.findall(pattern, s)
    # Each match is a tuple, so we join non-empty elements
    return [m[0] if m[0] else m[1] for m in matches]

