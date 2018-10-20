# coding=utf-8
"""
Private and protected attributes and economy memory slots.

"""


class Client(object):
    """

    A class is used to represent economy memory slots
    to show the difference in obtaining the memory
    by dict and tuple(slots).

    Class named Client in order to represent the need in safety of data
    in terms of client of a bank system since it is a simple and understandable example.
    """

    __slots__ = ('__dict__', '_id')

    def __init__(self, id, card_number):
        """

        :param id: int
            Id of the client.
        :param card_number: int
            Card number of the client.

        Initializes id and card number of client as Client(167, 5578342755667788), where
        first argument stands for id and the second for card number.

        Id of the Client is a protected variable and is saved in __slots__.

        Card number of the Client is a private variable and is saved in __dict__.

        """

        self._id = id  # protected variable
        self.__card_number = card_number # private variable

    def change_private_argument_not_properly(self, card_number):
        """

        :param card_number: int

        Attempt to change card number value in order to show that private value is changes improperly and must be as
                className._className__attribute .
        """

        self.__card_number = card_number

    def change_private_argument(self, card_number):
        """

        :param card_number: int

        :return: int
            Changed value of card number.

        Changes value of private attribute by a given value, in our example card_number,
        and returns new value of Client._Client__card_number.
        """

        self._Client__card_number = card_number
        return self._Client__card_number

