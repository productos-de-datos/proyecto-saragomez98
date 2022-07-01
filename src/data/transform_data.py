def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
   # raise NotImplementedError("Implementar esta función")
import pandas as pd
import xlwt
import os

landing_path = 'data_lake/landing/'
raw_path = 'data_lake/raw/'
files_landing_folder = os.listdir(landing_path)
files_raw_folder = os.listdir(raw_path)

for files in files_landing_folder:
    if files.split('.')[-1] == 'xlsx' or files.split('.')[-1] == 'xls':
        year_transformed = int(files.split('.')[0])
        if year_transformed in range(1995,2000):
            num_header = 3
        if year_transformed in range (2000, 2018):
            num_header = 2
        if year_transformed in range (2018, 2022):
            num_header = 0
    
        file = pd.read_excel(landing_path + files)
        file = file.iloc[num_header:, 0:25]
        file.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
        file.to_csv(raw_path + str(year_transformed) + '.csv', index=None)
        

if __name__ == "__main__":
    import doctest

    transform_data()

    doctest.testmod()
