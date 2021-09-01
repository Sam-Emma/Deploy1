def makePrediction(spl,spw,pll,plw):
    from sklearn.preprocessing import StandardScaler
    from sklearn.ensemble import RandomForestClassifier
    import pandas as pd
    import numpy as np
    df = pd.read_csv('Iris.csv')
    
    X  = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df["Species"]
    #print(X)
    #print(y)
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    #X_test = sc.transform(X_test)
    classifier = RandomForestClassifier()
    classifier.fit(X_train,y_train)
    test  = np.array([[spl,spw,pll,plw]])
    test = test
    return classifier.predict(test)
# -*- coding: utf-8 -*-

