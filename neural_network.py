import keras
import numpy as np
from keras import optimizers
from keras import losses
from keras import metrics
from keras import models
from keras import layers
from matplotlib import pyplot as plt

from sklearn.model_selection import train_test_split
from SVM_data import data_combo
from SVM_data import teams_stats
from SVM_data import subtract
from SVM_model1 import data_combo_2teams



# Uses sklearn neural_networks to predict NBA winners

def neural_network(games):

    train_data = []
    train_labels = []
    for date in range(2000, 2022):
        t = data_combo(date)
        train_data += t[0]
        train_labels += t[1]

    #games = data_combo_2teams(games)

    train_data, test_data, train_labels, test_labels = train_test_split(train_data, train_labels, test_size=0.3,random_state=109)


    #test_data, test_labels = data_combo(2021)


    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_dim=(len(train_data[0])))) #This is the first layer with 16 nodes and relu activation function, input shape is train_data length
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))#This is the Third layer with 1 nodes and  activation function sigmoid.

    model.compile(optimizer='adam',
                loss='binary_crossentropy',
                metrics=['accuracy'])

    '''
    model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                loss='binary_crossentropy',
                metrics=['accuracy'])
    '''



    e = 15
    b = 25
    #for e in [1, 5, 10, 50, 100]:
        #for b in [1, 5, 25, 50, 75, 100, 200, 500]:
    history = model.fit(train_data,
                        train_labels,
                        epochs=e,
                        batch_size=b)

    _, accuracy = model.evaluate(test_data, test_labels)
    print("Epoch is: {}\nBatch is: {}\nAccuracy is: {} \n\n\n".format(e, b, accuracy))
    #pred = model.predict(games)
    #return pred

# When we do random test data
# (15, 25) = 66.3%      16, 16, 1
# (7, 100) = 66.4%      16, 16, 1
# (5, 25)  = 66.5%      16, 16, 1
# stopped at 50

# When we make 2021 the test data
# (1, 75) = 60.3%       16, 16, 1
# (1, 500) = 60.6%      32, 16, 1


if __name__ == '__main__':
    '''
    
    games = []
    print("Please enter the games in: HOME AWAY")
    while True:
        i = input("\n")
        if i == 'done':
            break
        line = i.split(' ')
        game = (line[0], line[1])
        games.append(game)
    pred = neural_network(games)
    for index, game in enumerate(games):
        if pred[index] == 1:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(home, away))
        else:
            home = game[0]
            away = game[1]
            print("{} wins over {}".format(away, home))
    '''
    neural_network(None)