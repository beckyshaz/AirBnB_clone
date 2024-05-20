#!/usr/bin/python3
"""creating a unique storage instance"""



from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
