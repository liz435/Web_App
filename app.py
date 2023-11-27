from flask import Flask, render_template, request, url_for, redirect
import numpy as py
import tensorflow as tf
import h5py


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/predict')
def predict():
    data = request.get_json()
    predictions = model.predict(data)
    response = jsonify({'predictions': predictions})
    return response


if __name__ == '__main__':
    app.run(debug=True)