"""
private
protected
economy memory slots
"""


class Client(object):
    """
    Why client?
    """

    __slots__=('__dict__','_id')

    def __init__(self, id, card_number):
        """

        :param id:
        :param card_number:
        """

        self._id = id  # protected variable
        self.__card_number = card_number # private variable

    def change_private_argument_not_properly(self,card_number):
        """

        :param card_number:
        :return:
        """

        self.__card_number = card_number

    def change_private_argument(self,card_number):
        """

        :param card_number:
        :return:
        """

        self._Client__card_number = card_number

