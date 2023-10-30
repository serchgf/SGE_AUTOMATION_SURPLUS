import json
import logging
import pytest
from Config.config import login_data, files
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_SURSGE_029_steps as surp_steps
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
class MTC_SURSGE_029_Tests:

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    @pytest.mark.parametrize("data", cargar_datos_prueba(files.mtc_sursge_029_json))
    # @pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_029(self, data):
        # print("Test using: "+supplier)

        sge_funct = sge_functions2()
        logging.info("------------------------------Test to Generar traspaso SUC CEDI urgente total manual a permanente")
        print("------------------------------Test to Generar traspaso SUC CEDI urgente total manual a permanente")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        #surp_steps.precondicion_mtc_SURSGE_028(sge_funct,images.img_utilerias_menu)
        surp_steps.MTC_SURSGE_029_steps(sge_funct, data, images.img_vale_interno)
        print("Validating Generar traspaso SUC CEDI urgente total manual a permanente")
        if sge_funct.validate_image_x(images.img_validacion_traspaso):
            logging.info("Generar traspaso SUC CEDI urgente total manual a permanente success")
            print("Generar traspaso SUC CEDI urgente total manual a permanente success")
        else:
            logging.error("Error, validation Failed")
            print("Error, validation Failed")
            #sge_funct.terminate_sge_session()
            assert False



