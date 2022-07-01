import pickle
import os
import pandas as pd
import subprocess

subprocess.call(["pip", "install", "skforecast"])

from skforecast.model_selection import backtesting_forecaster
def make_forecasts():
    """Construya los pronosticos con el modelo entrenado final.

    Cree el archivo data_lake/business/forecasts/precios-diarios.csv. Este
    archivo contiene tres columnas:

    * La fecha.

    * El precio promedio real de la electricidad.

    * El pronóstico del precio promedio real.


    """
    #raise NotImplementedError("Implementar esta función")

    modelo = cargar_modelo()

    datos = pd.read_csv("data_lake/business/features/precios-diarios.csv")
    datos["Fecha"] = pd.to_datetime(datos["Fecha"], format="%Y-%m-%d")
    datos = datos.set_index("Fecha")
    datos = datos.asfreq("D")
    datos = datos.sort_index()

    datos_backtest = 365 * 20
    datos_train = datos[:-datos_backtest]
    datos_test = datos[-datos_backtest:]

    modelo.fit(y=datos_train["Precio"])

    metrica, predicciones = backtesting_forecaster(
        forecaster=modelo,
        y=datos.Precio,
        initial_train_size=len(datos_train),
        fixed_train_size=False,
        steps=1,
        metric="mean_absolute_error",
        refit=False,
        verbose=True,
    )

    predicciones.join(datos_test["Precio"]).to_csv(
        "data_lake/business/forecasts/precios-diarios.csv", index=True
    )


def cargar_modelo():
    
    with open("src/models/precios-diarios.pkl", "rb") as file:
        modelo = pickle.load(file)

    return modelo


if __name__ == "__main__":
    import doctest

    doctest.testmod()

