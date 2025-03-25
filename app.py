from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from chicken_disease_classification.pipeline.predict import PredictionPipeline
from chicken_disease_classification.utils.common import decodeImage
from chicken_disease_classification.constants import *
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

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

# Initialize the app globally
clApp = ClientApp()

@app.route("/", methods=["GET"])
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
    try:
        # Check if request has JSON
        if not request.is_json:
            logger.error("Invalid request format")
            return jsonify({
                "status": "error",
                "message": "Invalid request format"
            }), 400

        # Get image from request
        image = request.json.get('image')
        if not image:
            logger.error("No image data received")
            return jsonify({
                "status": "error",
                "message": "No image data provided"
            }), 400

        # Decode and save image
        try:
            decodeImage(image, clApp.filename)
            logger.info("Image decoded successfully")
        except Exception as e:
            logger.error(f"Image decoding error: {str(e)}")
            return jsonify({
                "status": "error",
                "message": "Error processing image"
            }), 400

        # Make prediction
        try:
            result = clApp.classifier.predict()
            logger.info(f"Prediction result: {result}")

            if not result:
                raise ValueError("No prediction result")

            # Handle the case where result is a list
            if isinstance(result, list):
                prediction_dict = result[0] if result else {}
                prediction = prediction_dict.get('image', 'Unknown')
            else:
                prediction = result.get('prediction', 'Unknown')

            return jsonify({
                "status": "success",
                "prediction": prediction,
                "confidence": 1.0,  # Since confidence is not provided in the result
                "message": "Analysis completed successfully"
            }), 200

        except Exception as e:
            logger.error(f"Prediction error: {str(e)}")
            return jsonify({
                "status": "error",
                "message": "Error during prediction"
            }), 500

    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({
            "status": "error",
            "message": "An unexpected error occurred"
        }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

