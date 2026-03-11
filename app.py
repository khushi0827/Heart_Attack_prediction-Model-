import joblib
from flask import Flask , render_template  ,  request , jsonify
import numpy as np

app = Flask(__name__)

model = joblib.load('Heart_attack_prediction.pkl')

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    data = request.get_json()
    features = [
        float(data['age']),
        float(data['sex']),
        float(data['cp']),
        float(data['trestbps']),
        float(data['chol']),
        float(data['fbs']),
        float(data['restecg']),
        float(data['thalach']),
        float(data['exang']),
        float(data['oldpeak']),
        float(data['slope']),
        float(data['ca']),
        float(data['thal'])
    ]
    features =  np.array(features).reshape(1,-1)
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0]
    prob_no =  round(probability[0]*100,1)
    prob_yes = round(probability[1]*100,1)
    if prediction==1:
        result = "High Risk of Heart Attack"
    else:
        result = "Low Risk of Heart Attack"
    return jsonify({
        "prediction":result,
        "prob_yes":prob_yes,
        "prob_no":prob_no,
    })  
if __name__ == "__main__":
    app.run(debug=True)