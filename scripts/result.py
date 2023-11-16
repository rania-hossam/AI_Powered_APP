from scripts.manipulation import image_manipulation
import numpy as np
import joblib

def deploy_cluster(model_path, image):
    # Test the function, look at input/output
    notation = []
    notation.append(image_manipulation(image))
    notation = np.asarray(notation)

    # flatten the images ndarray to one row per image
    features_flat = notation.reshape((notation.shape[0], -1))

    loaded_model = joblib.load(model_path)
    predictions = loaded_model.predict(features_flat)

    return predictions
