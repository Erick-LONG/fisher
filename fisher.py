from app import create_app

app = create_app()

if __name__ == "__main__":
    #生产环境 Nginx(接收浏览器请求然后转发给uwsgi)+uwsgi加载模块启动相关模块，生产环境不会执行app.run,保证生产环境不会启动自带服务器
    app.run(debug=app.config['DEBUG'],threaded=True)