import pandas as pd
import numpy as np
from sklearn import neighbors
from sklearn import datasets

knn = neighbors.KNeighborsClassifier()
iris = datasets.load_iris()

print(iris)

knn.fit(iris.data, iris.target)

new = knn.predict(testset)



