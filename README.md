# 🏙️ Smart Urban Rental Analyzer

An end-to-end data analytics and machine learning pipeline that predicts real estate rental prices based on property size, furnishing, and location.

## 🚀 Tech Stack
* **Database:** SQLite (Data Storage & Schema Design)
* **Python:** Pandas, NumPy (Data Preprocessing & Feature Engineering)
* **Machine Learning:** Scikit-Learn, Random Forest Regressor
* **Visualization:** PowerBI (Interactive Dashboards)

## 📁 Project Structure
* `/data` - Contains the SQLite database and exported CSVs for PowerBI.
* `/scripts` - Python scripts for database initialization and the CLI prediction tool.
* `/notebooks` - Jupyter Notebooks detailing Exploratory Data Analysis (EDA) and model training.
* `/models` - Serialized Random Forest model (`.pkl`).

## 🛠️ How to Run
1. **Initialize Database:** Run `python scripts/setup_db.py` to generate the mock real estate data.
2. **Train Model:** Open `notebooks/01_EDA_and_Exploration.ipynb` to explore the market and train the ML model.
3. **Predict Rent:** Run `python scripts/predict_rent.py` to use the command-line interface for instant rent predictions.