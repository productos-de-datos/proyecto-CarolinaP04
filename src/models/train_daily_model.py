def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd 
    import numpy as np
    from sklearn.neural_network import MLPRegressor
    import pickle

    df_train = pd.read_csv('data_lake/business/features/precios-diarios.csv')
    df_model = df_train.dropna()
    X = df_model.iloc[:, -1]
    X = np.array(X).reshape(-1, 1)
    y = df_model.iloc[:, 2]


    H = 1
    mlp = MLPRegressor(
        hidden_layer_sizes=(H,),
        activation="logistic",
        learning_rate="adaptive",
        momentum=0.0,
        learning_rate_init=0.1,
        max_iter=100000,
        )


    mlp.fit(X, y)  

    pickle.dump(mlp, open('src/models/precios-diarios.pkl', 'wb'))

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    train_daily_model()

