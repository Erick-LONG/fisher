from flask import Flask, current_app

app = Flask(__name__)
#应用上下文 对象 对Flask封装
#请求上下文 对象 对Request封装
# Flask AppContext 代理app核心对象
# Request RequestContext 代理request请求对象，先检查应用上下文的栈顶，如果没有，把app推送到栈中
#离线应用，单元测试，需要手动推入应用上下文，如果有请求上线文，flask会自动推入，否则，手动推入

ctx = app.app_context() #获取应用上下文
ctx.push() #入栈

a = current_app
d = current_app.config['DEBUG']

ctx.pop() #出栈