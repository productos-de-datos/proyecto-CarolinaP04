def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    for year in range(1995, 2022):
        
        if  year in range (1995,2016):
            
            read_file = pd.read_excel('data_lake/landing/{}.xlsx'.format(year), header = 3)
            df = read_file.iloc[:, :25] 
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
        
        elif year in range (2018,2022):
            read_file = pd.read_excel('data_lake/landing/{}.xlsx'.format(year), header = 2)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
        
        elif year == 2016  or year == 2017:
            read_file = pd.read_excel('data_lake/landing/{}.xls'.format(year), header = 2)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
          

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
