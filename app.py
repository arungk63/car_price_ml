from flask import Flask,render_template,request

import joblib
import pandas as pd

app =Flask(__name__)

@app.route('/')
def base():
    return render_template('home_new.html')

@app.route('/predict', methods = ['post'])

def predict():
    
    model_pred = joblib.load('price_job.pkl')
    
    model = request.form.get('model')
    company  = request.form.get('company')
    year = request.form.get('year')
    kms = request.form.get('kms')
    fuel = request.form.get('fuel')
    
    print(model)
    print(company)
    print(year)
    print(kms)
    print(fuel)
    
    data={'name': model ,'company': company ,'year': year,'kms_driven':kms,'fuel_type' : fuel}
    
    input_data = pd.DataFrame(data=data, index=[0])
    print(input_data)
    
    output = model_pred.predict(input_data)
    
    price = round (output[0],2)
    
    
    return render_template('result.html', data = price )
    
    

app.run(debug=True)