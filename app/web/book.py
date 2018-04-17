from flask import jsonify, request

from app.forms.book import SearchForm
from . import web
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@web.route('/book/search')
def search():
    '''
    q :普通关键词和isbn
    page
    ?q=金庸&page=1
    '''
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
            #dict序列化 API
        return jsonify(result)
    else:
        return jsonify(form.errors)