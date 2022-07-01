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
        
        if year <= 1999:
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx', index_col = None, header = None)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
        
        elif year > 1999 and year <= 2015:
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx', index_col = None, header = None)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
        
        elif year > 2015 and year <= 2017:
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx', index_col = None, header = None)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)

        else:
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx',  index_col = None)
            df = read_file.iloc[:, :25]
            df.to_csv(f'data_lake/raw/{year}.csv', index=False)
            

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data() 
