# Estudio de condiciones para plantaciones de cacao


En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos como parte de una nueva agenda de desarrollo sostenible. Para el 2030, se busca luchar contra la desertificación, rehabilitar las tierras y los suelos degradados, incluidas de las tierras afectadas por la desertificación, la sequía y las inundaciones, y procurar lograr un mundo con una degradación neutra del suelo.

El Ministerio de Agricultura y Desarrollo Rural busca recuperar los suelos para el cultivo del cacao. Para poder cumplir con esto han iniciado el análisis para las características del entorno donde se tiene previsto iniciar las plantaciones. Para esta tarea lo requieren a usted y se facilita una tabla que describe si el entorno es apto o no.

| CARACTERISTICAS | SUMAMENTE APTO | MODERADAMENTE APTO | MARGINALMENTE APTO | NO APTO |
| --- | --- | --- | --- | --- |
| Altura sobre el nivel del mar (m.s.n.m) | 400 - 800 ] | < 400 o 801 - 999 | 999 - 1200 | > 1200 |
| Temperatura media anual (°C) | 24 - 28 | 28 - 30 o 24 - 20 | 31 - 32 o 20 - 18 | < 18 o > 32 |
| Precipitación anual (mm) | 1800 - 2599 | 2600 - 3199 o 1799 - 1500	| 3200 - 3800 o 1499 - 1200 |	< 1200 o > 3800 |
| Profundidad efectiva del suelo (cm)	| > 100	| 50 - 100	| 25 - 50	| < 25 |

Para esta nueva fase se requiere un estudio más a fondo. Ahora se cuenta con dos matrices, estas llevan registros de diferentes medidas de una zona a lo largo de una semana de precipitación anual y la profundidad efectiva del suelo.

| Dia 1 | Dia 2 | Dia 3 | Dia 4 | Dia 5 | Dia 6 | Dia 7 |
| --- | --- | --- | --- | --- | --- | --- |
| Precipitacion 1,1 | Precipitacion 1,2 | Precipitacion 1,3 | Precipitacion 1,4 | Precipitacion 1,5 | Precipitacion 1,6 | Precipitacion 1,7 |
| Precipitacion 2,1 | Precipitacion 2,2 | Precipitacion 2,3 | Precipitacion 2,4 | Precipitacion 2,5 | Precipitacion 2,6 | Precipitacion 2,7 |
| ... | ... | ... | ... | ... | ... | ... |
| Precipitacion N,1 | Precipitacion N,2 | Precipitacion N,3 | Precipitacion N,4 | Precipitacion N,5 | Precipitacion N,6 | Precipitacion N,7 |

| Dia 1 | Dia 2 | Dia 3 | Dia 4 | Dia 5 | Dia 6 | Dia 7 |
| --- | --- | --- | --- | --- | --- | --- |
| Profundidad 1,1 | Profundidad 1,2 | Profundidad 1,3 | Profundidad 1,4 | Profundidad 1,5 | Profundidad 1,6 | Profundidad 1,7 |
| Profundidad 2,1 | Profundidad 2,2 | Profundidad 2,3 | Profundidad 2,4 | Profundidad 2,5 | Profundidad 2,6 | Profundidad 2,7 |
| ... | ... | ... | ... | ... | ... | ... |
| Profundidad N,1 | Profundidad N,2 | Profundidad N,3 | Profundidad N,4 | Profundidad N,5 | Profundidad N,6 | Profundidad N,7 |

Las posiciones correspondientes en cada matriz hacen referencia a una misma lectura, es decir, precipitación 2,3 y profundidad 2,3 hacen referencia los valores obtenidos en la zona 2 en el día 3.

El número de zonas a analizar se debe leer como un parámetro de entrada, seguida la matriz de precipitaciones y por último la matriz de profundidades.

Se debe mostrar por pantalla:
-	El conteo total de las categorías, separados por espacio, a las que pertenecen las lecturas de las matrices en el siguiente orden: no apto, marginalmente apto, moderadamente apto, sumamente apto.
- La categoría que más se presentó por cada zona, separadas por coma. En caso de que existan dos, escoger la mejor categoría.
- La categoría que menos se presentó por cada zona, separadas por coma. En caso de que existan dos, escoger la mejor categoría.

El criterio para la conclusión será el siguiente:

-	Si ambas variables se encuentran dentro de la misma categoría se escogerá la categoría.
-	Si están en categorías diferentes se escogerá la peor de ellas.


Ejemplo 1:
| Entrada esperada |
| --- |
| 3	|
| 2012 1631 1740 3161 1929 3587 3506 |
| 3103 1656 2549 1619 1385 2730 1988 |
| 1186 1199 3372 2368 3361 3714 1414 |
| 71 59 100 103 95 38 62 |
| 64 54 61 40 22 77 103 |
| 39 27 66 46 63 26 46 |

| Salida Esperada |
| --- |
| 3 8 9 1	|
| moderadamente apto,moderadamente apto,marginalmente apto, marginalmente apto,sumamente apto,no apto |
