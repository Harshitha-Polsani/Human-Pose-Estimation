from flask import Flask, render_template, request
from api import predict
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def upload_predict():
    imagefile = request.files['poseimage']
    filename = secure_filename(imagefile.filename)
    file_ext = os.path.splitext(filename)[1]
    if file_ext not in ['.jpg', '.jpeg', '.png']:
        return render_template('index.html', invalid_file=True)
    image_path = './images/' + filename
    imagefile.save(image_path)
    pose_label, encoded_img_or_error = predict(image_path)
    if pose_label is None:
        if encoded_img_or_error == "Pose landmarks not detected. Please upload a clear image.":
            return render_template('index.html', image_error="Pose landmarks not detected. Please upload a clear image.")
        elif encoded_img_or_error == "Image is too blurry. Please upload a clear image.":
            return render_template('index.html', image_error="Image is not clear or Blur Image. Please upload a clear image.")
        elif encoded_img_or_error == "Image is not clear or Blur Image. Please upload a clear image":
            return render_template('index.html', image_error="Image is not clear or Blur Image. Please upload a clear image.")
        else:
            return render_template('index.html', message=encoded_img_or_error)
    return render_template('result.html', pose_label=pose_label, encoded_img=encoded_img_or_error, filename=filename)

if __name__ == '__main__':
    app.run(debug=True, port=50002)
