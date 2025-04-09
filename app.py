from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')

@app.route('/menu')
def render_menu():
    return render_template('menu.html')

@app.route('/login', methods = ['POST', 'GET'])
def render_login_page():
    return render_template('login.html')

if __name__ == '__main__':
    app.run()
