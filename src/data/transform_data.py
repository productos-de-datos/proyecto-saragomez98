def transform_data():
    """Transforme los archivos xls a csv.
    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.
    """
    import pandas as pd
    for file in range(1995, 2022):
        if file in range(1995, 2000):
            read_file = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(file), header=3)
            read_file.to_csv(
                'data_lake/raw/{}.csv'.format(file), index=None)
        elif file in range(2000, 2018):
            if file in [2016, 2017]:
                read_file = pd.read_excel(
                    'data_lake/landing/{}.xls'.format(file), header=2)
                read_file.to_csv(
                    'data_lake/raw/{}.csv'.format(file), index=None)
            else:
                read_file = pd.read_excel(
                    'data_lake/landing/{}.xlsx'.format(file), header=2)
                read_file.to_csv(
                    'data_lake/raw/{}.csv'.format(file), index=None)
        else:
            read_file = pd.read_excel(
                'data_lake/landing/{}.xlsx'.format(file), header=0)
            read_file.to_csv(
                'data_lake/raw/{}.csv'.format(file), index=None)
#raise NotImplementedError("Implementar esta función")
def test_date_validation():
    """
    Testing that the date is in the column that should be
    """
    import pandas as pd
    for file in range(1995, 2022):
        read_file = pd.read_csv(
                'data_lake/raw/{}.csv'.format(file))
        assert ["Fecha"] == [read_file.columns.values[0]]

if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
    
