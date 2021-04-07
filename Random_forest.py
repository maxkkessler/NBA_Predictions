from sklearn.ensemble import RandomForestClassifier
from SVM_data import data_combo
from sklearn.model_selection import train_test_split
from sklearn import metrics

def random_forest():
    X_train = []
    y_train = []
    for date in range(2015, 2021):
        t = data_combo(date)
        X_train += t[0]
        y_train += t[1]

    X_test, y_test = data_combo(2021)
    
    clf = RandomForestClassifier(n_estimators=50)
    clf = clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)
    acc = metrics.accuracy_score(y_test, y_pred)
    
    return acc


if __name__ == '__main__':
    total = 0
    for i in range(10):
        total += random_forest()
    print(total/10)
    