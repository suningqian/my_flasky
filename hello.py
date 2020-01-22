from flask import Flask, request, render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    user_agent = request.headers.get('User_Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    # return '<h1>hello %s!</h1>' % name
    return render_template('user.html', name=name)


if __name__ == '__main__':
    manager.run()
