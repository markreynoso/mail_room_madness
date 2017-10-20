"""This file contains psuedocode for writing thank you notes to non-profit donors"""

import sys

donor_data = [{'name': 'Phil Collins', 'donations': [25, 45, 76, 100]}, {'name': 'Sven Sunguaard', 'donations': [50, 1000, 76, 1400]}]

# def main():
#     call all the things

def populate_dictionary(name, donation):
    """This function creates a dictionary of donors with names and giving amounts as key-value pairs. """
    for i in range(len(donor_data)):
        if donor_data[i]['name'] == name:
            donor_data[i]['donations'].append(donation)
        else:
            donor_data.append({'name': name, 'donations': [donation]})
            break
    print (donor_data)

populate_dictionary('Paul Miller', 10000)


def prompt_user():
    response = input('Welcome! What would you like to do? Write TY to send a thank you note to a donor, or CR to create a donation report. If you are here by mistake, just type Q to exit.')
    if response == 'TY':
        send_thank_you()
    elif response == 'CR':
        create_report()
    elif response == 'Q':
        sys.exit()
    else:
        print('Please type a valid input')
        prompt_user()
        

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

# def select_amount():
#     """This function recieves the donation amount of a selected individual"""
#     allow user to input donation amount
#     if number:
#         add amount to donation history
#         create_thank_you()
#     else:
#         prompt select_amount() again. 

# def create_thank_you():
#     """his function creates a personalized thank you note to a donor with the name and amount given included."""
#     print a thank you note to the terminal in string notation. 
#     send_thank_you()

# def create_report():
#     """This function prints a report of the giving history of all donors with their names."""
#     if quit:
#         create_data()
#     print report including the donor's name, giving total, giving frequency, and average gift.
#     create_data()
