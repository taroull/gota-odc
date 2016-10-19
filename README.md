# gota-odc
Trabajos realizados en torno a los datos del grupo GOTA.

---

## NetCDF Converter

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

---
