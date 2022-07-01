def create_data_lake():
    """Cree el data lake con sus capas.

    Esta función debe crear la carpeta `data_lake` en la raiz del proyecto. El data lake contiene
    las siguientes subcarpetas:

    ```
    .
    |
    \___ data_lake/
         |___ landing/
         |___ raw/
         |___ cleansed/
         \___ business/
              |___ reports/
              |    |___ figures/
              |___ features/
              |___ forecasts/

    ```


    """
   # raise NotImplementedError("Implementar esta función")
import os
import sys

os.mkdir('data_lake')

root_path ='data_lake/'
list =['landing', 'raw', 'cleansed', 'business']

for items in list:
    path = os.path.join(root_path, items)
    os.mkdir(path)

root_path_business = 'data_lake/business'
list_business= ['reports', 'features', 'forecasts']

for items in list_business:
    path = os.path.join(root_path_business, items)
    os.mkdir(path)

directory = 'figures'
root_path_reports = 'data_lake/business/reports'
path = os.path.join(root_path_reports, directory)
os.mkdir(path)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
