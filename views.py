from flask import render_template, request, redirect
from app import app
import random

@app.route('/')
def index():
    pic = str("static/images/image_" + str(random.randrange(0,827)) + ".jpg")
    return render_template('index.html', image=pic)

@app.route('/search', methods = ['POST'])
def search():
    url = ""
    if request.method == 'POST':
        text = str(request.form['text'])

        #search keyword override
        if text[0:3] == "yt ":
            url = "https://www.youtube.com/results?search_query="
            text = text[3:]
        elif text[0:5] == "goog ":
            url = "https://www.google.com/search?q="
            text = text[5:]
        elif text[0:2] == "r ":
            url = "https://www.reddit.com/r/"
            text = text[2:]
        elif text[0:3] == "rd ":
            url = "https://www.reddit.com/search/?q="
            text = text[3:]
        
        #normal search using bing for those bing points :)
        else:
            url = "https://www.bing.com/search?q="
            print(text)

        return redirect(url + text)
        