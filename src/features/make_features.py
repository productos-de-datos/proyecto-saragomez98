def make_features():
    """Prepara datos para pronóstico.

    Cree el archivo data_lake/business/features/precios-diarios.csv. Este
    archivo contiene la información para pronosticar los precios diarios de la
    electricidad con base en los precios de los días pasados. Las columnas
    correspoden a las variables explicativas del modelo, y debe incluir,
    adicionalmente, la fecha del precio que se desea pronosticar y el precio
    que se desea pronosticar (variable dependiente).

    En la carpeta notebooks/ cree los notebooks de jupyter necesarios para
    analizar y determinar las variables explicativas del modelo.

    """
   # raise NotImplementedError("Implementar esta función")
import pandas as pd
    import os
    import shutil

    # print(os.getcwd())
    os.chdir("./")

    # Se copia el archivo de business a la carpeta features
    shutil.copy(
        "data_lake/business/precios-diarios.csv",
        "data_lake/business/features/precios-diarios.csv",
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()

