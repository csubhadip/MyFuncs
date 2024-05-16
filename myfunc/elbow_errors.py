# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 16:22:29 2023

@author: ADMIN
"""
# Classfication Elbow
def Elbow_Class(x_train, x_test, y_train, y_test, K):
    import numpy as np
    from sklearn.neighbors import KNeighborsClassifier as KNN
    from sklearn.metrics import f1_score, accuracy_score
    from matplotlib import pyplot as plt
    #initiating empty list
    test_error = []
   
    #training model for evey value of K
    for i in K:
        #Instance of KNN
        clf = KNN(n_neighbors = i)
        clf.fit(x_train, y_train)
        # Appending F1 scores to empty list claculated using the predictions
        tmp = clf.predict(x_test)
        tmp = f1_score(y_true=y_test, y_pred=tmp, average='weighted')
        error = 1 - tmp
        #print((i, error, tmp))
        test_error.append(error)
    plt.plot(K, test_error)
    plt.xlabel('K Neighbors')
    plt.ylabel('Test error (1-F1)')
    plt.title('Elbow Curve for test')
    plt.show()
    print("Min F1 Error Index = ", [(j, i) for j,i in enumerate(test_error) if i == np.min(test_error)])
    print("Min F1 Error = ", np.min(test_error))
#%% Regression Elbow   
def Elbow_Reg(x_train, x_test, y_train, y_test, K):
    import numpy as np
    from sklearn.neighbors import KNeighborsRegressor as KNN
    from sklearn.metrics import r2_score
    from matplotlib import pyplot as plt
    #initiating empty list
    test_error = []
   
    #training model for evey value of K
    for i in K:
        #Instance of KNN
        clf = KNN(n_neighbors = i, weights='distance')
        clf.fit(x_train, y_train)
        # Appending F1 scores to empty list claculated using the predictions
        tmp = clf.predict(x_test)
        tmp = r2_score(y_true=y_test, y_pred=tmp, multioutput='variance_weighted')
        error = 1 - tmp
        test_error.append(error)
    plt.plot(K, test_error)
    plt.xlabel('K Neighbors')
    plt.ylabel('Test error (1-R2)')
    plt.title('Elbow Curve for test')
    plt.show()
    print("Min R2 Error Index = ", [(j, i) for j,i in enumerate(test_error) if i == np.min(test_error)])
    print("Min R2 Error = ", np.min(test_error))



