import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import normalize, StandardScaler, OrdinalEncoder, OneHotEncoder, KBinsDiscretizer


data = pd.read_csv("Stars.csv")
data["Color"] = data["Color"].astype("category").cat.codes
data["Spectral_Class"] = data["Spectral_Class"].astype("category").cat.codes

features = data.iloc[:, :-1]
y = data.iloc[:, -1]

"""
Q2: Uncomment these lines for applying discretizing and scaling
"""
# discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal', strategy='quantile')
# discretized_features = discretizer.fit_transform(features)
# scaler = StandardScaler()
# scaled_features = scaler.fit_transform(discretized_features)

"""
Q2: Comment this line for applying discretizing and scaling
"""
scaled_features = features

"""
* ‘ward’ minimizes the variance of the clusters being merged.
* If linkage is “ward”, only “euclidean” is accepted.
"""
agg_cluster = AgglomerativeClustering(n_clusters=6, affinity='euclidean', linkage='ward') 
 
"""
* ‘random’: choose n_clusters observations (rows) at random from data for the initial centroids.
* ‘n_init’: Number of time the k-means algorithm will be run with different centroid seeds.
* The final results will be the best output of n_init consecutive runs in terms of inertia.
* ‘max_iter’: Maximum number of iterations of the k-means algorithm for a single run.
* ‘random_state’ :Determines random number generation for centroid initialization
"""
kmean_cluster = KMeans(init="random", n_clusters=6, n_init=10, max_iter=100, random_state=261)

agg_pred = agg_cluster.fit_predict(scaled_features)
kmean_pred = kmean_cluster.fit_predict(scaled_features)

# Accuracy
agg_sum = 0
kmean_sum = 0
for i in range(len(y)):
    agg_sum += (agg_pred[i] == y[i])
    kmean_sum += (kmean_pred[i] == y[i])
    
print(f'Kmean:{kmean_sum/len(kmean_pred)} \nAgg: {agg_sum/len(agg_pred)}')
