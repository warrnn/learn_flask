from flask import Flask, request, url_for, render_template
from markupsafe import escape

# Flask Instance
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Index Page</h1>"

# String Parameters
@app.route('/user/<username>')
def profile(username):
    return f"{escape(username)}'s profile"

# Integer Parameters
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"Post {post_id}"

# Path Parameters
@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f"Subpath {escape(subpath)}"

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# URL Builder
with app.test_request_context():
    print(url_for('index'))
    # print(url_for('login'))
    # print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
    
# HTTP Methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Log In"
    else:
        return "Login Form"
    
# @app.get('/login')
# def login_get():
#     return "Login Form"

# @app.post('/login')
# def login_post():
#     return "Log In"

# Rendering Templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

# Accessing Request Data
with app.test_request_context('/hello', method='POST'):
    assert request.path == '/hello'
    assert request.method == 'POST'
    
# Reading Cookies
@app.route('/readcookie')
def cookie():
    username = request.cookies.get('username')
    return f"Hello, {username}"

# Storing Cookies
@app.route('/setcookie')
def setcookie():
    resp = app.make_response("<h1>Cookie Set</h1>")
    resp.set_cookie('username', "John Doe")
    return resp

# APIs with JSON
@app.route('/me')
def me_api():
    return {
        "username": "John Doe",
        "email": "johndoe@me.com",
    }