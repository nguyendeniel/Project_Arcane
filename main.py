from flask import Flask, render_template
from config import SqlConfig
import pymysql


app = Flask(__name__)
root = SqlConfig('localhost', 3306, 'root', 'cookingpie1998', 'db_website')
host, port, user, password, db_name = root.user_param

try:
    connection = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=password,
        database=db_name)
    print('all okay')
except Exception as exes:
    print('Not okay')
    print(exes)


@app.route("/", methods=["GET"])
def present_main_page():
    return render_template('main_page.html')


@app.route("/about_me", methods=["GET"])
def present_about_me():
    return render_template('about_me.html')


@app.route("/projects", methods=["GET"])
def present_projects():
    return render_template('projects.html')


@app.route("/stack", methods=["GET"])
def present_stack():
    return render_template('stack.html')


app.run(debug=True, port=3000, host='localhost')
