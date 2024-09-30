

from flask import Flask, render_template, request, redirect, url_for
import json
import random

app = Flask(__name__)
 #eröffnet die datei artikel und encodet in und packt ihn in die var f
with open('Artikel.json', encoding='utf-8') as f:
    data = json.load(f)



@app.route('/')
def Tic():
    return redirect(url_for('sky'))


@app.route('/Skybase')
def sky():
    #nimmt hier 4 random items aus der data(artikel liste) raus und setzt sie dan in items raus
    #random.samples erstellt 4 random listen mit random items aus data
    random_data = random.sample(list(data.items()),4)

    return render_template('Webshop.html', items=data, go=random_data)

@app.route('/Skybase/<Kategorie>')
def Kato(Kategorie):
    fil_kategorie = {}
    for name, item in data.items():
        if item['kategorie'] == Kategorie:  # Vergleicht die übergebene Kategorie mit der Kategorie im Item
            fil_kategorie[name] = item

    return render_template('Kategorie.html', items=fil_kategorie)




@app.route('/Suche', methods=['GET'])
def Suche():
    Error = None
    Suche = request.args.get('Suche').lower()

    # Erstelle ein leeres Dictionary für die gefilterten Kategorien
    fil_kategorie = {}

    # Durchlaufe jedes Item in 'data'
    for name, item in data.items():
        # Überprüfe, ob der Suchbegriff im Namen oder in der Herkunft des Items vorkommt
        if Suche in name.lower() or Suche in item['herkunft'].lower():
            # Füge das Item zum neuen Dictionary hinzu, wenn die Bedingung erfüllt ist
            fil_kategorie[name] = item
    return render_template('Kategorie.html', items=fil_kategorie, error=Error)



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




