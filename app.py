from flask import Flask, request, url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index Page</h1>"

@app.route('/hello')
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def profile(username):
    return f"{escape(username)}'s profile"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))