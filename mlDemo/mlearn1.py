#coding:utf-8
from sklearn.datasets.samples_generator import make_classification
from sklearn import preprocessing
X, y = make_classification(n_samples=6, n_features=5, n_informative=2, 
n_redundant=2, n_classes=2, n_clusters_per_class=2, scale=1.0, random_state=20)
for x, y in zip(X, y):
    print str(y) + ":", x
