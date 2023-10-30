"""
pip install pytest-html
pip install ansi2html
pip install ddt
"""
import os


class login_data:
    # uat02
    apuntando_A = "surplus"
    ambiente = "UAT02"
    linux_username = "itmx12"
    password = "sgem5986"
    ip = "172.22.210.22"#"desarrollo.oreillyauto.mx"
    #ip = "172.22.220.136" # ambiente de QA
    usuario_de_compras = "sfabian"


class csv_files_path:
    main_dir = "Config/TestDataSet/"
    csv_x_name = "Config/TestDataSet/x_name.csv"


class txt_files_path:
    main_dir = "Config/TestDataSet/"
    file_name = "tmpmasivo.txt"
    txt_file = main_dir + file_name
    carga_masiva_txt = "Config/TestDataSet/tmpmasivo.txt"
    cm_dso_txt = "Config/TestDataSet/cm_dso.txt"
    cm_zonas_txt = "Config/TestDataSet/cm_zonas.txt"
    cm_workzone_txt = "Config/TestDataSet/cm_workzone.txt"
    cm_localizacion_permante_txt = "Config/TestDataSet/cm_localizaciones_permanentes.txt"
    cm_localizacion_multiple_txt = "Config/TestDataSet/cm_localizaciones_multiples.txt"
    cm_regresion = "Config/TestDataSet/cm_regresion.txt"
    cm_asig_loc_perm_producto_txt = "Config/TestDataSet/cm_asig_loc_perm_producto.txt"
    cm_asig_zon_perm_producto_txt = "Config/TestDataSet/cm_asig_zon_perm_producto.txt"
    cm_localizaciones_y_limites_txt = "Config/TestDataSet/cm_localizaciones_y_limites.txt"
    cm_zonas_del_articulo_txt = "Config/TestDataSet/cm_zonas_del_articulo.txt"
    cm_relleno_pem_a_mul_txt = "Config/TestDataSet/cm_relleno_pem_a_mul.txt"
    cm_relleno_mul_a_mul_txt = "Config/TestDataSet/cm_relleno_mul_a_mul.txt"
    cm_relleno_mul_a_pem_txt = "Config/TestDataSet/cm_relleno_mul_a_pem.txt"


