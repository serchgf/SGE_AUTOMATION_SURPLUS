import pytest
from Config.config import login_data, images, files
from Sge_functions.sge_functions2 import sge_functions2
#from ddt import ddt, file_data
from Config.config import images
from steps import MTC_SURSGE_001_steps
from pytest import mark
from preconditions import Entry_to_Articles_steps
from preconditions import importe_de_venta_menor_al_costo_steps
import json

#Funciones globales para usar en todos lados

def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()

def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos

@mark.precondition
class Sge_preconditions_Tests:


    # @pytest.mark.flaky(reruns=1)
    @mark.importeMenor
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.importe_venta_menor_al_costo_json))
    def test_preconditions_importe_de_venta_menor_al_costo(self, data):
        sge_funct = sge_functions2()
        print("------------------------------Test preconditions_importe_de_venta_menor_al_costo")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        importe_de_venta_menor_al_costo_steps.pre_importe_de_venta_menor_al_costo(sge_funct, data)
        #sge_funct.close_sge_session()


    # @pytest.mark.flaky(reruns=1)
    @mark.entryArticles
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.entry_to_articles_json))
    def test_entry_to_articles(self, data):
        sge_funct = sge_functions2()
        print("------------------------------Test preconditions calculate cost and entry articules")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        Entry_to_Articles_steps.pre_Entry_to_Articles(sge_funct, data)# poner assert para control de inventarios

        assert sge_funct.validate_image_x(images.img_costo_adquisicion), "Error del costo de adquision"
        costo_de_adquisicion = sge_funct.doubleclick_axis_xy(images.img_costo_adquisicion, 30, 20)
        assert "1.00" == costo_de_adquisicion, "Error el costo de adquisicion es incorrecto"
        print(costo_de_adquisicion)
        sge_funct.close_sge_session()

        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        Entry_to_Articles_steps.calculate_and_entry_articles(sge_funct, costo_de_adquisicion, 100, data)
        sge_funct.close_sge_session()

# @ddt
class MTC_SURSGE_001_Tests:

    @pytest.mark.parametrize("data", cargar_datos_prueba(files.mtc_sursge_001_json))
    #@pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_SUR_001(self, data):
        # print("Test using: "+supplier)
        sge_funct = sge_functions2()
        print("------------------------------Test to Create invoice")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        MTC_SURSGE_001_steps.MTC_SURSGE_001_steps(sge_funct, data)
        assert sge_funct.validate_image_x(images.img_registro_alta), "Error en la creacion de DSO"
        print("Validacion realizada con exito")
        sge_funct.close_sge_session()

