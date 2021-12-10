from chalice import Chalice

app = Chalice(app_name='hello-world')


@app.route('/')
def index():
    app.log.error('This is a error statement')
    return {'hello': 'world'}

