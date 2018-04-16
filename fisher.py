from flask import Flask,make_response
from helper import is_isbn_or_key

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q,page):
    '''
    q :普通关键词和isbn
    page
    '''
    isbn_or_key = is_isbn_or_key(q)

    pass

#app.add_url_rule('/hello',view_func=hello)

if __name__ == "__main__":
    #生产环境 Nginx(接收浏览器请求然后转发给uwsgi)+uwsgi加载模块启动相关模块，生产环境不会执行app.run,保证生产环境不会启动自带服务器
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)