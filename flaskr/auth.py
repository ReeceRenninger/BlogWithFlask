import functools # functools is a module that contains tools for working with functions and other callable objects

from flask import (
  Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db