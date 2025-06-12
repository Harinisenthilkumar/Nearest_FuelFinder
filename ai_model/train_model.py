import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

# Synthetic dataset
# Columns: [distance (km), rating (1-5)]
# Target: score (0 to 1)
X = np.array([
    [1.0, 4.5],
    [2.5, 3.0],
    [0.5, 5.0],
    [4.0, 2.0],
    [1.8, 4.0],
    [3.0, 3.5],
    [0.8, 4.8],
    [5.0, 1.5],
    [2.0, 4.2],
    [1.5, 3.8]
])
y = np.array([0.9, 0.6, 0.95, 0.4, 0.8, 0.65, 0.92, 0.3, 0.85, 0.75])

# Scale the features (distance and rating)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the Linear Regression model
model = LinearRegression()
model.fit(X_scaled, y)

# Save the scaler and model
with open('ai_model/petrol_bunk_ranker.pkl', 'wb') as f:
    pickle.dump({'scaler': scaler, 'model': model}, f)

print("Model trained and saved to ai_model/petrol_bunk_ranker.pkl")