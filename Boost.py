from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import metrics
from SVM_data import data_combo
from SVM_data import teams_stats
from SVM_data import subtract
from SVM_model1 import data_combo_2teams
from sklearn.ensemble import AdaBoostClassifier


#Try xgboost

#Uses the sklearn boosting algorithm to predict winners

def boost_function(games):
    X_train = []
    y_train = []
    for date in range(2010, 2022):
        t = data_combo(date)
        X_train += t[0]
        y_train += t[1]

    #games = data_combo_2teams(games)

    #X_test, y_test = data_combo(2021)

    X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3,random_state=109)

    ada_clf = AdaBoostClassifier(n_estimators=100, algorithm="SAMME.R", learning_rate=.5)
    ada_clf.fit(X_train, y_train)
    y_pred = ada_clf.predict(X_test)

    print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    #pred = ada_clf.predict(games)
    #return pred


if __name__ == '__main__':

    games = []
    print("Please enter the games in: HOME AWAY")
    while True:
        i = input("\n")
        if i == 'done':
            break
        line = i.split(' ')
        game = (line[0], line[1])
        games.append(game)

    pred = boost_function(games)
    for index, game in enumerate(games):
        if pred[index] == 1:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(home, away))
        else:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(away, home))