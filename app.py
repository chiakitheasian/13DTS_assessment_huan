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

@app.route('/signup', methods = ['POST', 'GET'])
def render_signup_page():
    if request.method == 'POST':
        fname = request.form.get(user_fname).title().strip()
        lname = request.form.get(user_lname).title().strip()
        email = request.form.get(user_email).title().strip()
        password = reques.form.get(user_password)
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
