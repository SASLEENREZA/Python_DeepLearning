from sklearn import datasets,metrics
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#load the iris datasets
data=datasets.load_iris()
#load the irisdatasets column values
x=data.data
y=data.target

#splitting the data for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25)

model=GaussianNB()
#fit the training data into model
model.fit(x_train,y_train)

#define to predict the test data
y_pred = model.predict(x_test)

print("Accuracy : ",metrics.accuracy_score(y_test, y_pred))

