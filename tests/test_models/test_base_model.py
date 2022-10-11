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

    def test_id(self):
        b1 = BaseModel()
        self.assertIsNotNone(b1.id)

    def test_created_at(self):
        b2 = BaseModel()
        b2.my_number = 89
        self.assertEqual(b2.my_number, 89)

    def test_to_dict(self):
        b3 = BaseModel()
        v = b3.__dict__
        self.assertEqual(type(v), type({}))

    # def test_update_time(self):
    #     b4 = BaseModel()
    #     self.assertEqual(b4.created_at, b4.updated_at)
    #     sleep(1)
    #     b4.save()
    #     self.assertNotEqual(b4.created_at, b4.updated_at)

    def test_str(self):
        b5 = BaseModel()
        f = f"[{b5.__class__.__name__}] ({b5.id}) {b5.__dict__}"
        p = str(b5.__str__)
        print("Lo de abajo es P")
        print(p)
        print("Lo de abajo NOOOOO")
        self.assertEqual(p, f)


if __name__ == '__main__':
    unittest.main()
