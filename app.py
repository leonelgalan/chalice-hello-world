from chalice import Chalice

app = Chalice(app_name='hello-world')


@app.route('/')
def index():
    app.log.debug('This is a debug statement')
    return {'hello': 'world'}

