''' 
clean_data(): crear un archivo unico (ejm:.csv), a partir de una lista de archivos, indicando las columnas que debe contener 
el archivo creado. 
'''

def clean_data():
    """Realice la limpieza y transformación de los archivos CSV.
    Usando los archivos data_lake/raw/*.csv, 
    cree el archivo data_lake/cleansed/precios-horarios.csv.
    Las columnas de este archivo son:

    * fecha: fecha en formato YYYY-MM-DD
    * hora: hora en formato HH
    * precio: precio de la electricidad en la bolsa nacional

    Este archivo contiene toda la información del 1997 a 2021.

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import os
    import glob

    origen = os.path.join('data_lake/raw/', "*.csv")
    list_files = glob.glob(origen)

    df = pd.concat(map(pd.read_csv, list_files), ignore_index=True)
    df["Fecha"] = pd.to_datetime(df["Fecha"], format="%Y/%m/%d")
    df2 = pd.melt(df, id_vars=["Fecha"], value_vars = df.columns[1:], var_name= "hora", value_name= "precio")
    df2["hora"] = df2["hora"].replace({'H':''}, regex=True)
    df2["hora"] = pd.to_numeric(df2["hora"])
    df2.to_csv('data_lake/cleansed/precios-horarios.csv',index=False)

# Tests para verificar creacion de archivo y numero de columnas
def test_file():
    import os
    assert os.path.isfile('data_lake/cleansed/precios-horarios.csv') is True

def test_column_number():
    import pandas as pd
    precios_horarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    assert 3 == len(precios_horarios.columns)
 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
    clean_data()
