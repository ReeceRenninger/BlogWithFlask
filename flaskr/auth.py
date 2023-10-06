import functools # functools is a module that contains tools for working with functions and other callable objects

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth') # creates a Blueprint named 'auth'. Like the application object, the blueprint needs to know where it's defined, so __name__ is passed as the second argument. The url_prefix will be prepended to all the URLs associated with the blueprint

#TODO: write a view function for registering a new user
@bp.route('/register', methods=('GET', 'POST'))
def register():
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    db = get_db() # get a database connection
    error = None # error variable to store any errors that occur while validating the input

  if not username: # check if username was submitted
    error = 'Username is required.'
  elif not password: # check if password was submitted
    error = 'Password is required.'

  if error is None:
      try:
        db.execute(
        "INSERT INTO user (username, password) VALUES (?, ?)", # using SQL INSERT statement to insert the new user data into the database the ? marks are placeholders for values that we will specify later
        (username, generate_password_hash(password)) # generate_password_hash() is used to securely hash the password, which will be stored in the database
        )
        db.commit() # commit the changes to the database
      except db.IntegrityError:
        error = f"user {username} is already registered." # if the username already exists, an error is displayed
      else:
        return redirect(url_for('auth.login')) # if the username is available, the user is redirected to the login page
  flash(error) # if the username or password is missing or already taken, the appropriate message is displayed
  return render_template('auth/register.html') #TODO: NEED TO BUILD THIS TEMPLATE FILE

#TODO: write a submit form for registering a new user