from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ilostmy.db import get_db

bp = Blueprint('item_tracker', __name__)


@bp.route('/')
def index():
    db = get_db()
    items = db.execute(
        'SELECT *'
        'FROM item'
        ' ORDER BY created DESC'
        # ' ORDER BY item_type DESC'
    ).fetchall()
    # # if bp.debug:
    # from pprint import pprint as pp
    # print(type(items))
    # print(type(items[0]))
    # pp(items[0])

    return render_template('item_tracker/index.html', items=items)


def item_create():
    item_type = request.form['item-type']
    email = request.form['email']
    title = request.form['title']
    body = request.form['body']
    author = request.form['author']
    last_seen_time = request.form['last_seen_time']
    place = request.form['place']
    errors = []

    if not title:
        errors.append("Title is required.")
    elif not item_type:
        errors.append("Item type is required.")
    elif not email:
        errors.append("Email is required.")

    if body == '':
        body = None
    if author == '':
        author = None
    if last_seen_time == '':
        last_seen_time = None
    if place == '':
        place = None

    if errors is not []:
        flash(' '.join(errors))
    else:
        db = get_db()
        db.execute(
            'INSERT INTO post (created, item_type, email, title, body, author, last_seen_time)'
            ' VALUES (?, ?, ?)',
            (created, item_type, email, title, body, author, last_seen_time)
        )
        db.commit()
        item_id = db.execute('SELECT last_insert_rowid()').fetchone()
        return redirect(url_for('item_tracker.item', id=item_id))


@bp.route('/create_lost_item', methods=('GET', 'POST'))
def create_lost():
    if request.method == 'POST':
        item_create()
    return render_template('item_tracker/create_lost.html')


@bp.route('/create_found_item', methods=('GET', 'POST'))
def create_found():
    if request.method == 'POST':
        item_create()
    return render_template('item_tracker/create_found.html')
