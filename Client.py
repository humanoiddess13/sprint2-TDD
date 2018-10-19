# coding=utf-8
"""
Private and protected attributes and economy memory slots.

Protected member is (in C++ and Java) accessible only from within the class and it’s subclasses.
How to accomplish this in Python? The answer is – by convention. By prefixing the name of your member
with a single underscore, you’re telling others “don’t touch this, unless you’re a subclass”.
For ex : _name is a protected attribute.

By declaring your data member private you mean, that nobody should be able to access it from
outside the class, i.e. strong you can’t touch this policy. Python supports a technique called
name mangling. This feature turns every member name prefixed with at least two underscores and suffixed
with at most one underscore into _<className><memberName> .
For ex : __name is a private attribute and if it is member of class A(), it can be accessed as A._A__name

The default can be overridden by defining __slots__ in a new-style class definition. The __slots__ declaration
takes a sequence of instance variables and reserves just enough space in each instance to hold a value for each
variable. Space is saved because __dict__ is not created for each instance.
This class variable can be assigned a string, iterable, or sequence of strings with variable names
used by instances.
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

