"""This file contains psuedocode for writing thank you notes to non-profit donors"""

import sys


donor_data = {'Phil Collins':[25, 45, 76, 100], 'Sven Sunguaard': [50, 1000, 76, 1400]}


def main(): #pragma: no cover
    prompt_user()


def populate_dictionary(name, donation):
    """This function creates a dictionary of donors with names and giving amounts as key-value pairs. """
    try:
        donor_data[name].append(donation)
    except KeyError:
        donor_data[name] = [donation]
    print (donor_data)


def send_thank_you(full_name, donation_amount):
    """This function will send a personalized thank you not to the user."""
    print('Thank you, {}, for your generous donation of ${}. Your support is making a difference in our community.'.format(full_name, donation_amount))


def set_thank_you_amount(full_name):
    """This function allows the user to set a donation amount for each donor"""
    donation_amount = input('Please enter donation amount')
    if donation_amount.isalpha():
        print("Please enter a number.")
        set_thank_you_amount(full_name)
    else:
        populate_dictionary(full_name, int(donation_amount))
        send_thank_you(full_name, donation_amount)


def find_thank_you_donor():
    """This function allows the user to access a list of donor names or create a new donor name"""
    full_name = input('Please enter name or type list for a list of donors')
    if full_name.lower() == 'list':
        for i in donor_data:
            print(i)
        find_thank_you_donor()
    else:
        set_thank_you_amount(full_name)


def create_report():
    """This function prints a report of the giving history of all donors with their names."""
    from tabulate import tabulate
    holder_list = []
    for person in donor_data:
        total = sum(donor_data[person])
        num_gifts = len(donor_data[person])
        avg = total / num_gifts
        holder_list.append([person, total, num_gifts, avg])
    print (tabulate(holder_list, headers=['Name', 'Total Giving', '# Gifts', 'Avg Donation']))
    prompt_user()


def prompt_user():
    """This function gives instructions to the user and provides options for use"""
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


if __name__ == '__main__': #pragma: no cover
    main()
