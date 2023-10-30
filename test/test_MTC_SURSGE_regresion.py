import json
import logging


import pytest
from pytest import mark

from Config.config import login_data, files
from Sge_functions.sge_functions2 import sge_functions2
from steps.MTC_SURSGE_regresion_steps1 import eliminacion_steps
# from ddt import ddt, file_data
from Config.config import images

def leer_datos_desde_json(json_path):
    with open(json_path) as archivo:
        datos = json.load(archivo)
    return datos.values()


def cargar_datos_prueba(json_path):
    datos = leer_datos_desde_json(json_path)
    return datos



# @ddt
class MTC_SURSGE_regresion_Tests():

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    # @pytest.mark.flaky(reruns=1)
    @mark.eliminar
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.eliminar_datos_json))
    def test_MTC_SURSGE_regresion(self, data):
        sge_funct = sge_functions2()
        eliminacion_s = eliminacion_steps()
        logging.info("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
        print("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")

        # 1 BUSCAR Y ELIMINAR LOCALIZACION
        logging.info("************** 1 BUSCAR Y ELIMINAR LOCALIZACION *******************")
        eliminacion_s.buscar_y_eliminar_localizacion(sge_funct, data)
        # 2 BUSCAR Y ELIMINAR ASIGNACION DE LOCALIZACION
        logging.info("************** 2 BUSCAR Y ELIMINAR ASIGNACION DE LOCALIZACION *******************")
        eliminacion_s.buscar_y_eliminar_asignacion_de_localizacion(sge_funct, data)
        # 3 BUSCAR Y ELIMINAR ASIGNACION DE LA ZONA
        logging.info("************** 3 BUSCAR Y ELIMINAR ASIGNACION DE LA ZONA *******************")
        eliminacion_s.buscar_y_eliminar_zona(sge_funct, data)
        # 4 BUSCAR Y ELIMINAR LOCALIZACION Y TIPO
        logging.info("************** 4 BUSCAR Y ELIMINAR LOCALIZACION Y TIPO *******************")
        eliminacion_s.buscar_y_eliminar_localizacion_y_tipo(sge_funct, data)
        # 5 BUSCAR Y ELIMINAR WORKZONE
        logging.info("************** 5 BUSCAR Y ELIMINAR WORKZONE *******************")
        eliminacion_s.buscar_y_eliminar_workzone(sge_funct, data)
        # 6 BUSCAR Y ELIMINAR ZONA
        logging.info("************** 6 BUSCAR Y ELIMINAR ZONA *******************")
        eliminacion_s.buscar_y_eliminar_zona(sge_funct, data)
        # 7 BUSCAR Y ELIMINAR DSO
        logging.info("************** 7 BUSCAR Y ELIMINAR DSO *******************")
        eliminacion_s.buscar_y_eliminar_dso(sge_funct, data)

    # @mark.crear
    # @pytest.mark.parametrize("data", cargar_datos_prueba(files.eliminar_datos_json))
    # def test_MTC_SURSGE_crear(self, data):
    #     sge_funct = sge_functions2()
    #     logging.info(
    #         "------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
    #     print(
    #         "------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
    #     print("Trying to Connect...")
    #     sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
    #     print("Validating connection...")
    #     assert sge_funct.validate_adm_sge_connection(
    #         images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
    #     print("Validating Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva")
    #     sur_steps.MTC_SURSGE_creation_steps(sge_funct, files.t_dso,
    #                                         files.t_zona, files.t_wz,
    #                                         files.t_l_p, files.t_a_l_p,
    #                                         files.t_a_z_p)






    # assert sge_funct.validate_image_x(images.img_localizaciones_p_cm_guardadas), "Error, asignar_localizacion_permanente_a_producto_carga_masiva not created"
    # print("asignar_localizacion_permanente_a_producto_carga_masiva created successfull")

