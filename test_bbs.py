import importlib
import pytest


import bbs
import file_utils
from file_utils import DISK_PATH


# TEST SETUP:  this is a special function in pytest that runs
# before each test.  Here, we use it to reset your BBS on each test,
# so that each test runs independently (ie, files you write to disk
# in one test are deleted in the next one, or when you re-run a test)
#
# DO NOT MODIFY THIS FUNCTION
#
def setup_function(request):
    global bbs
    bbs = importlib.reload(bbs) # Reload the BBS module, resetting any globals
    bbs.clean_reset()


def test_example():
    assert 2 == 1 + 1

############### SAMPLE TEST FROM HANDOUT ######################

# Our test cases will look like this, with assertions intertwined

def test_sample_From_handout():
    bbs.connect("kathi")
    msg_id = bbs.post_msg("post homework?", "is the handout ready?")
    bbs.post_msg("vscode headache", "reinstall to fix the config error")

    s1 = bbs.print_summary("headache")
    assert "Poster: kathi" in s1

    bbs.switch_user("nick")
    bbs.find_print_msg(msg_id)
    # assert ???  (What might we test about this message?)

    bbs.post_msg("handout followup", "yep, ready to go")
    bbs.remove_msg(msg_id)
    s2 = bbs.print_summary("followup")
    # assert ???  (What might we test at this point?)

