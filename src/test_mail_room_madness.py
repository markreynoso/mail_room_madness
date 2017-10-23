"""This file tests the mail_room_madness module"""

import pytest


DATA = [
    ('Bob Barker', 980),
    ('Flerg Blerg', 23),
    ('Mail Room', 749),
    ('The Madness', 43)
]


@pytest.mark.parametrize('a, b', DATA)
def test_populate_dictionary(a, b):
    """Ensures that populate_dictionary() returns added value to dict"""
    from mail_room_madness import populate_dictionary
    for i in range(4):
        output = populate_dictionary(a, b)
        assert output[a][0] == b

@pytest.mark.parametrize('a, b', DATA)
def test_populate_dictionary_type(a, b):
    """ensures that populate_dictionary() returns added value to dict"""
    from mail_room_madness import populate_dictionary
    for i in range(4):
        output = populate_dictionary(a, b)
        assert type(output) == dict


THANKS = [
    ('Chill Dude', 30, '\nDear Chill Dude,\n Thank you for your generous donation of $30. Your support is making a difference in our community.\nSincerely,\nMark and Kavdi\nDirectors of Good\n'),
    ('Bill Goat', 300, '\nDear Bill Goat,\n Thank you for your generous donation of $300. Your support is making a difference in our community.\nSincerely,\nMark and Kavdi\nDirectors of Good\n'),
    ('Ed Ucation', 9000, '\nDear Ed Ucation,\n Thank you for your generous donation of $9000. Your support is making a difference in our community.\nSincerely,\nMark and Kavdi\nDirectors of Good\n'),
    ('Friend Ly', 1, '\nDear Friend Ly,\n Thank you for your generous donation of $1. Your support is making a difference in our community.\nSincerely,\nMark and Kavdi\nDirectors of Good\n')
]


@pytest.mark.parametrize('a, b, result', THANKS)
def test_send_thank_you(a, b, result):
    """tests a non-numericalal value in send_thank_you()"""
    from mail_room_madness import send_thank_you
    assert send_thank_you(a, b) == result


NAMES = [
    ('Phil Collins'),
    ('Sven Sunguaard')
]


@pytest.mark.parametrize('result', NAMES)
def test_names_in_create_report(result):
    """Tests if database names are included in create_report()."""
    from mail_room_madness import create_report
    out = create_report()
    assert out.find(result)


AMT = [
    ('25'),
    ('45'),
    ('76'),
    ('100'),
    ('50'),
    ('1000'),
    ('76'),
    ('1400')
]


@pytest.mark.parametrize('result', AMT)
def test_donation_amounts_in_create_report(result):
    """Tests if each donation is included in create_report()."""
    from mail_room_madness import create_report
    out = create_report()
    assert out.find(result)


AVG = [
    ('246'),
    ('2526')
]


@pytest.mark.parametrize('result', AVG)
def test_avg_donation_in_create_report(result):
    """Tests if the average donation amount is included in create_report()."""
    from mail_room_madness import create_report
    out = create_report()
    assert out.find(result)