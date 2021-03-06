'''
transform_data(): transformar los archivos en formato xls o xlsx a formato csv, 
considerando la fecha y horas contenidas en los archivos.
'''

def transform_data():
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    # raise NotImplementedError("Implementar esta función")

    import openpyxl
    import pandas as pd

    for year in range (1995,2022):
        
        if year in range (1995,2016):
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx',index_col=None)
            df = read_file.dropna(how = "any")
            df = df.iloc[1:,:25]
            df.columns = ["Fecha","H00","H01","H02","H03",
            "H04","H05","H06","H07","H08","H09","H10","H11","H12","H13",
            "H14","H15","H16","H17","H18","H19","H20","H21","H22","H23"]
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y/%m/%d")
            df.to_csv(f'data_lake/raw/{year}.csv', index_label= False, index = False) 

        elif year in range (2018,2022):
            read_file = pd.read_excel(f'data_lake/landing/{year}.xlsx',index_col=None, header = None)
            df = read_file.iloc[1:,:25]
            df.columns = ["Fecha","H00","H01","H02","H03",
            "H04","H05","H06","H07","H08","H09","H10","H11","H12","H13",
            "H14","H15","H16","H17","H18","H19","H20","H21","H22","H23"]
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y/%m/%d")
            df.to_csv(f'data_lake/raw/{year}.csv', index_label= False, index = False)  

        elif year == 2016  or year == 2017:
            read_file = pd.read_excel(f'data_lake/landing/{year}.xls',index_col=None,header = None)
            df = read_file.dropna(how = "any")
            df = df.iloc[1:,:25]
            df.columns = ["Fecha","H00","H01","H02","H03",
            "H04","H05","H06","H07","H08","H09","H10","H11","H12","H13",
            "H14","H15","H16","H17","H18","H19","H20","H21","H22","H23"]
            df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y/%m/%d")
            df.to_csv(f'data_lake/raw/{year}.csv', index_label= False, index = False)    

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    transform_data()
