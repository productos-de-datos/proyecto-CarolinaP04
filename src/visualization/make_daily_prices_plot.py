'''
make_daily_prices_plot(): crear un grafico de líneas (.png) para mostrar los promedios de los precios diarios.
Estableciendo las características personalizadas (ejm: tamaño, encabezado, eje x, eje y).
'''

def make_daily_prices_plot():
    """Crea un grafico de lines que representa los precios promedios diarios.

    Usando el archivo data_lake/business/precios-diarios.csv, crea un grafico de
    lines que representa los precios promedios diarios.

    El archivo se debe salvar en formato PNG en data_lake/business/reports/figures/daily_prices.png.

    """
    # raise NotImplementedError("Implementar esta función")

    import pandas as pd
    import matplotlib.pyplot as plt

    precios_diarios = pd.read_csv('data_lake/business/precios-diarios.csv')
    precios_diarios['Fecha'] = pd.to_datetime(precios_diarios["Fecha"])

    x = precios_diarios['Fecha']
    y = precios_diarios['precio']

    plt.figure(figsize=(14, 4)) 
    plt.plot(x, y, label='Promedio Diario') 
    plt.title('Precio Promedio Diario') 
    plt.xlabel('Fecha') 
    plt.ylabel('Precio') 
    plt.savefig("data_lake/business/reports/figures/daily_prices.png") 

if __name__ == "__main__":
    import doctest
    
    doctest.testmod()
    make_daily_prices_plot()
