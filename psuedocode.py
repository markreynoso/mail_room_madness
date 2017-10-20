"""This file contains psuedocode for writing thank you notes to non-profit donors"""

data = {}

def create_data():
    """This function creates a dictionary of donors with names and giving amounts as key-value pairs. """
    returns two options to user:
    send_thank_you()
    create_report()
    if quit:
        exit()

def send_thank_you():
    """This function will send a personalized thank you not to the user."""
    prompt for full name input
    if list is input:
        show list of names
    elif name:
        use it
    else:
        add name to dictionary and use it
    select_amount()

def select_amount():
    """This function recieves the donation amount of a selected individual"""
    allow user to input donation amount
    if number:
        add amount to donation history
        create_thank_you()
    else:
        prompt select_amount() again. 

def create_thank_you():
    """his function creates a personalized thank you note to a donor with the name and amount given included."""
    print a thank you note to the terminal in string notation. 
    send_thank_you()

def create_report():
    """This function prints a report of the giving history of all donors with their names."""
    if quit:
        create_data()
    print report including the donor's name, giving total, giving frequency, and average gift.
    create_data()
