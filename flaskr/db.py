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

def init_db(): 
  db = get_db() # get a database connection

  with current_app.open_resource('schema.sql') as f: # this is a special function that opens a file relative to the flaskr package thats targeting our schema.sql file
    db.executescript(f.read().decode('utf8')) # executescript() allows us to execute multiple SQL statements at once by passing in a string of SQL statements

@click.command('init-db') # defines a command line command called init-db that calls the init_db function and shows a success message to the user
def init_db_command():
  # clear the existing data and create new tables
  init_db()
  click.echo('Initialized the database.')

def close_db(e = None):
  db = g.pop('db', None) # checks if a connection was created by checking if g.db was set, if it was, close it
  if db is not None:
    db.close() # close the connection