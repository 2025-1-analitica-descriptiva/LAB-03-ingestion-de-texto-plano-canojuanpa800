"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import os
import re
import pandas as pd
from pprint import pprint
def get_data(file_path):
    headers = []
    with open(file_path,"r",encoding="utf-8") as file:
        headers = file.readlines()[4:]
    return headers

def get_lines(file_path):
    lines = []
    with open(file_path,"r",encoding="utf-8") as file:
        lines = file.readlines()
    return lines

def join_rows(data):
    join_rows = []
    join_row = ''
    for row in data:
        if row == '\n' or row == '                                         \n':
            join_rows.append(join_row)
            join_row = ''
            continue
        join_row += row
    return join_rows

def clear_data(data):
    result_data = []
    for row in data:
        # eliminar espacios innecesarios y saltos de linea
        result_row = []
        row = row.replace('\n','')
        row = re.sub(r"\s+", " ", row)

        # utilizar el simbolo % para separar la ultima columna
        f_part_row,s_part_row = row.split('%')[0],row.split('%')[1].strip()

        # separar la primera parte en 3 columnas y castear sus tipos de datos numericos
        f_part_list = f_part_row.strip().split(" ")
        f_part_list = [int(f_part_list[0]), int(f_part_list[1]), float(f_part_list[2].replace(",","."))] 
        
        # eliminar el simbolo . de las palabras claves
        s_part_row = s_part_row.replace(".","").strip()
    
        # construir el registro
        result_row += f_part_list
        result_row.append(s_part_row) 

        # almacenar los registros
        result_data.append(result_row) 
    return result_data

def pregunta_01():
    """Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:
    El dataframe tiene la misma estructura que el archivo original.
    Los nombres de las columnas deben ser en minusculas, reemplazando los
    espacios por guiones bajos.
    Las palabras clave deben estar separadas por coma y con un solo
    espacio entre palabra y palabra."""
    
    directory = "./files/input"
    file = "clusters_report.txt"
    file_path = os.path.join(directory,file)
    data = get_data(file_path)
    data = join_rows(data)
    data = clear_data(data)



    df = pd.DataFrame(data, columns=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    return df

# pregunta_01()