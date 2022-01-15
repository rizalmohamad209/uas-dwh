from app import app
from flask import render_template
from flask import request
from app.controllers import forecastController
# from app.models.user import User  # import kelas User dari model


@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'GET'):
        return render_template('index.html')


@app.route('/prediksi', methods=['POST'])
def predict():
    if (request.method == 'POST'):
        return forecastController.getPredictSalesInMonth()
