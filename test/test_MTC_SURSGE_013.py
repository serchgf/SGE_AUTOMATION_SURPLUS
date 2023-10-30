import pytest
import unittest
from Config.config import login_data, files
from Sge_functions.sge_functions2 import sge_functions2
#from ddt import ddt, file_data
from Config.config import images
from steps import MTC_SURSGE_013_steps

import json

#Funciones globales para usar en todos lados
def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()

def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos

#@ddt
class MTC_SURSGE_013_Tests:

    @pytest.mark.parametrize("data", cargar_datos_prueba(files.mtc_sursge_013_json))
    #@pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_SUR_013(self, data):

        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        MTC_SURSGE_013_steps.MTC_SURSGE_013_steps(sge_funct, data)
        assert sge_funct.validate_image_x(images.img_asignacion_localizacion_permanente), "Error en la asignacion de zona al producto"
        print("Validacion realizada con exito")

        sge_funct.close_sge_session()

