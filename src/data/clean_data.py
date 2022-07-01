def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.

    Usando los archivos data_lake/raw/*.csv, cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.


    """
    #raise NotImplementedError("Implementar esta función")
    
    import os 
    import pandas as pd
    
    

    def read_files(path_origin):
        correct_prices = pd.DataFrame()
        files_csv = csv_file(path_origin)
        for filename in files_csv:
            if filename.split('.')[-1] == 'csv':
                data = pd.read_csv(path_origin + filename, index_col=None, header=0)
                correct_prices = pd.concat(objs=[correct_prices, data], axis=0, ignore_index=False)
        return correct_prices

    def csv_file(path_origin):
        files_csv = os.listdir(path_origin)
        return files_csv

    def created_format(correct_prices):
        correct_prices['Fecha'] = correct_prices['Fecha'].apply(lambda x: str(x))
        correct_prices['Fecha'] = correct_prices['Fecha'].apply(lambda x: x[:10])
        correct_prices = correct_prices[correct_prices['Fecha'].notnull()]
        return correct_prices

    def create_df():
        df_correct_prices = pd.DataFrame()
        df_correct_prices['Fecha'] = None
        df_correct_prices['Hora'] = None
        df_correct_prices['Precio'] = None

        df_correct_prices_backup = pd.DataFrame()
        df_correct_prices_backup['Fecha'] = None
        df_correct_prices_backup['Hora'] = None
        df_correct_prices_backup['Precio'] = None
        return df_correct_prices, df_correct_prices_backup

    def make_correct_prices(correct_prices, df_correct_prices, df_correct_prices_backup):
        for hora in range(0,24):
            hora_str = str(hora)

            df_correct_prices_backup['Fecha'] = correct_prices['Fecha']
            df_correct_prices_backup['Hora'] = hora_str
            df_correct_prices_backup['Precio'] = correct_prices[hora_str]

            df_correct_prices = pd.concat(objs=[df_correct_prices, df_correct_prices_backup], axis=0, ignore_index=False)
        return df_correct_prices

    def save_correct_prices(df_correct_prices, path_final):
        df_correct_prices.to_csv(path_final + 'precios-horarios.csv', index=None)

    path_origin = './data_lake/raw/'
    path_final = './data_lake/cleansed/'
    correct_prices = read_files(path_origin)
    correct_prices = created_format(correct_prices)
    df_correct_prices, df_correct_prices_backup = create_df()
    df_correct_prices = make_correct_prices(correct_prices, df_correct_prices, df_correct_prices_backup)
    save_correct_prices(df_correct_prices, path_final)
    
    

if __name__ == "__main__":

    clean_data()
    import doctest

    doctest.testmod()
