import logging
import unittest
from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_SURSGE_020_steps as sur_steps
# from ddt import ddt, file_data
from Config.config import images


# @ddt
class MTC_SURSGE_020_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    # @pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_020(self):
        sge_funct = sge_functions2()
        logging.info("------------Test to Relleno_localizacion_multiple_a_permanente_masiva------------------")
        print("------------Test to Create_Relleno_localizacion_multiple_a_permanente_masiva------------------")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        sur_steps.MTC_SURSGE_020_steps(sge_funct, txt_files_path.cm_relleno_mul_a_pem_txt)
        print("Validating Test to Relleno_localizacion_multiple_a_permanente_masiva")
        assert sge_funct.validate_image_x(images.img_relleno_mul_a_pem), "Error, Relleno_localizacion_multiple_a_permanente_masiva not created"
        print("Relleno_localizacion_multiple_a_permanente_masiva created successfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        #sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()