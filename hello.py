from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    # return '<h1>hello %s!</h1>' % name
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()
