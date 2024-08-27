import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, root_mean_squared_error

def evaluate_cv(model, X, y, cv):

    r2 = []
    rmse = []

    for (train_index, test_index) in cv.split(X):

        train_index = pd.Index(train_index)
        test_index = pd.Index(test_index)

        X_train = X.loc[X.index.isin(train_index)]
        X_test = X.loc[X.index.isin(test_index)]

        y_train = y.loc[y.index.isin(train_index)]
        y_test = y.loc[y.index.isin(test_index)]

        pred_train = model.predict(X_train)
        pred_test = model.predict(X_test)

        r2.append(r2_score(y_test, pred_test).round(4))
        rmse.append(root_mean_squared_error(y_test, pred_test).round(4))

    return(pd.DataFrame({'R2 Score': r2, 'Root Mean Squared Error': rmse}))