from flask import jsonify, request, flash, render_template
import json

from flask_login import current_user

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from . import web


@web.route('/book/search')
def search():
    '''
    q :普通关键词和isbn
    page
    ?q=金庸&page=1
    '''
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            yushu_book = YuShuBook()
            yushu_book.search_by_isbn(q)
        else:
            yushu_book = YuShuBook()
            yushu_book.search_by_keyword(q,page)

        books.fill(yushu_book,q)

        #dict序列化 API
        #return json.dumps(books,default=lambda o: o.__dict__)
        #return jsonify(books)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        #return jsonify(form.errors)

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    #取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(YuShuBook.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(isbn=isbn, launched=False).first():
           has_in_gifts=True
        if Wish.query.filter_by(isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn,launched = False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_gifts_wish = TradeInfo(trade_wishes)

    return render_template('book_detail.html',book = book,
                           wishes = trade_gifts_wish,gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts,has_in_wishes=has_in_wishes)

