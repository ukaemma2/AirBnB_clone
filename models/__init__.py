#!/usr/bin/python3
'''__init__ magic method for model directiory'''
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
