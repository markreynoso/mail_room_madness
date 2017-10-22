"""This file tests the mail_room_madness module"""

import pytest
# import sys

# def test_prompt_user():
#     from mail_room_madness import prompt_user
#     prompt_user()
#     output = sys.stdout.getline().strip()
#     assert output == 'Welcome! What would you like to do? Write TY to send a thank you note to a donor, or CR to create a donation report. If you are here by mistake, just type Q to exit.'


# def test_create_report():
#     from mail_room_madness import create_report

# data = [
#     ('Bob Barker', 980),
#     # ('Flerg Blerg', 23),
#     # ('Mail Room', 749),
#     # ('The Madness', 43)
# ]

# @pytest.mark.parametrize('a, b', data)
def test_populate_dictionary(a, b):
    from mail_room_madness import populate_dictionary
    
    # for i in data:
    assert type(populate_dictionary('Bob Barker', 40)) == dict