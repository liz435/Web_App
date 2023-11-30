from flask import Flask, render_template, request, url_for, redirect, jsonify
import numpy as py
import os
import subprocess
import mediapipe as mp

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



@app.route("/generate_images", methods=["GET"])
def generate_images():
    pkl_file = request.form.get("gan.pkl")
    folder_pkl_file = request.form.get("model")
    output_images_dest = request.form.get("output")
    seed_min = 3000
    num_images_generated = 1
    # Set up the output directory
    output_images_dest = "model/" + str(output_images_dest)
    if not os.path.exists(output_images_dest):
        os.makedirs(output_images_dest)

    # Generate the images
    url = str(folder_pkl_file) + "/" + str(pkl_file)
    command = "/model/gen_images.py --network={} --outdir={} --seeds={}".format(url, output_images_dest, seed_min, seed_min + num_images_generated - 1)
    subprocess.run(command.split())


    # Return a JSON response with the number of images generated
    return jsonify({"images_generated": num_images_generated})


if __name__ == '__main__':
    print('running this cell')
    app.run(debug=True, host='0.0.0.0', port=5001)