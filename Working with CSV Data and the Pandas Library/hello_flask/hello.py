from flask import Flask
import functools

app = Flask(__name__)

def make_bold(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        return '<b>' + func(*args,**kwargs) + '</b>'
    return wrapper


@app.route('/')
@make_bold
def hello_world():
    return '<h1> Hello Neerya </h1> \
        <p> This is a paragraph </p>'
        

@app.route("/bye")
def bye():
    return 'Bye!'

@app.route("/username/<name>/<int:number>")
def greet(name,number):
    return f'Hello there {name}, your are {number} is old'

if __name__ == "__main__":
    app.run(debug = True)
