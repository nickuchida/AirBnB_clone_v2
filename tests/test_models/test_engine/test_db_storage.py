"""Tests the database storage module"""
import unittest
import os
import models.engine.db_storage
from models.state import State
from models import storage
import MySQLdb
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != "db", "Using filesystem\
                 storage instead of database")
class TestDBStorage(unittest.TestCase):
    """ Tests the db storage """

    @classmethod
    def setUp(self):
        """ Set up database connection """
        self.db = MySQLdb.connect(host="localhost", port=3306,
                                  user='hbnb_test', passwd='hbnb_test_pwd',
                                  db='hbnb_test_db', charset='utf8')

        self.cursor = self.db.cursor()
        self.storage = DBStorage()
        self.storage.reload()

    @classmethod
    def tearDown(self):
        """ Close connections """
        self.cursor.close()
        self.db.close()
