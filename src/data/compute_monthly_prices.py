def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
   # raise NotImplementedError("Implementar esta función")

import pandas as pd
    import os

    path_origin = 'data_lake/cleansed/precios-horarios.csv'
    final_path = 'data_lake/business/'
    
    day_prices = pd.read_csv('data_lake/cleansed/precios-horarios.csv', index_col=None, header=0)
    day_prices = day_prices[['Fecha', 'Precio']]
    day_prices['Fecha'] = pd.to_datetime(day_prices['Fecha'])
    day_prices['Firstday']= day_prices['Fecha'].to_numpy().astype('datetime64[M]')
    day_prices = day_prices[['Firstday', 'Precio']]
    monthly_ave_prices = day_prices.groupby('Firstday', as_index=False).mean({'Precio': 'Precio'})
    monthly_ave_prices.to_csv( final_path + 'precios-mensuales' + '.csv', index=None, header= True)
    

if __name__ == "__main__":

    compute_monthly_prices()
    import doctest

    doctest.testmod()
