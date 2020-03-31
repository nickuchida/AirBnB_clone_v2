#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import os

storage = None

if os.getenv("HBNB_TYPE_STORAG") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
