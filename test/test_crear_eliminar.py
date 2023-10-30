import logging
import unittest
import pytest
from Config.config import login_data, txt_files_path, files
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_SURSGE_regresion_steps as sur_steps
# from ddt import ddt, file_data
from Config.config import images


# @ddt
class MTC_SURSGE_regresion_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    # @pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_regresion(self):
        sge_funct = sge_functions2()
        logging.info("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
        print("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        sur_steps.MTC_SURSGE_regresion_steps(sge_funct, files.cm_regresion)
        print("Validating Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva")
        #sur_steps.MTC_SURSGE_creation_steps(sge_funct, files.t_dso, files.t_zona, files.t_wz,  files.t_l_p, files.t_a_l_p,                                            files.t_a_z_p)



        #assert sge_funct.validate_image_x(images.img_localizaciones_p_cm_guardadas), "Error, asignar_localizacion_permanente_a_producto_carga_masiva not created"
        #print("asignar_localizacion_per
        # manente_a_producto_carga_masiva created successfull")


    def test_MTC_SURSGE_crear(self):
        sge_funct = sge_functions2()
        logging.info("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
        print("------------Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva------------------")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        sur_steps.MTC_SURSGE_creation_steps(sge_funct, files.t_dso, files.t_zona, files.t_wz,  files.t_l_p, files.t_a_l_p,                                            files.t_a_z_p)
        print("Validating Test to Create_asignar_localizacion_permanente_a_producto_carga_masiva")






    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()