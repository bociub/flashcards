from flask import Flask,render_template,request
from config import Config
from wordgen import gen

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = create_app()

x = True

# https://jinja.palletsprojects.com/en/3.0.x/templates/

@app.route('/',methods=['GET'])
def home():
    global x
    x = gen()
    return render_template('home.html',x=x)

@app.route('/first',methods=['POST'])
def first():
    global x
    return render_template("home2.html",x=x)


@app.route('/second',methods=['POST'])
def second():
    global x
    x = gen()
    return render_template('home.html',x=x)

if __name__ == "__main__":
    app.run(port=80, debug=True)