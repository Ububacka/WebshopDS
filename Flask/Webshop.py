from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)





@app.route('/')
def Tic():
    return redirect(url_for('sky'))

@app.route('/skybase')
def sky():
    return render_template("webshop.html")

@app.route("/skybase", methods=['POST', 'GET'])
def check():
    error=None
    oot = None
    if request.method == "POST":
        # Wenn der Bootstrap Button geklickt wurde
        if request.form['Top'] == 'Suche':
            return redirect(url_for('Top_Items'))  # Weiterleitung zur 'bootstrap' Route
            print(request.form['Top'])
    return render_template("webshop.html", oot=oot, error=error)  # GET-Anfragen laden einfach die Startseite

@app.route('/Tic', methods=['POST', 'GET'])
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



@app.route("/skybase/Top-Items")
def Top_Items():
    return render_template("Top-Items.html")


@app.route("/skybase/Charts")
def Charts():
    return render_template("Charts.html")




if __name__ == '__main__':
    app.run(debug=True)




