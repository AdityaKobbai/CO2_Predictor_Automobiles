import pandas as pd
from predictor import predict_with_scaled_input
from utils.ratings import determine_rating

# Example new data input
new_input_data = pd.DataFrame({
    'Model year': [2021],
    'Make': ['Audi'],
    'Model': ['S4'],
    'Vehicle class': ['Full-size'],
    'Engine size (L)': [2],
    'Cylinders': [6],
    'Transmission': ['AV'],
    'Fuel type': ['X'],
    'Combined (mpg)': [32]
})

if __name__ == "__main__":
    predictions = predict_with_scaled_input(new_input_data)
    ratings = determine_rating(predictions)
    
    if ratings:
        print(f"Possible ratings: {ratings}")
    else:
        print("No matching rating found.")
