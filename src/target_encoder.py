import joblib
from category_encoders import TargetEncoder

def load_target_encoder():
    return joblib.load('target_encoder.pkl')
