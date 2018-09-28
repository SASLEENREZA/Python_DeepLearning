from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets

data=datasets.load_iris()
#load x and y data
x=data.data
y=data.target
#split training and test data for both x and y for linear kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.3)

train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.3)

#define the model for linear kernel
lmodel=SVC(kernel='kernel')
#fit training data into linear kernel
lmodel.fit(train_x, train_y)
#predict the test data using linear kernel
prediction=lmodel.predict(test_x)
#calc accuracy score for linear kernel
print("linear kernel Accuracy ", accuracy_score(prediction, test_y))

rmodel = SVC(kernel='rbf')
rmodel.fit(train_x1, train_y1)
pred=rmodel.predict(test_x1)
print("RBF kernel accuracy ", accuracy_score(pred, test_y1))
