import logging
import unittest
from Config.config import login_data, txt_files_path
from Sge_functions.sge_functions2 import sge_functions2
from steps import MTC_SURSGE_006_steps as sur_steps
# from ddt import ddt, file_data
from Config.config import images


# @ddt
class MTC_SURSGE_006_Tests(unittest.TestCase):

    # @file_data("./Config/TestDataset/dataSet_ddt_invoice_credit_simple_order.json")
    # @pytest.mark.flaky(reruns=1)
    def test_MTC_SURSGE_006(self):
        sge_funct = sge_functions2()
        logging.info("------------Test to Create_Work_Zone_carga_masiva------------------")
        print("------------Test to Create_Work_Zone_carga_masiva------------------")
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username, login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        sur_steps.MTC_SURSGE_006_steps(sge_funct, txt_files_path.cm_workzone_txt)
        print("Validating carga masiva WorkZone")
        assert sge_funct.validate_image_x(images.img_workzone_cm_guardadas), "Error, WorkZone Carga masiva not created"
        print("WorkZone carga masiva created successfull")

    def tearDown(self):
        sge_funct = sge_functions2()
        sge_funct.close_sge_session()


if __name__ == '__main__':
    unittest.main()