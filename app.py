from flask import Flask, render_template, request, url_for, redirect, session

app = Flask(__name__)
app.config[DEBUG = True]

# Configuring the Database here


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def employee_login():
    return render_template('SIGNUP.html')


if __name__ == '__main__':
    app.run(debug=True)
