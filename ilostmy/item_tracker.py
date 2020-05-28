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
        'SELECT * FROM item ORDER BY created DESC'
        # ' ORDER BY item_type DESC'
    ).fetchall()
    # # if bp.debug:
    # from pprint import pprint as pp
    # print(type(items))
    # print(type(items[0]))
    # pp(items[0])

    return render_template('item_tracker/index.html', items=items)


def item_create():
    # from pprint import pp
    # pp(request.form)
    # print(request.form)

    item_type = request.form['item_type']
    email = request.form['email']
    item_name = request.form['item_name']
    info = request.form['info']
    author = request.form['author']
    sighting_time = request.form['sighting_time']
    place = request.form['place']
    errors = []

    if not item_name:
        errors.append("Item is required.")
    elif not item_type:
        errors.append("Item type is required.")
    elif not email:
        errors.append("Email is required.")

    if info == '':
        info = None
    if author == '':
        author = None
    if sighting_time == '':
        sighting_time = None
    if place == '':
        place = None

    if errors != []:
        flash(' '.join(errors))
    else:
        db = get_db()
        item_id = db.execute(
            'INSERT INTO item (item_type, email, item_name, info, author, sighting_time, place, resolved) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
            (item_type, email, item_name, info, author, sighting_time, place, 0)
        ).lastrowid
        db.commit()
        # print(f"item_id: {item_id}")
        return redirect(url_for('item_tracker.item', item_id=item_id))


@bp.route('/create_lost_item', methods=('GET', 'POST'))
def create_lost():
    if request.method == 'POST':
        return item_create()
    return render_template('item_tracker/create_lost.html')


@bp.route('/create_found_item', methods=('GET', 'POST'))
def create_found():
    if request.method == 'POST':
        return item_create()
    return render_template('item_tracker/create_found.html')


@bp.route('/item/<int:item_id>')
def item(item_id):
    item = get_db().execute(
        'SELECT * FROM item WHERE id=?',
        (item_id,)
    ).fetchone()

    return render_template('item_tracker/item.html', item=item)
