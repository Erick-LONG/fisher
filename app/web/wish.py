from flask import flash, redirect, url_for
from flask_login import login_required, current_user

from app.models.base import db
from app.models.wish import Wish
from . import web

__author__ = '七月'


@web.route('/my/wish')
def my_wish():
    pass


@web.route('/wish/book/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        #事务
        # try:
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已经添加过了，不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/satisfy/wish/<int:wid>')
def satisfy_wish(wid):
    pass


@web.route('/wish/book/<isbn>/redraw')
def redraw_from_wish(isbn):
    pass
