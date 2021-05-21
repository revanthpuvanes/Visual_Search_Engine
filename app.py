
from flask import Flask, render_template, request, send_from_directory, jsonify
from flask_ngrok import run_with_ngrok
#from werkzeug.utils import secure_filename
import os
#from PIL import Image
#import sys
from search import fe, feature_scores, product_id
from keras.preprocessing.image import load_img


APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)
run_with_ngrok(app)

UPLOAD_FOLDER = 'static/uploads/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
  
@app.route("/")
def home():
    return render_template('index.html')

@app.route("/upload", methods=['GET','POST'])
# def upload():
#   if request.method == 'POST':
#       f = request.files['file']
#       img_name = f.filename
#       f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
#       return render_template("result.html")
def upload():
    for img in request.files.getlist("file"):
	    img_name = img.filename
	    destination = "/".join([UPLOAD_FOLDER, img_name])
	    img.save(destination)
    if img_name == img.filename:
        #img = cv2.imread('/static/uploads/<image_name>',flags=3)
        img = load_img(('./static/uploads/'+img_name), target_size=(224, 224))
        #img = load_img(listdir(r'E:\projects\one\static\uploads', target_size=(224,224)))
        #img_name = img.filename
        query = fe.extract(img)
        #return query
        result = feature_scores(query)
        id = product_id(query)
        #id = product_id(query)
        p_id = []
        for value in id:
            p_id.append(value)

        # class final_result:
        #     def __init__(self, result, id):
        #         self.result = result
        #         self.id = id
        # results = []
        # results = final_result(result,id)

        result_final = []
        for img in result:
            result_final.append("images/"+img)

        # final_result = []
        # for a,b in list(zip(result_final, p_id)):
        #     final_result.append((a,b))
        final_result = dict(zip(result_final, p_id))

    return render_template("result.html",image_name = img_name, result_paths = final_result)

@app.route("/static/uploads/<filename>")
def send_image(filename):
	return send_from_directory("./static/uploads/", filename)
    
app.run()