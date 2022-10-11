#!/usr/bin/python3
"""Test for BaseModel.py"""

from time import sleep
import unittest
from unittest import mock
from unittest.mock import patch
from models.base_model import BaseModel
from datetime import datetime

class test_BaseModel(unittest.TestCase):
    """Unittest for BaseModel"""
    # def test_get_id_BaseModel(self):
    #     b1 = BaseModel()
    #     @patch('b1.iid',return_value=b1.iid):

    #     self.assertEqual(b1.iid, mock_uuid4)

    def test_created_at(self):
        b2 = BaseModel()
        b2.my_number = 89
        self.assertEqual(b2.my_number, 89)

    # def test_str_id(self):
    #     b3 = BaseModel()
    #     self.assertEqual(type(b3.iid), str)
    #     self.assertEqual(type(b3.created_at), datetime)
    #     self.assertEqual(type(b3.updated_at), datetime)

    def test_update_time(self):
        b4 = BaseModel()
        self.assertEqual(b4.created_at, b4.updated_at)
        sleep(1)
        b4.save()
        self.assertNotEqual(b4.created_at, b4.updated_at)

if __name__ == '__main__':
    unittest.main()