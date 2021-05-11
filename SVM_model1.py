from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import metrics
from SVM_data import data_combo
from SVM_data import teams_stats
from SVM_data import subtract




def data_combo_2teams(games):
    #Takes a list of matchups and returns a list of their combined data. Just subtract away array from home array
    data = []
    for game in games:
        date = 2021     #current date
        d = teams_stats(date)
        arr = subtract(d[game[0]], d[game[1]])
        data.append(arr)
    return data




def svm_function(games):
    #First model. Uses SVM to predict NBA winners

    X_train = []
    y_train = []
    for date in range(2018, 2022):
        t = data_combo(date)
        X_train += t[0]
        y_train += t[1]

    games = data_combo_2teams(games)

    #X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size=0.3,random_state=109)

    #X_test, y_test = data_combo(2021)

    clf = SVC(kernel='linear', C = 1)

    clf.fit(X_train, y_train)

    
    #y_pred = clf.predict(X_test)

    #print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

    pred = clf.predict(games)
    return pred


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

    pred = svm_function(games)
    for index, game in enumerate(games):
        if pred[index] == 1:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(home, away))
        else:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(away, home))