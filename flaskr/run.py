from flask import Flask

from flaskr.views.index import index
from flaskr.views.upload import upload
from flaskr.views.action import action
from flaskr.views.songlister import songlister

from flaskr.models import initialize_database
from config import config


app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(upload)
app.register_blueprint(action)
app.register_blueprint(songlister)

def run():
    initialize_database()
    app.run(debug=True, host=config['host'])