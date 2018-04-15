from flask import Flask,make_response

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    #基于类的视图（即插视图）
    #返回status code 200，404，301
    #返回content-type  http headers
    #content-type = text/html
    # 返回一个Response对象
    headers = {
        'content-type':'text/plain',
        'location':'http://www.bing.com'
    }
    # response = make_response('<html></html>',404)
    # response.headers = headers
    return '<html></html>',301,headers
    #return '<html></html>'

#app.add_url_rule('/hello',view_func=hello)

if __name__ == "__main__":
    #生产环境 Nginx(接收浏览器请求然后转发给uwsgi)+uwsgi加载模块启动相关模块，生产环境不会执行app.run,保证生产环境不会启动自带服务器
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)