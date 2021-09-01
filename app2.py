# -*- coding: utf-8 -*-

from flask import Flask, request,  render_template
import model2 as m2
app = Flask(__name__)
mm =""
@app.route("/", methods =["POST","GET"])
def Home():
    if request.method == "POST":
        pele = request.form["peLe"]
        pewe = request.form["peWe"]
        sele = request.form["seLe"]
        sewe = request.form["seWe"]
        preds = m2.makePrediction(pele,pewe,sele,sewe)
        mm = preds
        print(preds)
    return render_template("indexx.html",pred = mm)
#@app.route('/sub', methods = ['POST'])
#def submit():
#    if request.method == "POST":
#        name = request.form["username"]
#        return render_template("sub.html", n =name)

if __name__ == "__main__":
    app.run(debug = True,use_reloader=False)