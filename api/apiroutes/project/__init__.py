from flask import Blueprint

projects = Blueprint('projects', __name__, url_prefix="/project")

from .routes import *