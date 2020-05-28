import os

from flask import Flask

from datetime import date


def pprint_iso_date(datestring):
    return date.fromisoformat(datestring).strftime('%m/%d/%y')


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    # credit to https://stackoverflow.com/a/7226047/9221660
    app.jinja_env.globals.update(pprint_iso_date=pprint_iso_date)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'ilostmy.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app)

    from . import item_tracker
    app.register_blueprint(item_tracker.bp)
    app.add_url_rule('/', endpoint='index')

    return app
