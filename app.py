from chicken_disease_classification.pipeline.predict import PredictionPipeline
from flask import Flask , request, jsonify,render_template
from flask_cors import CORS,cross_origin
from chicken_disease_classification.utils.common import decodeImage
from chicken_disease_classification.constants import *
import os

os.environ["LANG"] = "en_US.UTF-8"
os.environ["LC_ALL"] = "en_US.UTF-8"

app = Flask(__name__)
# The following line enables Cross-Origin Resource Sharing (CORS) for the Flask app,
# allowing it to accept requests from different origins, which is useful for APIs
# that need to be accessed from web applications hosted on different domains.
CORS(app)


class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)
        
        
@app.route("/",methods=["GET"])
@cross_origin()
def home():
    return render_template("index.html")

@app.route("/train",methods=["GET"])
@cross_origin()
def train():
    os.system("python main.py")
    return "Training successful!"


@app.route("/predict", methods=['POST'])
@cross_origin()
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predict()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    # app.run(host='0.0.0.0', port=8080) #local host
    # app.run(host='0.0.0.0', port=8080) #for AWS
    app.run(host='0.0.0.0', port=80) #for AZURE

