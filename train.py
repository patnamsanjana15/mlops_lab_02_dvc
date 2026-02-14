import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Load data
df = pd.read_csv("data/CC_GENERAL.csv")

# Select a few numeric features
features = df[["BALANCE", "PURCHASES", "CREDIT_LIMIT"]].dropna()

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(features)

# KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

features["cluster"] = clusters

print("Cluster counts:")
print(features["cluster"].value_counts())

print("\nSample clustered data:")
print(features.head())