class images:
    """images location"""
    ROOT = os.path.abspath(os.path.join(".", os.pardir))
    img_pantalla_modificacion_datos_f2_f00 = "image_files/pantalla_modificacion_de_datos_del_f2_f00.png"
    img_pantalla_mod02 = "image_files/pantalla_mod02.png"
    img_costo_adquisicion = "image_files/costo_adquision_vigente.png"
    img_pantalla_inicial = f"image_files/pantallaInicial.png"
    img_error_connection = f"image_files/errorConexion2.png"
    img_error_atraso_importante = f"image_files/Error atraso importante.png"
    img_promociones = f"image_files/promociones.png"
    img_promociones2 = f"image_files/promociones2.png"
    img_sge_adm_pantalla_inicial = f"image_files/sge_adm_pantalla_inicial.png"
    img_folio_generado_validacion = f"image_files/folioGeneradoValidacion.png"
    img_allure_screenshot_name = "my_allure_screenshot.png"
    img_allure_screenshot_path = "/Screenshots/my_allure_screenshot.png"
    img_seleccion_sucursal_12 = "image_files/seleccion_sucursal_12.png"
    img_sucursal_12_selec_mods = "image_files/sucursal_12_selec_mods.png"
    img_error_cedi_preferente = f"image_files/error_cedi_preferente.png"
    img_change_loc_perm_perm = "image_files/change_loc_perm_perm.png"
    img_inicio_factura = "image_files/inicioFactura.png"
    img_validacion_devolucion = "image_files/devolución_total_a_permanente.png"
    img_vale_interno = "image_files/vale_interno.png"
    img_folioEmbarque = "image_files/ultimo_folio_embarque.png"
    img_validacion_traspaso = "image_files/validacion_traspaso.png"
    img_validacion_tc22 = "image_files/validacion_tc22.png"
    SUCURSALES = {
        '1': 'image_files/sucursal_1.png', '2': 'image_files/sucursal_2.png', '3': 'image_files/sucursal_3.png',
        '4': 'image_files/sucursal_4.png', '5': 'image_files/sucursal_5.png', '6': 'image_files/sucursal_6.png',
        '7': 'image_files/sucursal_7.png', '8': 'image_files/sucursal_8.png', '9': 'image_files/sucursal_9.png',
        '10': 'image_files/sucursal_10.png', '11': 'image_files/sucursal_11.png', '12': 'image_files/sucursal_12.png',
        '13': 'image_files/sucursal_13.png', '14': 'image_files/sucursal_14.png', '15': 'image_files/sucursal_15.png',
        '16': 'image_files/sucursal_16.png', '17': 'image_files/sucursal_17.png', '18': 'image_files/sucursal_18.png',
        '19': 'image_files/sucursal_19.png', '20': 'image_files/sucursal_20.png', '21': 'image_files/sucursal_21.png',
        '22': 'image_files/sucursal_22.png', '23': 'image_files/sucursal_23.png', '24': 'image_files/sucursal_24.png',
        '25': 'image_files/sucursal_25.png', '26': 'image_files/sucursal_26.png', '27': 'image_files/sucursal_27.png',
        '28': 'image_files/sucursal_28.png', '29': 'image_files/sucursal_29.png', '30': 'image_files/sucursal_30.png',
        '31': 'image_files/sucursal_31.png', '32': 'image_files/sucursal_32.png', '33': 'image_files/sucursal_33.png',
        '34': 'image_files/sucursal_34.png', '35': 'image_files/sucursal_35.png', '36': 'image_files/sucursal_36.png',
        '37': 'image_files/sucursal_37.png', '38': 'image_files/sucursal_38.png', '39': 'image_files/sucursal_39.png',
        '40': 'image_files/sucursal_40.png', '41': 'image_files/sucursal_41.png', '42': 'image_files/sucursal_42.png',
        '43': 'image_files/sucursal_43.png', '44': 'image_files/sucursal_44.png', '45': 'image_files/sucursal_45.png',
        '46': 'image_files/sucursal_46.png', '47': 'image_files/sucursal_47.png'}

    # SURPLUS
    img_dso_cm_guardadas = "image_files/cm_dso_guardadas.png"
    img_zonas_cm_guardadas = "image_files/cm_zonas_guardadas.png"
    img_workzone_cm_guardadas = "image_files/cm_workzone_guardadas.png"
    img_localizaciones_p_cm_guardadas = "image_files/cm_localizaciones_permanentes_guardadas.png"
    img_localizaciones_m_cm_guardadas = "image_files/cm_localizaciones_multiples_guardadas.png"
    img_asig_loc_prod_perm = "image_files/cm_asig_loc_prod_perm.png"
    img_asig_zon_prod_perm = "image_files/cm_asig_zon_prod_perm.png"
    img_localizaciones_y_limites = "image_files/cm_localizaciones_y_limites.png"
    img_asignar_zona_a_producto = "image_files/cm_asignar_zona_a_producto.png"
    img_relleno_pem_a_mul = "image_files/cm_relleno_pem_a_mul.png"
    img_relleno_mul_a_mul = "image_files/cm_relleno_mul_a_mul.png"
    img_relleno_mul_a_pem = "image_files/cm_relleno_mul_a_pem.png"

    img_registro_alta = f"image_files/registro_dado_alta.png"  # GRECIA 25/07/2023 DSO y workzone
    img_registro_actualizado = f"image_files/registro_actualizado.png"  # GRECIA 25/07/2023 ZONA
    img_registro_alta_correctamente = f"image_files/registro_dado_alta_correctamente.png"  # GRECIA 25/07/2023
    # ZONA
    img_registro_alta_localizacion = f"image_files/registro_dado_alta_localizacion.png"  # GRECIA 26/07/2023 Localizacion
    img_prueba_localizacion_m = f"image_files/prueba_localizacion_m.png"  # GRECIA 26/07/2023 Localizacion
    img_asignacion_localizacion_permanente = f"image_files/asignacion_localizacion_permanente_codigo.png"  # GRECIA 27/07/2023 Localizacion
    img_cant_actualizada_correctamente = f"image_files/cantidad_actualizada_correctamente_relleno.png"  # GRECIA 27/07/2023 relleno

    # precondiciones
    img_utilerias_menu = "image_files/utilerias_homescreen.png"
    """
    validar que realice la regresion o 
    eliminacion del end to end
    """
    img_r_borrado_de_zona = "image_files/r_borrado_de_zona.png"
    img_r_borrar_asignacion_de_localizacion = "image_files/r_borrar_asignacion_de_localizacion.png"
    img_r_dso_dobleclic = "image_files/r_dso_dobleclic.png"
    img_r_Localizacion_dobleclic = "image_files/r_Localizacion_dobleclic.png"
    img_r_validacion_de_desvinculacion_de_zona = "image_files/r_validacion_de_desvinculacion_de_zona.png"
    img_r_validacion_de_eliminacion_de_DSO = "image_files/r_validacion_de_eliminacion_de_DSO.png"
    img_r_validacion_de_eliminacion_de_zona = "image_files/r_validacion_de_eliminacion_de_zona.png"
    img_r_validacion_de_localizacion = "image_files/r_validacion_de_localizacion.png"
    img_r_validacion_existencia_DSO = "image_files/r_validacion_existencia_DSO.png"
    img_r_workzone_dobleclic = "image_files/r_workzone_dobleclic.png"
    img_r_zona_dobleclic = "image_files/r_zona_dobleclic.png"
    img_r_borrar_asignacion_de_la_zona = "image_files/r_borrar_asignacion_de_la_zona.png"
    img_r_no_existe_el_la_zona_verifique = "image_files/r_no_existe_el_la_zona_verifique.png"
    img_r_no_existe_localizacion_1 = "image_files/r_no_existe_localizacion_1.png"
    img_r_borrar_workzone_loctipo_dobleclic = "image_files/r_borrar_workzone_loctipo_dobleclic.png"
    img_r_borrar_workzone_loctipo_dobleclic_2="image_files/r_borrar_workzone_loctipo_dobleclic_2.png"

