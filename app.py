from flask import Flask,render_template,request
from config import Config
from wordgen import gen

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    return app

app = create_app()

key = "wrongkey"
value = "wrongvalue"

@app.route('/',methods=['GET'])
def home():
    global key
    global value
    x = gen()
    key = x[0]
    value = x[1]
    return render_template('home.html',msg=key)

@app.route('/first',methods=['POST'])
def first():
    global key
    global value
    return render_template("home2.html",msg=key, msg2=value)


@app.route('/second',methods=['POST'])
def second():
    global key
    global value
    x = gen()
    key = x[0]
    value = x[1]
    return render_template('home.html',msg=key)

if __name__ == "__main__":
    app.run(port=80, debug=True)