from flask import Flask 
'''
It creates the instance of the Flask Class, 
which will be our WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome() :
    return "Welcome to this best Flask Course. This should be an amazing course"

@app.route("/index")
def welcomeIndex() :
    return "Welcome to the index page"

if __name__ == "__main__": #Entry point of any py file - Execution Starts from here
    app.run(debug = True)