from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')

@app.route('/menu')
def render_menu():

    return render_template('menu.html')

@app.route('/contact')
def render_contact():

    return render_template('contact.html')

@app.route('/login', methods = ['POST', 'GET'])
def render_login_page():
    return render_template('login.html')

@app.route('/signup', methods = ['POST', 'GET'])
def render_signup_page():
    if request.method == 'POST':
        fname = request.form.form.get('user_fname').title().strip
        lname = request.form.form.get('user_lname').title().strip
        email = request.form.form.get('user_email').lower().strip
        password = request.form.form.get('user_password')
        password2 = request.form.form.get('user_password2')

        if password != password2:
            return redirect("\signup?error=passwors+do+not+match")

        if len(password) < 8:
            return redirect("\signup?error=password+must+be+more+than+8+characters")
    return render_template('signup.html')

if __name__ == '__main__':
    app.run()
