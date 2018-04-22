from . import web


@web.route('/')
def index():
    return 'xxx'

@web.route('/personal')
def persional_center():
    pass