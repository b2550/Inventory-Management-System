from flask import Flask
from flask_migrate import Migrate
from server.database import db
from server.api import api

app = Flask(__name__, instance_relative_config=True)
app.logger.info('Server initialized')

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
app.config.from_pyfile('application.cfg', silent=True)
app.logger.info('Configuration loaded')
app.logger.debug('ENV: ' + str(app.config['ENV']))
app.logger.debug('DEBUG: ' + str(app.config['DEBUG']))
app.logger.debug('TESTING: ' + str(app.config['TESTING']))

db.init_app(app)
migrate = Migrate(app, db)
app.logger.info('Database initialized at ' + app.config['SQLALCHEMY_DATABASE_URI'])

app.register_blueprint(api)

app.logger.info('Server ready')

@app.cli.command('dbinit')
def create_database():
    app.logger.info('Creating Database...')
    db.create_all()
    app.logger.info('Database Created')


@app.route("/")
def hello():
    return "Hello World!"
