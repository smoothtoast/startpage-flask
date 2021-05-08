from flask import render_template, request
from app import app
import random

@app.route('/')
def index():
    pic = str("static/images/image_" + str(random.randrange(0,827)) + ".jpg")
    url = "http://www.duckduckgo.com"
    name = "q"
    return render_template('index.html', image=pic, url=url, name=name)
