from flask import Flask

from .view import app
from . import models

models.db.init_app(app)