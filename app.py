import json

from flask import Flask, render_template

# app is just a variable to be instance of the Flask class
app = Flask(__name__)

app.SECRET_KEY = 'some_secret'



@app.route('/')  # this will refer to the home page of our website
# we need to run the home page: home orthers may name index
# the way to define or call any page is using pure py function:
def home():
    # we don't want to just return a one message
    # return '<h2>Hello, World one more time, good to see you again with Flask Framework!<h2>'
    # we want to return a full html page!
    module_name = "Practical Python"
    page_title = "Flask Framework Website"
    copyright = "copyright 2020 - Practical Python Module - Canadian Business College"
    return render_template('index.html', module_name=module_name, title=page_title, cr=copyright)


# Home page "/" 

# creating more pages:
@app.route('/about')
def about():
   
    return render_template('about.html')


# page with data
@app.route('/new')
def new():
    data = []
    with open("data/aristotle.json", "r") as aristotle_json_data:
        data = json.load(aristotle_json_data)
    print(data)
    return render_template('new.html', aristotle=data)


# step 1 : we need to specify the route name
@app.route('/more')  # http://127.0.0.1:5000/more
# step 2: creating the view=(function)
def more():
    # we want this function to return an html page named "more.html"
    return render_template('more.html')


# page with game
@app.route('/game')  # http://127.0.0.1:5000/game
# step 2: creating the view=(function)
def game():
    # we want this function to return an html page named "more.html"
    return render_template('game.html')



@app.route("/register")
def register():
   
    return render_template('register.html')

#@app.route("/register", methods=["GET"],["POST"])
#def register():
#    if request.method = "POST":


#print(request.form["name"])

#    return render_template('register.html')





#Flash ("thank you {}, your message is here", format(request.form["name"]))

# any_name() it is a function (method) because it has an opening and closing (    )

#!!!
# MVC: Model View Controler
# Model: the data we want to display(from data base)
# View: the html page that we need to view to the user
# Controller: is the current app.py file
