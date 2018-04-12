from importlib import reload
import preTest
from numpy import vstack, ravel

from sklearn.svm import SVC

reload(preTest)

d9, l9 = preTest.load_dev_data(1, 9)

d10, l10 = preTest.load_dev_data(1, 10)

dataMat = vstack((d9, d10))
labelMat = vstack((l9, d9))

clf = SVC()


SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
  decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
  max_iter=-1, probability=False, random_state=None, shrinking=True,
  tol=0.001, verbose=False)

print(clf.predict([[1]]))