/* ¿Qué aerolínea tiene más vuelos? */
SELECT Aerolínea,count(*) as vuelos FROM tabla_vuelo GROUP BY Aerolínea ORDER BY vuelos DESC limit 1
/* La Aerolínea que más vuelos tiene es la número 7 */


/* ¿Qué Origen se repite más? */
SELECT Origen,count(*) as total FROM tabla_vuelo GROUP BY Origen ORDER BY total DESC limit 1
/* El origen que más se repite es: SAP con un total de 1404 vuelos    */


/*¿Desde donde vuela más la aerolínea 8? */
SELECT Origen,count(*) as total FROM tabla_vuelo WHERE Aerolínea = 8  GROUP BY Origen ORDER BY total DESC limit 1
/* La aerolínea número 8 vuela más a : SAP con un total de 134 vuelos  */


/*¿Hacia dónde vuela más la aerolínea 4? */
SELECT Destino,count(*) as total FROM tabla_vuelo WHERE Aerolínea = 4  GROUP BY Destino ORDER BY total DESC limit 1
/* La aerolínea 4 vueltas más a : SAP con un total de 141 vuelos" */


/*¿Qué piloto vuela más? */
SELECT Piloto FROM tabla_pilotos WHERE "Codigo Piloto" = (SELECT "Codigo Piloto" FROM (SELECT "Codigo Piloto",count(*) as total FROM tabla_vuelo GROUP BY "Codigo Piloto" ORDER BY total DESC limit 1))
/* El piloto que más vuela es: Jonh Pierson  */