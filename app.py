from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/index')     # whether user is directed to index.html or home.html should depend on if they are signed in
def index():
    return render_template("index.html")


@app.route('/login')
def login():
    # credentials check here
    return render_template("login.html")

# TODO: Add a route for all pages referenced in the HTML templates, including the register page


if __name__ == '__main__':
    app.run()