

from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)

with open('Artikel.json', encoding='utf-8') as f:
    data = json.load(f)



@app.route('/')
def Tic():
    return redirect(url_for('sky'))


@app.route('/Skybase')
def sky():

    random_data = random.sample(list(data.items()),4)

    return render_template('Webshop.html', items=data, go=random_data)

@app.route('/Skybase/<Kategorie>')
def Kato(Kategorie):
    fil_kategorie = {}
    for name, item in data.items():
        if item['kategorie'] == Kategorie:  # Vergleicht die übergebene Kategorie mit der Kategorie im Item
            fil_kategorie[name] = item

    return render_template('Kategorie.html', items=fil_kategorie)




@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    filtered_items = {name: item for name, item in items.items() if query in name.lower() or query in item['beschreibung'].lower()}
    return render_template('partner.html', items=filtered_items)
'''
@app.route('/', methods=['POST', 'GET'])
def Tic():
    error = None
    Tic = ["", "", "",
           "", "", "",
           "", "", ""]

    if request.method == "POST":
        # Überprüfen, ob alle Felder gesendet wurden

        Tic = [ request.form['t1'], request.form['t2'], request.form['t3'],
                request.form['t4'], request.form['t5'], request.form['t6'],
                request.form['t7'], request.form['t8'], request.form['t9']
            ]
        print(Tic)



        return render_template("Tic.html", Tic=Tic, error=error)

    # Wenn GET-Anfrage, leeres Tic-Feld initialisieren
    return render_template("Tic.html", Tic=Tic, error=error)
'''


@app.route("/Skybase/Kategorien")
def Top_Items():
    return render_template("Kategorie.html")

@app.route("/Skybase/Partner")
def Partner():
    return render_template("Partner.html")


@app.route("/Skybase/Bestseller")
def Charts():
    return render_template("Bestseller.html", items=data)

@app.route("/Skybase/Warenkorb")
def Warenkorb():
    return render_template("Warenkorb.html")

@app.route("/Skybase/Impressum")
def Impressum():
    return render_template("Impressum.html")

@app.route("/Skybase/Prime")
def Prime():
    return render_template("Prime.html")

@app.route('/Skybase/<Artikel>')
def Arto(Artikel):
    fil_artikel = {}
    for name, item in data.items():
        if item['kategorie'] == Artikel:  # Vergleicht die übergebene Kategorie mit der Kategorie im Item
            fil_artikel[name] = item

    return render_template('Kategorie.html', items=fil_artikel)


if __name__ == '__main__':
    app.run(debug=True)




