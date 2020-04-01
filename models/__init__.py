#!/usr/bin/python3
"""create a unique FileStorage instance for your application"""
import os

storage = None

if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    print("Using db")
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    print("Using fs")

storage.reload()
