# This is a complete Flask web app that displays an HTML file 
# when you visit the website.
# Render = Convert code into something visible in a browser.




print()

from flask import Flask, render_template  # ← ADD render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':  # ← ADD THIS
    app.run(debug=True)     # ← ADD THIS


print()
# let's import the flask
from flask import Flask
import os # importing operating system module

app = Flask(__name__)

@app.route('/') # this decorator create the home route
def home ():
    return '<h1>Welcome</h1>'

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
    ## Simple Analogy 
# Basic Flask = Walkie-talkie that only works in your room

# Production Flask = Walkie-talkie that works anywhere (home, office, cloud)

# First code works only for you testing locally.
# Second code adds 3 things so a cloud platform (like Heroku) can run it:

# Reads the port number the cloud gives it

# Listens for traffic from anywhere (not just your computer)

# Works automatically whether on your machine or in the cloud

# Bottom line: First is for practice. Second is for putting your app live on the web.
## 🌐 The Modern Replacement for Heroku: Render.com
# Render is the closest free alternative to Heroku — 
# it works almost identically (push code → it goes live), 
# it's beginner-friendly, and it's specifically what the Python/Flask community
#  migrated to after Heroku killed its free tier.
# Render promises simple, automated deployment by just pushing code through 
# GitHub. Whether you're developing in Python, Node, Go, or Ruby, 
# there's well-written documentation for smooth deployment. 
# It also offers free SSL for all services.
# You can deploy a Flask app on Render in just a few clicks, 
# and every push to your linked GitHub branch automatically builds 
# and deploys your app.
