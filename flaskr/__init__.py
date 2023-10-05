import os
from flask import Flask

def create_app(test_config=None):
  # create our app and configure it here
  app = Flask(__name__, instance_relative_config=True) # create the Flask instance and tell it to use the __name__ of the current Python module as the name to import resources from
  app.config.from_mapping(
    SECRET_KEY='dev', # override the default configuration with values taken from the config.py file in the instance folder if it exists
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # sets the path where the SQLite database file will be saved
  )

  if test_config is None:
    # load the instance config, if it exists, for when we are NOT testing the application
    app.config.from_pyfile('config.py', silent=True) # silent argument tells Flask to not complain if no such file exists
  else:
    # load the test =config if passed in
    app.config.from_mapping(test_config) 
  # checking if the instance folder exists
  try:
    os.makedirs(app.instance_path) # ensure that app.instance_path exists or create it if it doesn't
  except OSError: # the OSError exception is raised if a directory exists
    pass # if the directory exists, do nothing

    # create our simple intro page
    @app.route('/setup')
    def setup():
      return 'Hello you have not broken your page yet'
    
    return app
