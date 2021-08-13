import os
import random
import datetime

from WCFunction import generateWordCloud
from flask import Flask, render_template, request, redirect, url_for, flash, send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = os.path.abspath(__file__)
UPLOAD_FOLDER = os.path.dirname(UPLOAD_FOLDER)

ALLOWED_EXTENSIONS = {'txt', 'md'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = str(random.random())

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def getImage():
    image = "./img/temp.png"
    image = os.path.abspath(image)
    return image

@app.route('/')
def root():
    return render_template('index.html')

@app.route('/serveImg/', methods=['GET', 'POST'])
def serveImage():
    image = getImage()
    return send_file(image, mimetype='image/png')

@app.route('/upload/', methods=['GET', 'POST'])
def submitClicked():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('root'))
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            generateWordCloud(filename)
            return redirect(url_for('serveImage'))


if __name__ == '__main__':
   app.run(host='127.0.0.1', port=8080, debug=True)
