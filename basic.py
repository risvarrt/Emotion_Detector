from flask import Flask,render_template,request,jsonify
import numpy as np
import cv2
import tensorflow as tf
import base64
import check
#import MUSIC


app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/cam')
def cam():
    return render_template("cam.html")


@app.route('/summa')
def summa():
    return render_template("summa.html")


@app.route('/submit')
def submit():
    answer=check.GetResult();
    if answer == 'Angry':
        return render_template("Angry.html")
    elif answer == 'Happy':
        return render_template("Happy.html")
    elif answer == 'Neutral':
        return render_template("Neutral.html")
    elif answer == 'Sad':
        return render_template("Sad.html")
    elif answer == 'Surprise':
        return render_template("Surprise.html")



@app.route('/angry')
def angry():
    #MUSIC.func()
    return 0


@app.route('/happy')
def happy():
    #MUSIC.func()
    return 0


@app.route('/neutral')
def neutral():
    #MUSIC.func()
    return 0


@app.route('/surprise')
def surprise():
    #MUSIC.func()
    return 0


@app.route('/sad')
def sad():
    #MUSIC.func()
    return 0


if __name__ == '__main__':
    app.run(debug=True)
