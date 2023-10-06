# creating a SQLite database using Python’s sqlite3 module
import sqlite3

import click # allows us to create custom commands for the flask command line application
from flask import current_app, g # g is a special object that is unique for each request, used to store data that might be accessed by multiple functions during the request

def get_db():
  if 'db' not in g:
    g.db = sqlite3.connect(
      current_app.config['DATABASE'], # current_app is another special object that points to the Flask application handling the request
      detect_types=sqlite3.PARSE_DECLTYPES 
    )
    g.db.row_factory = sqlite3.Row # tells the connection to return rows that behave like Python dictionaries
  
  return g.db

def close_db(e = None):
  db = g.pop('db', None) # checks if a connection was created by checking if g.db was set, if it was, close it
  if db is not None:
    db.close() # close the connection