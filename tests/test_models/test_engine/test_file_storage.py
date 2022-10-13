#!/usr/bin/python3
"""Testerino"""

from mmap import PAGESIZE
import unittest
import models
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class test_filestorage(unittest.TestCase):
    """Testerino"""
    def test_file_exists(self):
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_obj(self):
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_All(self):
        a = storage.all()
        self.assertEqual(type(a), dict)

    def test_reload(self):
        self.assertRaises(FileNotFoundError, storage.reload())

    def new(self):
        a = storage.all()
        storage.new(BaseModel)
        self.assertNotEqual(a, storage.all())

    def save(self):
        pass
