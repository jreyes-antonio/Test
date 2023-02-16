import pandas as pd
import sqlite3

datos_vuelo = pd.read_csv('vuelos.csv')
datos_pilotos = pd.read_csv("pilotos.csv",encoding='ANSI' )

conexion = sqlite3.connect('datos.db')
datos_vuelo.to_sql('tabla_vuelo', conexion, if_exists='replace', index=False)
datos_pilotos.to_sql('tabla_pilotos', conexion, if_exists='replace', index=False)



########################   QUERYS #############################
#¿Qué aerolínea tiene más vuelos?
query1 =  pd.read_sql_query('SELECT Aerolínea,count(*) as vuelos FROM tabla_vuelo GROUP BY Aerolínea ORDER BY vuelos DESC limit 1', conexion)

# ¿Qué Origen se repite más?

query2 = pd.read_sql_query('SELECT Origen,count(*) as total FROM tabla_vuelo GROUP BY Origen ORDER BY total DESC limit 1', conexion)

#¿Desde donde vuela más la aerolínea 8?

query3 = pd.read_sql_query('SELECT Origen,count(*) as total FROM tabla_vuelo WHERE Aerolínea = 8  GROUP BY Origen ORDER BY total DESC limit 1', conexion)

#¿Hacia dónde vuela más la aerolínea 4?

query4 = pd.read_sql_query('SELECT Destino,count(*) as total FROM tabla_vuelo WHERE Aerolínea = 4  GROUP BY Destino ORDER BY total DESC limit 1', conexion)

#¿Qué piloto vuela más?

query5 = pd.read_sql_query('SELECT Piloto FROM tabla_pilotos WHERE "Codigo Piloto" = (SELECT "Codigo Piloto" FROM (SELECT "Codigo Piloto",count(*) as total FROM tabla_vuelo GROUP BY "Codigo Piloto" ORDER BY total DESC limit 1))', conexion)


############################## PYTHON ###############################

# En primer instancia se deben cargar los archivos vuelos y pilotos a un dataframe
# datos_vuelo & datos_pilotos

#Agregar en la hoja Vuelos un campo para el nombre del piloto
#Insertar el nombre del piloto
datos_vuelo_piloto = pd.merge(datos_vuelo, datos_pilotos, on='Codigo Piloto')

#Descartar/marcar los registros donde Origen y Destino sean iguales.
datos_limpios = datos_vuelo_piloto.drop(datos_vuelo_piloto[datos_vuelo_piloto['Origen'] == datos_vuelo_piloto['Destino']].index)

#Agregar comentario en ONTIME, si el tiempo en valor absoluto es menor o igual a 30 A, si es esta entre 30 y 50 B, si es mayor que 50 C.
datos_limpios['ONTIME'] = datos_limpios['Minutos de retraso'].apply(lambda x: 'A' if abs(x) <= 30 else ('B' if abs(x) <= 50 else ('C' if abs(x) > 50 else '')))


#¿Quién es el piloto que tiene más vuelos A?
piloto = datos_limpios[datos_limpios["ONTIME"] == "A"]["Piloto"].mode()[0]
#R: El piloto que tiene más vuelos en A es: Jonh Pierson

#¿Qué aerolínea tiene más vuelos C?
vuelos = datos_limpios[datos_limpios["ONTIME"] == "C"]["Aerolínea"].mode()[0]
#R: La aerolínea que más vuelos tiene en C es: la número 4

#¿Para qué aerolínea vuela Hung Cho?
aerolinea_de_piloto = df.loc[datos_limpios["Piloto"] == "Hung Cho", "Aerolínea"].iloc[0]
#R: La aerolínea de Hung Cho es: la aerolínea número 9

#¿Cuántos vuelos A, B, C tiene Chao Ma?
Chao_Ma = datos_limpios[datos_limpios['Piloto'] == 'Chao Ma']
cantidad_vuelos = Chao_Ma['ONTIME'].count()
#R: Chao Ma tiene un total de: 10 vuelos
