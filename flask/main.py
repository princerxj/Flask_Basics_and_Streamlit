from flask import Flask, render_template
'''
It creates the instance of the Flask Class, 
which will be our WSGI (Web Server Gateway Interface) application.
'''
#### WSGI Application
app = Flask(__name__)

@app.route("/")
def welcome() :
    return "<html><h1>Welcome to the flask Course.</h1></html>"

@app.route("/index")
def welcomeIndex() :
    return render_template('index.html')

@app.route("/about")
def about() :
    return render_template('about.html')

if __name__ == "__main__": #Entry point of any py file - Execution Starts from here
    app.run(debug = True)