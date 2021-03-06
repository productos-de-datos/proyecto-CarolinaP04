'''
ingest_data(): extraer desde una fuente los archivos que seran utilizados 
y llevarlos a una carpeta del directorio. 
(ejm: origen = repositorio de github, tipo de archivo descargado = xls o xlsx)
'''

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
            origen = f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{year}.xls?raw=true'
            wget.download(origen, out = 'data_lake/landing')
        else:
            origen =  f'https://github.com/jdvelasq/datalabs/blob/master/datasets/precio_bolsa_nacional/xls/{year}.xlsx?raw=true'
            wget.download(origen, out = 'data_lake/landing')
        
        
if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    ingest_data()
 