def train_daily_model():
    """Entrena el modelo de pronóstico de precios diarios.

    Con las features entrene el modelo de proóstico de precios diarios y
    salvelo en models/precios-diarios.pkl


    """
   # raise NotImplementedError("Implementar esta función")
import subprocess
    import numpy as np
    import pandas as pd
    import datetime
    import os
    import pickle

    subprocess.call(["pip", "install", "holidays"])
    subprocess.call(["pip", "install", "sklearn"])
    subprocess.call(["pip", "install", "skforecast"])

    import holidays
    from sklearn.linear_model import Ridge
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    from skforecast.ForecasterAutoreg import ForecasterAutoreg
    from skforecast.model_selection import grid_search_forecaster
    from skforecast.model_selection import backtesting_forecaster

   
    datos = pd.read_csv("data_lake/business/features/precios-diarios.csv")
    datos["Fecha"] = pd.to_datetime(datos["Fecha"], format="%Y-%m-%d")
    datos["Día Semana"] = datos["Fecha"].dt.strftime("%A")

    fecha = datetime.datetime.now()

    total_anios = fecha.year - 1995

    
    anios = list(range(1995, 1995 + total_anios, 1))

    co_holidays = holidays.Colombia(years=anios)
    datos["Festivo"] = datos["Fecha"].isin(co_holidays)

    datos = datos.set_index("Fecha")
    datos = datos.asfreq("D")
    datos = datos.sort_index()

    datos_backtest = 365 * 20
    datos_train = datos[:-datos_backtest]
    datos_test = datos[-datos_backtest:]

    forecaster = ForecasterAutoreg(
        regressor=make_pipeline(StandardScaler(), Ridge()), lags=1
    )

    forecaster.fit(y=datos_train["Precio"])

    metrica, predicciones = backtesting_forecaster(
        forecaster=forecaster,
        y=datos.Precio,
        initial_train_size=len(datos_train),
        fixed_train_size=False,
        steps=1,
        metric="mean_absolute_error",
        refit=False,
        verbose=True,
    )

    forecaster = ForecasterAutoreg(
        regressor=make_pipeline(StandardScaler(), Ridge()), lags=1
    )

    # Lags utilizados como predictores
    lags_grid = [5, 24, [1, 2, 3, 23, 24, 25, 47, 48, 49]]

    # Hiperparámetros del regresor
    param_grid = {"ridge__alpha": np.logspace(-3, 5, 10)}

    resultados_grid = grid_search_forecaster(
        forecaster=forecaster,
        y=datos_test["Precio"],
        param_grid=param_grid,
        lags_grid=lags_grid,
        steps=1,
        metric="mean_absolute_error",
        refit=False,
        initial_train_size=datos_train.size,
        fixed_train_size=False,
        return_best=True,
        verbose=False,
    )

    
    with open("src/models/precios-diarios.pkl", "wb") as f:
        pickle.dump(forecaster, f)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

