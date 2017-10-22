"""This file contains psuedocode for writing thank you notes to non-profit donors"""

import sys


donor_data = {'Phil Collins':[25, 45, 76, 100], 'Sven Sunguaard': [50, 1000, 76, 1400]}


# def main():
#     call all the things

def populate_dictionary(name, donation):
    """This function creates a dictionary of donors with names and giving amounts as key-value pairs. """
    try:
        donor_data[name].append(donation)
    except KeyError:
        donor_data[name] = [donation]
    print (donor_data)

# populate_dictionary('Phil Collins', 10000)


def send_thank_you(full_name, donation_amount):
    """This function will send a personalized thank you not to the user."""
    print('Thank you, {}, for your generous donation of ${}. Your support is making a difference in our community.'.format(full_name, donation_amount))


def set_thank_you_amount(full_name):
    donation_amount = input('Please enter donation amount')
    if donation_amount.isalpha():
        print("Please enter a number.")
        set_thank_you_amount(full_name)
    else:
        populate_dictionary(full_name, int(donation_amount))
        send_thank_you(full_name, donation_amount)


def find_thank_you_donor():
    full_name = input('Please enter name or type list for a list of donors')
    if full_name.lower() == 'list':
        for i in donor_data:
            print(i)
        find_thank_you_donor()
    else:
        set_thank_you_amount(full_name)


def prompt_user():
    response = input('Welcome! What would you like to do? Write TY to send a thank you note to a donor, or CR to create a donation report. If you are here by mistake, just type Q to exit.')
    if response == 'TY':
        find_thank_you_donor()
    elif response == 'CR':
        create_report()
    elif response == 'Q':
        sys.exit()
    else:
        print('Please type a valid input')
        prompt_user()
prompt_user()




        
#     else:
#         add name to dictionary and use it
#     select_amount()

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
