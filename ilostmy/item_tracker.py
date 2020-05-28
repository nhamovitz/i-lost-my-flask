from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from ilostmy.db import get_db

from ilostmy.util import pprint_iso_date

bp = Blueprint('item_tracker', __name__)


def list_items(page_name, resolved):
    db = get_db()
    items = db.execute(
        'SELECT * FROM item WHERE resolved = ? ORDER BY created DESC',
        (int(resolved),)
    ).fetchall()

    return render_template('item_tracker/list_items.html', items=items, page_name=page_name)


@bp.route('/')
def index():
    return list_items("Outstanding items", False)


@bp.route('/resolved')
def resolved():
    return list_items("Previously resolved items", True)


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

    try:
        pprint_iso_date(sighting_time)
    except ValueError:
        errors.append("Invalid sighting date")

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


@bp.route('/item/<int:item_id>/resolve', methods=('POST',))
def resolve(item_id):
    db = get_db()
    db.execute(
        'UPDATE item SET resolved = ? WHERE id = ?',
        (1, item_id)
    )
    db.commit()
    return redirect(url_for('item_tracker.item', item_id=item_id))
