"""This file contains psuedocode for writing thank you notes to non-profit donors"""

import sys


donor_data = {'Phil Collins':[25, 45, 76, 100], 'Sven Sunguaard': [50, 1000, 76, 1400]}


def main(): #pragma: no cover
    prompt_user()


def populate_dictionary(name, donation): #pragma: no cover
    """This function creates a dictionary of donors with names and giving amounts as key-value pairs."""
    try:
        donor_data[name].append(donation)
    except KeyError:
        donor_data[name] = [donation]
    return donor_data


def send_thank_you(full_name, donation_amount):
    """This function will send a personalized thank you not to the user."""
    return ('\nDear {},\n Thank you for your generous donation of ${}. Your support is making a difference in our community.\nSincerely,\nMark and Kavdi\nDirectors of Good\n'.format(full_name, donation_amount)) 


def set_thank_you_amount(full_name): #pragma: no cover
    """This function allows the user to set a donation amount for each donor"""
    donation_amount = input('\nPlease enter donation amount.\n')
    if donation_amount.isalpha():
        print('\nPlease enter a number.\n')
        set_thank_you_amount(full_name)
    else:
        populate_dictionary(full_name, int(donation_amount))
        letter = send_thank_you(full_name, donation_amount)
        print(letter)
        prompt_user()


def find_thank_you_donor(): #pragma: no cover
    """This function allows the user to access a list of donor names or create a new donor name"""
    full_name = input('\nPlease do one of the following:\n- Enter a donors name to input donation amount\n- Enter a new donor name to create an account\n- Type list to show all current donors.\n')
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
    return (tabulate(holder_list, headers=['Name', 'Total Giving', '# Gifts', 'Avg Donation']))


def prompt_user(): #pragma: no cover
    """This function gives instructions to the user and provides options for use"""
    response = input('\nWelcome to your donor management center.\nWhat would you like to do?\n\nType:\n- TY to send a thank you note to a donor\n- CR to create a donation report\n- Q to exit.\n')
    if response == 'TY':
        find_thank_you_donor()
    elif response == 'CR':
        report = create_report()
        print(type(report))
        prompt_user()
    elif response == 'Q':
        sys.exit()
    else:
        print('\nPlease type a valid input\n')
        prompt_user()


if __name__ == '__main__': #pragma: no cover
    main()
