from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)





@app.route('/')
def Tic():
    return redirect(url_for('sky'))

@app.route('/skybase')
def sky():
    return render_template("webshop.html")



@app.route('/search')  # 'GET' is the default method, you don't need to mention it explicitly
def search():


    query = request.GET.get('search')  # try this instead

    req_search = Storage.query.filter_by(req_no=query)
    return render_template('search.html', req_search=req_search)
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





@app.route("/skybase/Top-Items")
def Top_Items():
    return render_template("Kategorie.html")

@app.route("/skybase/Charts")
def Charts():
    return render_template("Bestseller.html")

@app.route("/skybase/Warenkorb")
def Warenkorb():
    return render_template("Warenkorb.html")

@app.route("/skybase/Impressum")
def Impressum():
    return render_template("Impressum.html")






if __name__ == '__main__':
    app.run(debug=True)




