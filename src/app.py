from flask import Flask, render_template, request, jsonify
import os
import joblib

app = Flask(__name__)

# Path to the directory containing this scipt
current_script_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the directory containing models
models_directory = os.path.join(current_script_directory, 'models')

# Load all models features and scalers
models = {
    'temp': {
        'model': joblib.load(os.path.join(models_directory, 'temp_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'temp_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'temp_scaler.sav'))
    },
    'wind_speed': {
        'model': joblib.load(os.path.join(models_directory, 'speed_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'speed_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'speed_scaler.sav'))
    },
    # 'precip': {
    #     'model': joblib.load(os.path.join(models_directory, 'precip_model.sav')),
    #     'features': joblib.load(os.path.join(models_directory, 'precip_features.sav')),
    #     'scaler': joblib.load(os.path.join(models_directory, 'precip_scaler.sav'))
    # },
    'month': {
        'model': joblib.load(os.path.join(models_directory, 'month_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'month_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'month_scaler.sav'))
    },
    'hour': {
        'model': joblib.load(os.path.join(models_directory, 'hour_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'hour_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'hour_scaler.sav'))
    },
    'pressure': {
        'model': joblib.load(os.path.join(models_directory, 'pressure_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'pressure_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'pressure_scaler.sav'))
    },
    'humid': {
        'model': joblib.load(os.path.join(models_directory, 'humid_model.sav')),
        'features': joblib.load(os.path.join(models_directory, 'humid_features.sav')),
        'scaler': joblib.load(os.path.join(models_directory, 'humid_scaler.sav'))
    }
}





@app.route("/")
def home():
    return render_template("predict.html")


# Responses from server
INVALID_PREDICTION_TYPE = {'error': 'Invalid prediction type'}
ERROR_PROCESSING_REQUEST = {'error': 'Error processing your request'}

def prepare_and_predict(data, model_info):
    try:
        features = [float(data.get(name, 0)) for name in model_info['features']]
        scaled_features = model_info['scaler'].transform([features])
        prediction = model_info['model'].predict(scaled_features)
        return abs(round(prediction[0], 2))
    except Exception as e:
        app.logger.error(f"Error during prediction: {str(e)}")
        return None

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    prediction_type = data.get("predictionType", "")
    app.logger.info(f"Received prediction request for type: {prediction_type} with data: {data}")
    
    # Make sure we are trying to predict a valid target
    model_info = models.get(prediction_type)
    if not model_info:
        app.logger.warning(f"Invalid prediction type: {prediction_type}")
        return jsonify(INVALID_PREDICTION_TYPE), 200

    # Make Prediction
    prediction_result = prepare_and_predict(data, model_info)
    if prediction_result is None:
        return jsonify(ERROR_PROCESSING_REQUEST), 200
    
    # Return Prediction to website
    response = {'prediction': prediction_result}
    return jsonify(response), 200

    
    
if __name__ == '__main__':
    app.run(debug=True)