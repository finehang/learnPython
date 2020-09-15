from sklearn import svm

x=[[2,0],[1,1], [2,3]]
y=[0,0,1]

clf = svm.SVC(kernel="linear")
clf.fit(x, y)

print(clf)
print(clf.support_vectors_) # 找出支持向量
print(clf.support_) # 找出支持向量的索引
print(clf.n_support_) # 找出每个类里支持向量的个数
print(clf.predict([[0,0], [5,5]]))
