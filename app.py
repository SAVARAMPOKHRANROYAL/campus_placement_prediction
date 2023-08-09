import numpy as np
from flask import Flask, request, render_template
import pickle

flask_app = Flask(__name__)

model = pickle.load(open("Placement.pkl","rb"))

@flask_app.route("/")
def Home():
    return render_template("home.html")


@flask_app.route("/predict", methods = ["GET","POST"])  
def predict():
    b = request.form.get('gender')
    c = request.form.get('ssc_p')
    d = request.form.get('ssc_b')
    e = request.form.get('hsc_p')
    f = request.form.get('hsc_b')
    g = request.form.get('hsc_s')
    h = request.form.get('degree_p')
    i = request.form.get('degree_t')
    j = request.form.get('workex')
    k = request.form.get('etest_p')
    l = request.form.get('specialisation')
    m = request.form.get('mba_p')
    
    if b=='' or c=='' or d=='' or e=='' or f=='' or g=='' or h=='' or i=='' or j=='' or k=='' or l=='' or m=='':
        return "You can't leave any field empty!!!"

    b = int(b)
    c = float(c)
    d = int(d)
    e = float(e)
    f = int(f)
    g = int(g)
    h = float(h)
    i = int(i)
    j = int(j)
    k = float(k)
    l = int(l)
    m = float(m)

    arr_val=np.array([[b,c,d,e,f,g,h,i,j,k,l,m]])
    prediction = model.predict(arr_val)
    return render_template("after.html", data=prediction)

if __name__ == "__main__":
    flask_app.run(debug=True)