import pandas as pd
import joblib

# 1. Load the trained model
# Ensure the script looks in the models/ directory
model = joblib.load('../models/rental_rf_model.pkl')

# Scikit-learn remembers the exact columns used during training
expected_cols = model.feature_names_in_

def run_predictor():
    print("\n" + "="*40)
    print(" 🏙️ SMART URBAN RENTAL PREDICTOR")
    print("="*40)
    
    # 2. Gather user input
    print("\nAvailable Neighborhoods: Wakad, Hinjewadi, Kharadi, Baner, Viman Nagar")
    nbh = input("Enter Neighborhood: ").strip()
    
    bhk = int(input("Enter BHK size (1, 2, 3): "))
    sqft = int(input("Enter Square Footage (e.g., 800): "))
    
    print("\nOptions: Unfurnished, Semi-Furnished, Fully Furnished")
    furnishing = input("Enter Furnishing Status: ").strip()
    
    maintenance = int(input("Enter Monthly Maintenance (₹): "))
    transit = float(input("Distance to transit (km): "))

    # 3. Preprocess the input to match the training data format
    furnishing_map = {'Unfurnished': 0, 'Semi-Furnished': 1, 'Fully Furnished': 2}
    furnishing_code = furnishing_map.get(furnishing, 0) # Defaults to 0 if spelled wrong
    
    # Create a dictionary with all expected features set to 0 initially
    input_data = {col: 0 for col in expected_cols}
    
    # Map the numerical inputs
    input_data['bhk_size'] = bhk
    input_data['sqft'] = sqft
    input_data['maintenance_monthly'] = maintenance
    input_data['distance_to_transit_km'] = transit
    input_data['furnishing_code'] = furnishing_code
    
    # Map the neighborhood (One-Hot Encoding logic for a single row)
    nbh_col = f'neighborhood_{nbh}'
    if nbh_col in input_data:
        input_data[nbh_col] = 1 
        # Note: If the user types the 'dropped' base neighborhood (like Baner), 
        # it won't be in expected_cols, so all neighborhood columns correctly remain 0.

    # Convert the dictionary into a 1-row Pandas DataFrame
    df_input = pd.DataFrame([input_data])
    
    # 4. Generate the Prediction
    predicted_price = model.predict(df_input)[0]
    
    print("\n" + "="*40)
    print(f"📊 Predicted Fair Market Rent: ₹{predicted_price:,.0f} / month")
    print("="*40 + "\n")

if __name__ == "__main__":
    run_predictor()