import sqlite3
import pandas as pd
import random

# 1. Connect to SQLite (creates the file 'rental_analyzer.db' in your folder)
conn = sqlite3.connect('data/rental_analyzer.db')
cursor = conn.cursor()

# 2. Define the SQL Schema
cursor.execute('''
CREATE TABLE IF NOT EXISTS properties (
    property_id INTEGER PRIMARY KEY AUTOINCREMENT,
    neighborhood TEXT,
    bhk_size INTEGER,
    sqft INTEGER,
    furnishing TEXT,
    rent_monthly INTEGER,
    maintenance_monthly INTEGER,
    distance_to_transit_km REAL
)
''')

# Clear existing data if you run the script multiple times
cursor.execute('DELETE FROM properties')

# 3. Generate Mock Data 
neighborhoods = ['Wakad', 'Hinjewadi', 'Kharadi', 'Baner', 'Viman Nagar']
furnishing_options = ['Unfurnished', 'Semi-Furnished', 'Fully Furnished']

mock_data = []
for _ in range(500):  # Generate 500 mock property listings
    nbh = random.choice(neighborhoods)
    bhk = random.choice([1, 2, 3])
    
    # Calculate somewhat realistic square footage based on BHK
    sqft = bhk * random.randint(400, 600) + random.randint(0, 200)
    furnishing = random.choice(furnishing_options)
    
    # Create somewhat realistic pricing logic for the ML model to "discover" later
    base_rent = bhk * 12000
    premium = 6000 if furnishing == 'Fully Furnished' else (2500 if furnishing == 'Semi-Furnished' else 0)
    rent = base_rent + premium + random.randint(-2000, 4000)
    
    maintenance = random.randint(1500, 5000)
    transit = round(random.uniform(0.2, 5.0), 1)
    
    mock_data.append((nbh, bhk, sqft, furnishing, rent, maintenance, transit))

# 4. Insert into the SQL Database
cursor.executemany('''
INSERT INTO properties 
(neighborhood, bhk_size, sqft, furnishing, rent_monthly, maintenance_monthly, distance_to_transit_km)
VALUES (?, ?, ?, ?, ?, ?, ?)
''', mock_data)

conn.commit()

# 5. Verify the data using Pandas (our bridge to the next step)
df = pd.read_sql_query("SELECT * FROM properties LIMIT 5", conn)
print("Database created successfully! Here are the first 5 rows:")
print("-" * 60)
print(df.to_string(index=False))

conn.close()