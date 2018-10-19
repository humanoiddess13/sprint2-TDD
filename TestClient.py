from unittest import TestCase

from Client import Client
from sys import getsizeof


class ClientTestCase(TestCase):

    def test_var(self):
        client = Client(167,5578342726791879)
        client._id = 157
        self.assertEqual(client._id,157)

    def test_change_private_argument_not_properly(self):
        client=Client(167,5578342726791879)
        client.change_private_argument_not_properly(5578323212125656)
        self.assertRaises(AttributeError,client.change_private_argument_not_properly(5578323212125656))

    def test_change_private_argument(self):
        client = Client(167, 5578342726791879)
        client.change_private_argument(5578342726791877)
        self.assertEqual(client._Client__card_number, 5578342726791877)

    def test_memory_optimizaion(self):
        client = Client(167, 5578342726791879)
        a = getsizeof(client.__slots__)
        b = getsizeof(client.__dict__)
        self.assertTrue(a<b)

    def test_different_arguments_in_memory(self):
        client = Client(167, 5578342726791879)
        dict_keys = client.__dict__.keys()
        first_arg_in_dict = list(dict_keys)[0]
        self.assertNotIn(first_arg_in_dict, client.__slots__)
