"""
Módulo de ingestión de datos.
-------------------------------------------------------------------------------

"""


def ingest_data():
    """Ingeste los datos externos a la capa landing del data lake.

    Del repositorio jdvelasq/datalabs/precio_bolsa_nacional/xls/ descarge los
    archivos de precios de bolsa nacional en formato xls a la capa landing. La
    descarga debe realizarse usando únicamente funciones de Python.

    """
    # raise NotImplementedError("Implementar esta función")

    import wget

    for year in range(1995, 2022):
        
        if year == 2016 or year == 2017:
            origen = f'https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls/{year}.xls?raw=true'
            wget.download(origen, out = 'data_lake/landing')
        else:
            origen =  f'https://github.com/jdvelasq/datalabs/tree/master/datasets/precio_bolsa_nacional/xls/{year}.xlsx?raw=true'
            wget.download(origen, out = 'data_lake/landing')
        
        return
   
        raise NotImplementedError("Implementar esta función")
        
if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    ingest_data()
