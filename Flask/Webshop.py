from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Unserer Webshop</h1>"

@app.route('/class/<Klassenname>')
def hello(Klassenname):
    return f'<h1>Willkommen auf der Klassenseite der {Klassenname} </h1>'
@app.route('/hello/')




@app.route('/Tic/')
def Tic():
    return render_template('')



if __name__ == '__main__':
    app.run(debug=False)




