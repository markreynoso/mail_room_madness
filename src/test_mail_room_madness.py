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
    """ensures that populate_dictionary() returns added value to dict"""
    from mail_room_madness import populate_dictionary
    for i in range(4):
        output = populate_dictionary(a, b)
        assert output[a][0] == b