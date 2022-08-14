# from flask import Flask,render_template,request
# import pickle
# import numpy as np
#
# model=pickle.load(open('iri.pkl','rb'))
#
# app=Flask(__name__)
#
# @app.route('/')
# def homepage():
#     # return "<h1>Helloo</h1>"
#     return render_template('home.html')
#
#
# # @app.route('/predict',method=['post'])
# @app.route('/predict')
# def home():
#     data1=request.form['a']
#     data2=request.form['b']
#     data3=request.form['c']
#     data4=request.form['d']
#
#     arr=np.array([[data1,data2,data3,data4]])
#     pred=model.predict(arr)
#     return render_template('after.html',data=pred)
#
# if __name__=="__main__":
#     app.run(debug=True)



# from crypt import methods
from flask import Flask,render_template,request
import pickle
import numpy as np

model=pickle.load(open('iri.pkl','rb'))

app=Flask(__name__)

# @app.route('/')
# def home():
#     return "<h1>Hello</h1>,"

@app.route('/')
def homepage():
    return render_template('home.html')

@app.route('/predict',methods=['POST'])
def home():
    data1=request.form['a']
    data2=request.form['b']
    data3=request.form['c']
    data4=request.form['d']

    arr=np.array([[data1,data2,data3,data4]])
    pred=model.predict(arr)
    return render_template('after.html',data=pred)


if __name__=="__main__":
    app.run(debug=True)