from flask import Flask, render_template,request
import joblib

model = joblib.load('hiring_model.pkl')

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("form.html")

@app.route('/predict', methods=['post'])
def predict():
    
    exp= request.form.get('number')
    tst= request.form.get('number')
    itr= request.form.get('number')

    prediction = model.predict([[exp,tst,itr]])
    output = round(prediction[0],2)


    return render_template('form.html', prediction = f'employee salary in $ {output}')

if __name__ == '__main__':
    app.run(debug=True)
""" else:
    print("File not found")   """  



