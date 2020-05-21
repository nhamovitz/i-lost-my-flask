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
        'SELECT id, created, item_type, email, title, body, author, username, last_seen_time, place'
        'FROM item'
        ' ORDER BY created DESC'
        # ' ORDER BY item_type DESC'
    ).fetchall()
    if bp.debug:
        from pprint import pprint as pp
        print(type(items))
        print(type(items[0]))
        pp(items[0])

    return render_template('blog/index.html', items=items)
