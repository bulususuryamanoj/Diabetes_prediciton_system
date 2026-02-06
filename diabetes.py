import pickle
from flask import Flask,render_template,request
saved_model = "model.pkl"
with open(saved_model,'rb') as file:
    model = pickle.load(file)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods = ['POST'])
def predict():
    age = int(request.form['Age'])
    gender = int(request.form['Gender'])
    polyuria = int(request.form['Polyuria'])
    polydipsia = int(request.form['Polydipsia'])
    sudden_weight_loss = int(request.form['sudden_weight_loss'])
    weakness = int(request.form['weakness'])
    polyphagia = int(request.form['Polyphagia'])
    genital_thrush = int(request.form['Genital_thrush'])
    visual_blurring = int(request.form['visual_blurring'])
    itching = int(request.form['Itching'])
    irritability = int(request.form['Irritability'])
    delayed_healing = int(request.form['delayed_healing'])
    partial_paresis = int(request.form['partial_paresis'])
    muscle_stiffness = int(request.form['muscle_stiffness'])
    alopecia = int(request.form['Alopecia'])
    obesity = int(request.form['Obesity'])

    input_data = [[
        age, gender, polyuria, polydipsia, sudden_weight_loss, weakness,
        polyphagia, genital_thrush, visual_blurring, itching, irritability,
        delayed_healing, partial_paresis, muscle_stiffness, alopecia, obesity
    ]]

    prediction = int(model.predict(input_data)[0])

    return render_template(
        'result.html',
        prediction=prediction,
        age=age,
        gender=gender,
        polyuria=polyuria,
        polydipsia=polydipsia,
        sudden_weight_loss=sudden_weight_loss,
        weakness=weakness,
        polyphagia=polyphagia,
        genital_thrush=genital_thrush,
        visual_blurring=visual_blurring,
        itching=itching,
        irritability=irritability,
        delayed_healing=delayed_healing,
        partial_paresis=partial_paresis,
        muscle_stiffness=muscle_stiffness,
        alopecia=alopecia,
        obesity=obesity
    )
if __name__ == "__main__":
    app.run(debug=False)