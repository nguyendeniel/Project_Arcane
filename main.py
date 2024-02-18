from flask import Flask, render_template


app = Flask(__name__)


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

