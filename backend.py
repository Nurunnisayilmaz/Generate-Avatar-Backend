import base64
import os
from flask import Flask, flash, request, send_file, url_for, redirect
from werkzeug.utils import secure_filename
import cv2
import photo2cartoon
import time
import numpy
from PIL import Image
import io
from flask_cors import CORS

UPLOAD_FOLDER = r'.\uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
CORS(app)


# helpers
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ai
c2p = photo2cartoon.Photo2Cartoon()


# routes
@app.route('/generateavatar', methods=['POST'])
def generateavatar():
    if 'img' in request.files:
        file = request.files['img']

        if file.filename == '':
            return 400, 'Eksik request'
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            path = "upload/" + filename
            file.save(path)

            # img = cv2.imdecode(numpy.fromstring(file.read(), numpy.uint8), cv2.COLOR_BGR2RGB)
            img = cv2.cvtColor(cv2.imread(path), cv2.COLOR_BGR2RGB)
            # img = file.stream.read()

            cartoon = c2p.inference(img)
            # cv2.imwrite("cartoon/test.jpg", cartoon)
            data = Image.fromarray(cartoon, 'RGB')

            img_io = io.BytesIO()
            data.save(img_io, 'JPEG', quality=100)
            #img_io.seek(0)

            #return send_file(img_io, mimetype='image/jpeg')
            return base64.b64encode(img_io.getvalue()).decode('utf-8')

        return "Error"
    else:
        return 400, 'Eksik request'


if __name__ == "__main__":
    app.run()
