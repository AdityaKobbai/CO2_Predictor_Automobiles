import joblib
from target_encoder import load_target_encoder
from scaler import load_scaler

def load_model():
    return joblib.load('best_model.pkl')

def predict_with_scaled_input(new_input_data):
    target_encoder = load_target_encoder()
    scaler = load_scaler()
    best_model = load_model()
    
    new_input_data_encoded = target_encoder.transform(new_input_data)
    new_input_data_scaled = scaler.transform(new_input_data_encoded)
    
    predictions = best_model.predict(new_input_data_scaled)
    
    return predictions
