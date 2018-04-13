from importlib import reload

import pre_test

from numpy import vstack, hstack, ravel, shape

from sklearn.svm import SVC

from sklearn.externals import joblib

reload(pre_test)

d9, l9 = pre_test.load_dev_data(1, 9)

d10, l10 = pre_test.load_dev_data(1, 10)

m9 = shape(d9)[0]
m10 = shape(d10)[0]

dataMat = vstack((d9, d10))
labelMat = hstack((l9, d9))

dataMat = vstack((d9[0:int(m9*0.01)], d10[0:int(m10*0.01)]))
labelMat = hstack((l9[:, 0:int(m9*0.01)], d9[:, 0:int(m10*0.01)]))

clf = SVC()

clf.fit(dataMat, ravel(labelMat))

SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)


print(clf.predict([[1]]))

