from flask import Flask, render_template, request, redirect, url_for, make_response,jsonify
import os
app = Flask(__name__)

@app.route('/')
def home():
    img = '/static/images/yoobee.jpg'
    return render_template('index.html', img=img)

@app.route("/new")
def new_page():
    return render_template('new.html')

@app.route("/<name>/<int:age>")
def welcome(name, age):
    return f"welcome {name} who is {age} years old!"

@app.route("/upload", methods=["GET", "POST"])
def upload_images():
    f = request.files['file']
    basepath = os.path.dirname(__file__)
    upload_path = os.path.join(basepath, 'static/images', f.filename)
    f.save(upload_path)
    img = '/static/images/' + f.filename
    return render_template('index.html', img=img)


if __name__ == '__main__':
    app.run(debug=True)
