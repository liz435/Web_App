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


if __name__ == '__main__':
    print('running this cell')
    app.run(debug=True, host='0.0.0.0', port=5001)