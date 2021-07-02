"""
Role:       	Server (complement to server.py)
Author:     	Songkomkrit Chaiyakan
Github link:	https://github.com/songkomkrit/GameAnalytics

"""

import math
from sklearn.cluster import KMeans
import warnings

def classify(X):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
        list_label = kmeans.labels_
        list_centroid = kmeans.cluster_centers_
    
    list_group = ['a']*len(list_label)
    distinct_label = list(set(list_label))
    num_group = len(distinct_label)
    list_coin = [v[2] for v in list_centroid[:num_group]]
    list_destroyed = [v[3] for v in list_centroid[:num_group]]

    
    for k in range(num_group):
        if math.floor(k/2) == 0:
            adj = 'Hardcore'
        else:
            adj = 'Casual'
        
        if k % 2 == 0:
            label = list_coin.index(max(list_coin))
            overall_group = 'Achiever'
        else:
            label = list_destroyed.index(max(list_destroyed))
            overall_group = 'Killer'
        
        for i, v in enumerate(list_label):
            if v == label:
                list_group[i] = adj + ' ' + overall_group
        
        list_coin[label] = -1000
        list_destroyed[label] = -1000
    
    return list_group