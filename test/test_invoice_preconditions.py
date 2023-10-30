import logging
import unittest
import pytest
from pytest import mark
from Config.config import login_data, images, files
from Sge_functions.sge_functions2 import sge_functions2
from preconditions import Entry_to_Articles_steps
from preconditions import importe_de_venta_menor_al_costo_steps
import json


def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()


def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos


@mark.precondition
class Sge_preconditions_Tests:


    @pytest.mark.flaky(reruns=1)
    @mark.importeMenor
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.importe_venta_menor_al_costo))
    def test_preconditions_importe_de_venta_menor_al_costo(self, data):
        sge_funct = sge_functions2()
        print("------------------------------Test preconditions_importe_de_venta_menor_al_costo")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        importe_de_venta_menor_al_costo_steps.pre_importe_de_venta_menor_al_costo(sge_funct, data)



    @pytest.mark.flaky(reruns=1)
    @mark.entryArticles
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.entry_to_articles))
    def test_entry_to_articles(self, data):
        sge_funct = sge_functions2()
        print("------------------------------Test preconditions calculate cost and entry articules")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        Entry_to_Articles_steps.pre_Entry_to_Articles(sge_funct, data)# poner assert para control de inventarios

        assert sge_funct.validate_image_x(images.img_costo_adquisicion), "Error del costo de adquision"
        costo_de_adquisicion = sge_funct.doubleclick_axis_xy(images.img_costo_adquisicion, 20, 10)
        assert "1.00" == costo_de_adquisicion, "Error el costo de adquisicion es incorrecto"
        print(costo_de_adquisicion)
        sge_funct.close_sge_session()
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Trying to Connect...")
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error de conexion"
        Entry_to_Articles_steps.calculate_and_entry_articles(sge_funct, costo_de_adquisicion, 999999, data)

