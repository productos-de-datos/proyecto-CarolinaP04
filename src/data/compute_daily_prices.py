'''
compute_daily_prices(): promediar los precios diarios agrupando el archivo 
y calculado la media mediante pandas.
'''
def compute_daily_prices():
    """Compute los precios promedios diarios.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio diario (sobre las 24 horas del dia) para cada uno de los dias. Las
    columnas del archivo data_lake/business/precios-diarios.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio diario de la electricidad en la bolsa nacional



    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    precios_diarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    precios_diarios = precios_diarios[['Fecha', 'precio']]  
    precios_diarios.groupby(["Fecha"])["precio"].mean() 
    precios_diarios.to_csv('data_lake/business/precios-diarios.csv', index=False) 

if __name__ == "__main__":
    import doctest   
    doctest.testmod()
    compute_daily_prices()
    