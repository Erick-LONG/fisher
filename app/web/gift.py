from flask import current_app, flash, redirect, url_for

from app.models.base import db
from app.models.gift import Gift
from . import web
from flask_login import login_required,current_user


@web.route('/my/gifts')
@login_required
def my_gift():
    uid = current_user.id
    gift_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gift_of_mine]
    Gift.get_wish_counts(isbn_list)
    return 'xxx'


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    if current_user.can_save_to_list(isbn):
        #事务
        # try:
        with db.auto_commit():
            gift = Gift()
            gift.isbn = isbn
            gift.uid = current_user.id
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            # db.session.commit()
        # except Exception as e:
        #     db.session.rollback()
        #     raise e
    else:
        flash('这本书已经添加过了，不要重复添加')
    return redirect(url_for('web.book_detail',isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass