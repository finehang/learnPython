import pandas as pd
import numpy as np
import random
from sklearn import neighbors

def load(filePath:str, split:float):
    trainset = []
    testset=[]
    data = pd.read_csv(filePath)
    print(data)
    for i in range(0, len(data)):
        if random.random() < split:
            trainset.append(data.iloc[i])
        else:
            testset.append(data.iloc[i])
    return [pd.DataFrame(trainset), pd.DataFrame(testset)]


def getN(testset, trainset, k=3):
    for i in range(0, len(testset)):
        for j in range(0, len(trainset)):
            testset.iloc[]


path = r"C:\Users\fanhang\Desktop\learn_python\NP\machineLearning\k_nearest_neighbor\iris.csv"
trainset, testset = load(path, split = .7)


knn = neighbors.KNeighborsClassifier()


len(trainset)
len(testset)

