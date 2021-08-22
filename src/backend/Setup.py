import os 
from sys import platform
import sqlite3 
from .Encryption import hash 

fileName = "Passwords.db"
pathName = None # To avoid scope related.

if platform.lower().startswith('win'):
    pass
else:
    pathName = os.environ['HOME'] + '/.Simple-Password-Manager'

def setup(primaryPassword):
    pass 