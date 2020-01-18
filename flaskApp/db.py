import click
import MySQLdb
from flask import current_app,g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = MySQLdb.connect(host=current_app.config['HOST'],
                               user= current_app.config['USER'],
                               passwd= current_app.config['PASSWORD'],
                               db=current_app.config['DATABASE'],)
        g.db.cursor = g.db.cursor()

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.cursor.close()
        db.close()


def init_db():
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.cursor.execute(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
