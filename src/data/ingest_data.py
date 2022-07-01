"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""

def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
#    raise NotImplementedError("Implementar esta función")

import os
import pandas as pd
import xlwt

start = 1995
end = 2022
repo_path = 'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls'
final_path = 'data_lake/landing/'

for year_to_download in range (start, end):
    try: 
        files = pd.read_excel(repo_path + '/' + str(year_to_download) + '.xlsx?raw=true')
        files.to_excel(final_path + str(year_to_download) + '.xlsx', index=None, header=True)
    except:
        files = pd.read_excel(repo_path + '/' + str(year_to_download) + '.xls?raw=true')
        files.to_excel(final_path + str(year_to_download) + '.xls', index=None, header=True)

if __name__ == "__main__":

    ingest_data()
    import doctest

    doctest.testmod()
