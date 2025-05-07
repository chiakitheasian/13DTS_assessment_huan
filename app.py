import sqlite3

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

DATABASE = 'health_DB'
def connect_database(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except Exception as e:
        print("Database connection failed:",e)
        return None
@app.route('/')
def render_homepage():  # put application's code here
    return render_template('home.html')

@app.route('/menu')
def render_menu():
    try:
        con = connect_database(DATABASE)
        query = "SELECT entry_date, mood, confidence_rating FROM entries"
        cur = con.cursor()
        cur.execute(query)
        entries_list = cur.fetchall()
        con.close()

        column_names = [desc[0] for desc in cur.description]
        entries = [dict(zip(column_names,row)) for row in entries_list]

        return render_template('menu.html', entries_list=entries_list)
    except Exception as e:
        return f"<h1>Error</h1><p>{e}</p>"

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
            return redirect("\signup?error=passwords+do+not+match")

        if len(password) < 8:
            return redirect("\signup?error=password+must+be+more+than+8+characters")

       #con = connect_database(DATABASE)
       #query_insert = "INSERT INTO user (first_name, last_name,email,password
    return render_template('signup.html')



if __name__ == '__main__':
    app.run()
