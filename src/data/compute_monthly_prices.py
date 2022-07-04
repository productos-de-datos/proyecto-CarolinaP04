def compute_monthly_prices():
    """Compute los precios promedios mensuales.

    Usando el archivo data_lake/cleansed/precios-horarios.csv, compute el prcio
    promedio mensual. Las
    columnas del archivo data_lake/business/precios-mensuales.csv son:

    * fecha: fecha en formato YYYY-MM-DD

    * precio: precio promedio mensual de la electricidad en la bolsa nacional



    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd

    precios_horarios = pd.read_csv('data_lake/cleansed/precios-horarios.csv')
    precios_horarios = precios_horarios[['Fecha', 'precio']]
    precios_horarios['mes'] = precios_horarios['Fecha'].str[:7] + '-01'  
    precios_mensuales = precios_horarios.groupby('mes', as_index = False).mean()
    precios_mensuales.columns = ['Fecha', 'precio']
    precios_mensuales.to_csv('data_lake/business/precios-mensuales.csv', index=False)

if __name__ == "__main__":
    import doctest

    doctest.testmod()
    compute_monthly_prices()
    