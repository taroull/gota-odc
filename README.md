# gota-odc
---
Trabajos realizados en torno a los datos del grupo GOTA.
* NetCDF Converter
* Notebook: Mapa GOTA

## NetCDF Converter
---
Convierte un fichero científico en formato `NetCDF` a una combinación de `JSON` y `CSV`, con el objetivo de hacer los datos más ‘amigables’.

Dado un fichero en formato `NetCDF`, se genera:
* Un fichero `JSON` con las especificaciones generales.
* Para cada una de las variables definidas, un fichero `CSV` con sus valores.
* Un fichero `CSV` con todas las variables y todos los valores.

### Ejecución:

```
python netcdf_converter.py ficheroDeEntrada.nc variableDeSalida
```

Por ejemplo: 
```
python netcdf_converter.py dif_t2max_day_2090_2099_rcp85_wrf341wrf4g_ll_yseasmean.nc T2MAX
```

## Notebook: Mapa GOTA
---
Ejemplo de uso de datos abiertos del portal Open Data Canarias.

Para llevar a cabo este ejemplo se han hecho uso de los datos [**Proyecciones climáticas de temperatura máxima en Canarias para el período 2090-2100 (RCP4.5)**](http://www.opendatacanarias.es/datos/dataset/gota-ull-proyecciones-climaticas-de-temperatura-maxima-en-canarias-para-el-periodo-2090-2100-rcp4-5/resource/7c1bc250-73f0-400a-b5e9-ea4f93a30683) en formato `NetCDF` extraidos del portal Open Data Canarias.

Estas proyecciones han sido realizadas por el *Grupo de Observación de la Tierra y la Atmósfera (GOTA)* de la Universidad de La Laguna utilizando modelos numéricos de regionalización climática y la técnica "Pseudo-Global-Warming" para evaluar el efecto del cambio climático en una región orográficamente compleja como Canarias.

Las proyecciones se realizaron para el escenario de emisiones de gases de efecto invernadero definidos en el IPCC: RCP4.5 (escenario en el que se adoptan medidas para mitigar el cambio climático) y RCP8.5 (escenario más desfavorable en el que no se toman medidas).

Los resultados que se aportan en este conjunto de datos (expresados por medias estacionales), pueden interpretarse de la siguiente forma:

Diferencias de temperaturas máximas respecto al periodo actual (1995-2004) para el período temporal: final (2090-2100) de siglo, y para el escenario de cambio seleccionado: RCP45.

**NOTA:** Si se desea usar cualquier otro archivo `NetCDF` de los aportados por el grupo GOTA, simplemente hay que modificar la variable `my_example_nc_file` con la ruta al fichero deseado y las variables que la componen.
