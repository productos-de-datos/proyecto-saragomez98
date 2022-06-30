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

    
    data = pd.read_csv("data_lake/cleansed/precios-horarios.csv")
    data["Fecha"] = pd.to_datetime(data["Fecha"])

    
    data = data.set_index("Fecha").resample("M")["Precio"].mean()

    
    data.to_csv("data_lake/business/precios-mensuales.csv", index=True)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
