def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
   # raise NotImplementedError("Implementar esta función")

from email import header
import pandas as pd
final_path = 'data_lake/business/'

file = pd.read_csv('data_lake/cleansed/precios-horarios.csv', index_col=None, header=0)
file = file[['Fecha', 'Precio']]
file['Fecha'] = pd.to_datetime(file['Fecha'])
daily_ave_prices = file.groupby('Fecha', as_index=False).mean({'Precio': 'Precio'})

daily_ave_prices.to_csv( final_path + 'precios-diarios' + '.csv', index=None, header= True)

if __name__ == "__main__":
    import doctest

    compute_daily_prices()

    doctest.testmod()
