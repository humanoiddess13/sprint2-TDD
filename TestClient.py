from unittest import TestCase

from Client import Client
from sys import getsizeof


class ClientTestCase(TestCase):
    """
    This class is used to test Client.
    """

    def test_set_protected_argument(self):

        """
        Tests if a protected variable can be changed.
        """

        client = Client(167, 5578342726791879)
        client._id = 157
        self.assertEqual(client._id, 157)

    def test_set_private_argument_not_properly(self):

        """
        Tests if a private variable can be changed without invoking class name.
        """

        client = Client(167, 5578342726791879)
        client.set_private_argument_not_properly(5578323212125656)
        self.assertRaises(AttributeError, client.set_private_argument_not_properly(5578323212125656))

    def test_set_private_argument(self):

        """
        Tests if a private variable can be changed.
        """

        client = Client(167, 5578342726791879)
        client.set_private_argument(5578342726791877)
        self.assertEqual(client._Client__card_number, 5578342726791877)

    def test_memory_optimization(self):

        """
        Tests if __slots__ uses less memory than __dict__.

        Filters:
            size_of_slot : size, that __slots__ with variables obtains in memory
            size_of_dict : size, that __dict__ with variables obtains in memory
        """

        client = Client(167, 5578342726791879)
        size_of_slot = getsizeof(client.__slots__)
        size_of_dict = getsizeof(client.__dict__)
        self.assertTrue(size_of_slot < size_of_dict)

    def test_different_arguments_in_memory(self):

        """
        Tests if variable in __dict__ or in __slots__.

        Filters :
            dict_keys : keys of variables in __dict__
            first_arg_in_dict : first key in dict_keys
        """

        client = Client(167, 5578342726791879)
        dict_keys = client.__dict__.keys()
        first_arg_in_dict = list(dict_keys)[0]
        self.assertNotIn(first_arg_in_dict, client.__slots__)

    def test_different_arguments_in_memory(self):
            """
            Tests if variable in __dict__ or in __slots__.

            Filters :
                first_arg_in_slots : argument in slots, next to dict
            """

            client = Client(167, 5578342726791879)
            first_arg_in_slots = client.__slots__[1]
            self.assertNotIn(first_arg_in_slots, client.__dict__.keys())
