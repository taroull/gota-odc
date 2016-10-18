#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Dado un fichero en formato NetCDF, se genera:
- Un fichero JSON con las especificaciones generales.
- Un fichero CSV con los valores para cada una de las variables definidas.
- Un fichero CSV con todas las variables y todos los valores

Ejecución: python netcdf_converter.py fichero_de_entrada.nc variable_de_salida
'''

from netCDF4 import Dataset
import numpy as np
import json
import os.path
import sys
from itertools import product

def get_type_convert(np_type):
  convert_type = type(np.zeros(1, np_type).tolist()[0]).__name__
  return convert_type

def netcdfvar_to_csv(nc_var):
  output_list = []
  if nc_var.ndim in (1, 2):
    output_file = nc_var.name + '.csv'
    np.savetxt(output_file, nc_var[:], delimiter = ', ', fmt = '%.8f', newline = '\n')
    output_list.append(output_file)
  elif nc_var.ndim == 3:
    num_files = nc_var.shape[0]
    for i in range(num_files):
      nc_data = nc_var[i]
      output_file = nc_var.name + '_' + str(i) + '.csv'
      np.savetxt(output_file, nc_data, delimiter = ', ', fmt = '%.8f', newline = '\n')
      output_list.append(output_file)

  return output_list

def nc_values_to_csv(nc, var_name, output_file):
  output_file = os.path.splitext(output_file)[0] + '.csv'
  with open(output_file, 'w') as out_file:
    out_file.write( ', '.join(nc.variables[var_name].dimensions) + ', ' + var_name + '\n')
    nc_list = []
    for dim in nc.variables[var_name].dimensions:
      nc_list.append(nc.variables[dim][:])
    for vals in product(*nc_list):
      line = ""
      d = nc.variables[var_name][:]    
      for i in range(len(vals)):
        line += str(vals[i]) + ', ' 
        d = d[ nc.variables[nc.variables[var_name].dimensions[i]][:].tolist().index(vals[i]) ]
      line += str(d) + '\n'
      out_file.write(line)
    

def netcdf_to_json(nc, output_file):
  # Global attributes
  global_attrs = { key: value if not isinstance(value, np.generic) else np.asscalar(value) for key, value in nc.__dict__.items() }

  # Variables
  vars_list = []
  for var_name in nc.variables.keys():
    var_dict = {}
    for attr_name in nc.variables[var_name].ncattrs():
      value = getattr(nc.variables[var_name], attr_name)
      if isinstance(value, np.generic):
        value = np.asscalar(value)
      var_dict[attr_name] = value

      var_dict['files_values'] = netcdfvar_to_csv(nc.variables[var_name])
      var_dict['short_name'] = var_name
      var_dict['type'] = get_type_convert(nc.variables[var_name].datatype.type)
      var_dict['shape'] = str(nc.variables[var_name].shape)
      var_dict['ndim'] = nc.variables[var_name].ndim
      var_dict['dimensions'] = str(nc.variables[var_name].dimensions)

    vars_list.append(var_dict)

  # Dimensions
  dims_list = []
  for var_name in nc.dimensions:
    dim_dict = {}
    dim_dict['name'] = nc.dimensions[var_name].name
    dim_dict['size'] = nc.dimensions[var_name].size
    dims_list.append(dim_dict)

  # Output
  output_dict = {
    'variables': vars_list,
    'dimensions': dims_list,
    'attributes': global_attrs
  }  

  output_file = os.path.splitext(output_file)[0] + '.json'
  with open(output_file, 'w') as out_file:
    json.dump(output_dict, out_file, sort_keys = True, indent = 3)


def main(argv):
  filename = argv[0]
  var_name = argv[1]
  nc = Dataset(filename, 'r', Format='NETCDF4')
  netcdf_to_json(nc, filename)

  # All variables values to one big CSV
  nc_values_to_csv(nc, var_name, filename)

if __name__ == '__main__':
    main(sys.argv[1:])
