
from flask import Flask, render_template, request, send_from_directory
from flask_ngrok import run_with_ngrok
#from werkzeug.utils import secure_filename
import os
#from PIL import Image
#import sys
from search import fe, feature_scores, feature_scores_1, feature_scores_2
from keras.preprocessing.image import load_img
import cv2
#import matplotlib.pyplot as plt


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
        result, id = feature_scores(query)

        for img in result:

            img1 = cv2.imread('./static/images/'+str(img))
            # print('###########################################################',img)
            img2 = cv2.imread('./static/uploads/'+img_name)
            dif1 = cv2.calcHist([img1],[0],None,[256],[0,256])
            dif2 = cv2.calcHist([img2],[0],None,[256],[0,256])
            res = cv2.compareHist(dif1, dif2, cv2.HISTCMP_BHATTACHARYYA)
            # print('###########################################################',res)

        ################
        ################
        threshold = 0.4
        ################
        ################

        result_final = []

        ###########################################################
        result_2, id_2 = feature_scores_2(query)

        result_final_2 = []
        for img in result_2:
            result_final_2.append("images/"+img)

        p_id_2 = []
        for value in id_2:
            p_id_2.append(value)

        final_result_2 = dict(zip(result_final_2, p_id_2))
        ############################################################

        if res <= threshold:

            sift = cv2.xfeatures2d.SIFT_create()

            kp1, des1 = sift.detectAndCompute(img1,None)
            kp2, des2 = sift.detectAndCompute(img2,None)
            # BF(brute force)Matcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1,des2, k=2)
            # Apply ratio test
            good = []
            for m,n in matches:
                if m.distance < 0.3*n.distance:
                    good.append([m])
            #print("##################################################",good)
            if len(good) == 0:
                return render_template("result1.html",image_name = img_name, result_paths_2 = final_result_2)
            else:
                for img in result:
                    result_final.append("images/"+img)            
        else:
            return render_template("result1.html",image_name = img_name, result_paths_2 = final_result_2)

        
        # id = product_id(query)
        p_id = []
        for value in id:
            p_id.append(value)

        # result_final = []
        # for img in final_val:
        #     result_final.append("images/"+img)

        final_result = dict(zip(result_final, p_id))

        ####################################################
        result_1, id_1 = feature_scores_1(query)

        result_final_1 = []
        for img in result_1:
            result_final_1.append("images/"+img)

        p_id_1 = []
        for value in id_1:
            p_id_1.append(value)

        final_result_1 = dict(zip(result_final_1, p_id_1))
        #######################################################

    return render_template("result.html",image_name = img_name, result_paths = final_result, result_paths_1 = final_result_1)

@app.route("/static/uploads/<filename>")
def send_image(filename):
	return send_from_directory("./static/uploads/", filename)
    
app.run()