class files:
    directory_tmp_file = "tmp_file/"
    screenshot_folder = "Screenshots/"
    mtc_sursge_001_json = "Config/TestDataSet/mtc_sursge_001.json"
    mtc_sursge_003_json = "Config/TestDataSet/mtc_sursge_003.json"
    mtc_sursge_005_json = "Config/TestDataSet/mtc_sursge_005.json"
    mtc_sursge_007_json = "Config/TestDataSet/mtc_sursge_007.json"
    mtc_sursge_009_json = "Config/TestDataSet/mtc_sursge_009.json"
    mtc_sursge_011_json = "Config/TestDataSet/mtc_sursge_011.json"
    mtc_sursge_013_json = "Config/TestDataSet/mtc_sursge_013.json"
    mtc_sursge_015_json = "Config/TestDataSet/mtc_sursge_015.json"
    mtc_sursge_017_json = "Config/TestDataSet/mtc_sursge_017.json"
    mtc_sursge_019_json = "Config/TestDataSet/mtc_sursge_019.json"
    entry_to_articles_json = "Config/TestDataSet/entry_to_articles.json"
    importe_venta_menor_al_costo_json = "Config/TestDataSet/importe_venta_menor_al_costo.json"
    mtc_sursge_021_json = "Config/TestDataSet/mtc_sursge_021.json"
    mtc_sursge_022_json = "Config/TestDataSet/mtc_sursge_022.json"
    mtc_sursge_023_json = "Config/TestDataSet/mtc_sursge_023.json" #
    mtc_sursge_024_json = "Config/TestDataSet/mtc_sursge_024.json" #
    mtc_sursge_025_json = "Config/TestDataSet/mtc_sursge_025.json" #
    mtc_sursge_026_json = "Config/TestDataSet/mtc_sursge_026.json" #
    mtc_sursge_027_json = "Config/TestDataSet/mtc_sursge_027.json" #
    mtc_sursge_028_json = "Config/TestDataSet/mtc_sursge_028.json" #
    mtc_sursge_029_json = "Config/TestDataSet/mtc_sursge_029.json" #
    mtc_sursge_030_json = "Config/TestDataSet/mtc_sursge_030.json" #

    eliminar_datos_json = "Config/TestDataSet/eliminar_datos.json"
    #tc 28
    cm_traspasos_file = "Config/TestDataSet/cm_traspasos.txt"
    entry_to_articles = "Config/TestDataSet/Entry_to_Articles2.json"
    importe_venta_menor_al_costo = "Config/TestDataSet/importe_venta_menor_al_costo2.json"
    # test creation de test data
    t_dso = "Config/TestDataSet/t_dso.txt"
    t_zona = "Config/TestDataSet/t_zona.txt"
    t_wz = "Config/TestDataSet/t_wz.txt"
    t_l_p = "Config/TestDataSet/t_l_p.txt"
    t_a_l_p = "Config/TestDataSet/t_a_l_p.txt"
    t_a_z_p = "Config/TestDataSet/t_a_z_p.txt"
    cm_regresion = "Config/TestDataSet/cm_regresion.txt"

