from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
import pandas as pd

data = pd.read_csv(r"./comp.csv")
feature = []
label = []
rowDict = {}

for row in range(0,len(data)):
    label.append(data.iloc[row][-1])
    for i in range(0, len(data.iloc[0]) -1):
        rowDict[data.columns[i]] = data.iloc[row][i]
    feature.append(rowDict)
    rowDict = {}

vec = DictVectorizer() # 变量转换对象
lb = preprocessing.LabelBinarizer()

dummyX = vec.fit_transform(feature).toarray() # 变量转换
dummyY = lb.fit_transform(label)

# 建模
clf = tree.DecisionTreeClassifier(criterion="entropy") # 决策树分类模型对象
mod = clf.fit(dummyX, dummyY)

# 导出文件
with open(r"./tree.dot", "w") as f:
    f = tree.export_graphviz(mod, feature_names=vec.get_feature_names(), out_file=f)

# 绘制决策树
# dot -Tpdf tree.dot -o tree.pdf

# 预测
new = dummyX[0:1,:]
new[0][0] = 1
preNew = mod.predict(new)
print(preNew)