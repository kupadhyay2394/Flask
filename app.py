from flask import Flask
'''
 It creates an instance of the Flask class, 
 which will be your WSGI (Web Server Gateway Interface) application.
'''
###WSGI Application
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this best Flask course.helloThis should be an amazing course"

@app.route("/index")
def index():
    return "Welcome to the index page"



'''entry point of py code'''
if __name__=="__main__":
    app.run(debug=True)
# debug true means that the server wiLL
#  automatically reload for code changes 
#  and show an interactive debugger in the browser if an error occurs.
