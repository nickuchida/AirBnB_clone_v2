"""Tests the database storage module"""
import unittest
import os
import models.engine.db_storage
from models.state import State
from models import storage


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Using filesystem\
                 storage instead of database")
class TestDBStorage(unittest.TestCase):
    """ Tests the db storage """

    def test_new(self):
        """ Tests the `new` method """

