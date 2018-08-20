from flask import Flask
from flask_migrate import Migrate
from server.database import db

app = Flask(__name__, instance_relative_config=True)
app.logger.info('Server initialized')

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app.config.from_object(Config)
app.config.from_pyfile('application.cfg', silent=True)
app.logger.info('Configuration loaded')
app.logger.debug(app.config)

db.init_app(app)
migrate = Migrate(app, db)
app.logger.info('Database initialized at ' + app.config['SQLALCHEMY_DATABASE_URI'])
app.logger.info('Server ready')

@app.cli.command('dbinit')
def create_database():
    app.logger.info('Creating Database...')
    db.create_all()
    app.logger.info('Database Created')


@app.route("/")
def hello():
    return "Hello World!"
