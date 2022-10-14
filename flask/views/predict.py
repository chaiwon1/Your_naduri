from flask import Blueprint, render_template, request
import numpy as np
import pickle


model = pickle.load(open('model.pkl', 'rb'))

predict_bp = Blueprint('predict', __name__)
@predict_bp.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET' :
        return render_template('predict.html')

    if request.method == 'POST' :
        try : 
            data1 = float(request.form['평균기온'])
            data2 = float(request.form['최저기온'])
            data3 = float(request.form['최고기온'])
            data4 = float(request.form['합계일조시간'])
            data5 = float(request.form['평균풍속'])
            data6 = float(request.form['평균상대습도'])

            arr = np.array([[data1, data2, data3, data4, data5, data6]])
            pred = model.predict(arr)
            pred = round(pred[0])

            return render_template('predict_result.html', pred=pred)
            
        except :
            return render_template("404.html")