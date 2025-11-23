import numpy as np
import pickle
from flask import Flask,render_template,request
saved_model = r"D:\python\EDA_Workshop\model.pkl"
with open(saved_model,'rb') as file:
    model = pickle.load(saved_model)
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def predict():
    try:
        Age = int(request.form.get('Age'))
        Gender = int(request.form.get('Gender'))
        Polyuria=int(request.form.get('Polyuria'))
        Polydipsia= int(request.form.get('Polydipsia'))
        sudden_weight_loss= int(request.form.get('sudden_weight_loss'))
        weakness = int(request.form.get('weakness'))
        Polyphagia = int(request.form.get('Polyphagia'))
        Genital_thrush = int(request.form.get('Genital_thrush'))
        visual_blurring = int(request.form.get('visual_blurring'))
        Itching = int(request.form.get("Itching"))
        Irritability = int(request.form.get("Irritability"))
        delayed_healing = int(request.form.get('delayed_healing'))
        partial_paresis = int(request.form.get('partial_paresis'))
        muscle_stiffness = int(request.form.get('muscle_stiffness'))
        Alopecia=int(request.form.get('Alopecia'))
        Obesity = int(request.form.get('Obesity'))
        
        input_data = np.array(Age,Gender,Polyuria,Polydipsia,sudden_weight_loss,weakness,Polyphagia,Genital_thrush,visual_blurring,Itching,Irritability,delayed_healing,partial_paresis,muscle_stiffness,Alopecia,Obesity)

        predictions = model.predict(input_data)
        
        if predictions[0] == 0:
            result = 'No Diabetes'
        else:
            result = 'Diabetes'
        return render_template('index.html',result=result)
    except Exception as e:
        return f"{e} error has occured"
    
if __name__ == "__main__":
    app.run(debug=True)
