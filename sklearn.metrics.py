import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn import metrics 

y_true = [[3,4,1], [4,5,1]]
y_pred = [[3,4,1], [40,18,10]]
result0 = mean_absolute_error(y_true, y_pred)
result1 = mean_squared_error(y_true, y_pred)
print(result0)
print(result1)

def abmean(x:list, y:list):
    result = 0
    n = 0
    for i in range(0, len(x)):
        n = 0
        for j in range(0, len(x[1])):
            n += abs(x[i][j] - y[i][j])
        result += n/len(x[1])
    return (result / len(x))

def absqu(x:list, y:list):
    result = 0
    n = 0
    for i in range(0, len(x)):
        n = 0
        for j in range(0, len(x[1])):
            n += (x[i][j] - y[i][j]) ** 2
        result += n/len(x[1])
    return (result / len(x))



y1=[1,0,2,0,1,0,2,0,0,2,1,0,2,0,1,0,2,0,0,2,0,2,0,1,0,2,0,1,0,2,0,0,2,0,2,0,0,2]
y2=[1,0,1,0,0,0,2,0,2,1,1,0,0,0,2,0,2,1,0,2,1,1,0,0,0,2,0,2,1,0,0,2,0,2,1,0,0,2]
result_4=recall_score(y1,y2, average=None)
result_5=precision_score(y1,y2, average=None)
result_6=f1_score(y1,y2, average=None)
result_7=classification_report(y1,y2, target_names=["0", "1", "2"])
s = (metrics.roc_curve(y1,y2, pos_label=1))
print("SSSSS", s)

plt.plot(data=([0.  , 0.25, 0.5 , 1.  ], [0. , 0. , 0.5, 1. ]))
plt.show()

result_2 = abmean(y_true, y_pred)
result_3 = absqu(y_true, y_pred)
print(result_2)
print(result_3)
print(result_4)
print(result_5)
print(result_6)
print(result_7)