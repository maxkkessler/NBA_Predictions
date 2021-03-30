from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import metrics
from SVM_data import data_combo


data, target = data_combo(2015)

X_train, X_test, y_train, y_test = train_test_split(data, target, test_size = 0.3, random_state = 109)


for n in [0.05, 0.1, 1, 10, 100]

    clf = SVC(kernel='linear', C = n)

    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)


    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))


