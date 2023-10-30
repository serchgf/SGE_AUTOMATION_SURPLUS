import logging

from Config.config import images, login_data

""" FUNCIONES DE CREACION DE DATOS """
def MTC_SURSGE_creation_steps(sge_funct, archivo_cm_Dso_temp, archivo_cm_zonas_temp, archivo_cm_workzone_temp, archivo_cm_localizaciones_permanentes_temp, archivo_cm_asignacion_producto_localizacion_temp, archivo_cm_asignacion_zona_producto_temp):
    print("Ingresar uu (cambiar usuario) ")
    sge_funct.activar_cambio_usuario()
    print("Ingresar el usuario sfabian0")
    sge_funct.send_text("sfabian0")
    print("Press Enter")
    sge_funct.press_enter()
    print("Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("3 Press Enter")
    sge_funct.press_enter()
    print("4 Teclear input 2")
    sge_funct.send_text('2')
    print("5 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 9")
    sge_funct.send_text('9')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("6 Teclear input 15")
    sge_funct.send_text('15')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA DSO *******************
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_dso.txt")
    sge_funct.leer_archivo_productos(archivo_cm_Dso_temp)


    sge_funct.segundos_de_espera(1)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("6 Teclear input 8")
    sge_funct.send_text('8')
    print("7 Teclear input Enter")
    sge_funct.press_enter()

    # ************** CREACION CARGA MASIVA ZONAS *******************
    print("10 Presionamos ctrl + F para vizualizar controsl de zonas")
    sge_funct.press_hotkeys('ctrl+f')
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    sge_funct.segundos_de_espera(3)
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_zonas_temp)

    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("6 Teclear input 12")
    sge_funct.send_text('12')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA WORKZONE *******************
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_workzone_temp)
    sge_funct.segundos_de_espera(3)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian0 ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("6 Teclear input 14")
    sge_funct.send_text('14')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA LOCALIZACIONES *******************
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_localizaciones_permanentes_temp)
    sge_funct.segundos_de_espera(3)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("6 Teclear input 8")
    sge_funct.send_text('8')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA ASIGNACION LOCALIZACION Y ZONA *******************
    # ************** LOCALIZACION DEL ARTICULO Y LIMITES *******************
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("Seleccionamos Localizaciones y Limites ")
    sge_funct.send_text('1')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_asignacion_producto_localizacion_temp)
    sge_funct.segundos_de_espera(3)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("6 Teclear input 8")
    sge_funct.send_text('8')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    # ************** ASIGNACION DE ZONA DEL ARTICULO *******************
    print("10 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("Seleccionamos Localizaciones y Limites ")
    sge_funct.send_text('2')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("11 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_asignacion_zona_producto_temp)
    sge_funct.segundos_de_espera(3)
    print("13 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("16 introducimos el password ")
    sge_funct.send_text('123')
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("17 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    #RELLENAR CANTIDAD PRODUCTO DE  TEMPORAL A LOCALIZACION PERMANENTE
    print("Teclear input 13")
    sge_funct.send_text('13')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input c")
    sge_funct.send_text('c')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 99")
    sge_funct.send_text('99')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input CH243")
    sge_funct.send_text('ch243')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input m")
    sge_funct.send_text('m')
    print("selecionar la temporal ")
    sge_funct.flecha_abajo()
    print("13 Presionamos ctrl + D")
    sge_funct.press_hotkeys('ctrl+d')
    print("Teclear input P01B0101A")
    sge_funct.send_text('P01B0101A')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 100000")
    sge_funct.send_text('100000')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input s")
    sge_funct.send_text('s')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input Enter")
    sge_funct.press_enter()

class eliminacion_steps:

    """ FUNCIONES DE ELIMINACION DE DATOS """
    def inicio_comun(self, sge_funct, data):
        print("Trying to Connect...")
        sge_funct.sge_connection(login_data.linux_username,login_data.ip, login_data.password)
        print("Validating connection...")
        assert sge_funct.validate_adm_sge_connection(
            images.img_sge_adm_pantalla_inicial), "Error Found, SGE Connection Failed!!"
        sge_funct.segundos_de_espera(2)
        print("Ingresar uu (cambiar usuario) ")
        sge_funct.activar_cambio_usuario()
        print("Ingresar el usuario sfabian0")
        sge_funct.segundos_de_espera(1)
        sge_funct.send_text(data["usuario"])
        print("Press Enter")
        sge_funct.press_enter()
        print("Ingresar numero de sucursal ")
        sge_funct.send_text(data["sucursal_origen"])
        sge_funct.segundos_de_espera(1)
        sge_funct.validar_sucursal_seleccionada(data["sucursal_origen"])
        print("Press Enter")
        sge_funct.press_enter()
        print("6.-Teclear input 2")
        sge_funct.send_text('2')
        print("7.-Teclear input Enter")
        sge_funct.press_enter()
        print("8.-Teclear input 9")
        sge_funct.send_text('9')
        print("9.-Teclear input Enter")
        sge_funct.press_enter()

    def eliminar_localizacion(self, sge_funct,img_r_no_existe_localizacion_1,data):
        """ valida si hay localizacion para eliminar y regresa True si no hay dato para eliminar """
        # ************** LIBERAR LA LOCALIZACION *******************
        print("10.-Teclear input 13")
        sge_funct.send_text('13')
        print("11.-Teclear input Enter")
        sge_funct.press_enter()
        print("12.-Teclear input c")
        sge_funct.send_text('c')
        print("13.-Teclear input Enter")
        sge_funct.press_enter()
        print("14.-Teclear input 99")
        sge_funct.send_text(data["linea"])
        print("15.-Teclear input Enter")
        sge_funct.press_enter()
        print("16.-Teclear input ch243")
        sge_funct.send_text(data["codigo"])
        print("17.-Teclear input Enter")
        sge_funct.press_enter()
        return sge_funct.validate_image_x(img_r_no_existe_localizacion_1)

    def quitar_la_asignacion_de_la_localizacion(self, sge_funct,data):
        """ valida si hay localizacion asignada para eliminar y regresa True si no hay dato para eliminar"""
        logging.info("************** QUITAR LA ASIGNACION DE LA LOCALIZACION *******************")
        # ************** QUITAR LA ASIGNACION DE LA LOCALIZACION *******************
        print("29.-Teclear input 8")
        sge_funct.send_text('8')
        print("30.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("31.-Teclear input 01 ingresar almacen")
        sge_funct.send_text(data["almacen"])
        print("32.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("33.-Teclear input 99")
        sge_funct.send_text(data["linea"])
        print("34.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("35.-Teclear input CH243")
        sge_funct.send_text(data["codigo"])
        print("36.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("37.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()

        print("38.-Teclear input 1")
        sge_funct.send_text('1')
        return sge_funct.validate_image_x(images.img_r_borrar_asignacion_de_localizacion)

    def quitar_la_asignacion_de_la_zona(self, sge_funct, data):
        """ valida si hay asignacion de zona para eliminar y regresa True si no hay dato para eliminar"""
        print("29.-Teclear input 8")
        sge_funct.send_text('8')
        print("30.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("31.-Teclear input 01 ingresar almacen")
        sge_funct.send_text(data["almacen"])
        print("32.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("33.-Teclear input 99")
        sge_funct.send_text(data["linea"])
        print("34.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("35.-Teclear input CH243")
        sge_funct.send_text(data["codigo"])
        print("36.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("37.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("38.-Teclear input 2")
        sge_funct.send_text('2')
        return sge_funct.validate_image_x(images.img_r_borrar_asignacion_de_la_zona)

    def eliminacion_de_la_localizacion_y_tipo(self, sge_funct,data):
        """ valida si hay workzone CON LOCALIZACION Y TIPO para eliminar y regresa True SI HAY dato para eliminar """
        # ************** ELIMINACION DE LA LOCALIZACION Y TIPO *******************
        print("54.-Teclear input 14")
        sge_funct.send_text('14')
        print("55.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("56.-Presionamos Tab para buscar por workzone")
        sge_funct.press_tab()
        sge_funct.segundos_de_espera(2)
        print("57.-Teclear input T_WZ_01M")
        sge_funct.escribir_wz_temporal()
        wz_name = sge_funct.doubleclick_axis_y(images.img_r_borrar_workzone_loctipo_dobleclic_2, 30)
        if data['work_zone'] == wz_name:
            logging.info("se encontro la workzone con localizacion y tipo")
            print("58.-Presionamos ctrl + E")
            sge_funct.press_hotkeys('ctrl+e')
            print("59.-Teclear input S")
            sge_funct.send_text('s')
            print("60.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("61.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("62.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            return True
        else:
            return False

    def eliminacion_de_work_zone(self, sge_funct,data):
        """ valida si hay workzone para eliminar y regresa True SI HAY dato para eliminar """
        # ************** ELIMINACION DE WORK ZONE *******************
        print("63.-Teclear input 12")
        sge_funct.send_text('12')
        print("64.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("65.-Teclear input 01 ")
        sge_funct.send_text('01 ')
        print("66.-Presionamos Tab para buscar por workzone")
        sge_funct.press_tab()
        sge_funct.segundos_de_espera(2)
        print("67.-Teclear input T_WZ_01P")
        sge_funct.escribir_wz_temporal()
        wz_name = sge_funct.doubleclick_axis_y(images.img_r_workzone_dobleclic, 20)
        if data['work_zone'] == wz_name:
            logging.info("Workzone encontrada")
            print("68.-Presionamos ctrl + E")
            sge_funct.press_hotkeys('ctrl+e')
            print("69.-Teclear input S")
            sge_funct.send_text('s')
            print("70.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("71.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("72.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            return True
        else:
            return False

    def eliminacion_de_la_zona(self, sge_funct,data):
        """ valida si hay zona para eliminar y regresa FALSE SI HAY dato para eliminar """
        # ************** ELIMINACION DE ZONA *******************
        print("73.-Teclear input 8")
        sge_funct.send_text('8')
        print("74.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("75.-Presionamos ctrl + F")
        sge_funct.press_hotkeys('ctrl+f')
        print("76.-Presionamos C")
        sge_funct.send_text('c')
        print("77.-Presionamos 12")
        sge_funct.send_text('12')
        print("78.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("79.-Presionamos 01")
        sge_funct.send_text('01')
        print("80.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("81.-Presionamos 990")
        sge_funct.send_text('990')
        if sge_funct.validate_image_x(images.img_r_no_existe_el_la_zona_verifique):
            print("no existe el la zona ... verifique")
            return False
        else:
            print("82.-Presionamos B")
            sge_funct.send_text('b')
            print("83.-Presionamos S")
            sge_funct.send_text('s')
            print("84.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            if sge_funct.validate_image_x(images.img_r_validacion_de_eliminacion_de_zona):
                print("Se Elimino el Registro zona 990")
                print("85.-Presionamos ctrl + A")
                sge_funct.press_hotkeys('ctrl+a')
                print("86.-Presionamos ctrl + A")
                sge_funct.press_hotkeys('ctrl+a')
                return True
            else:
                print("No Se encontro la zona")
                return False

    def eliminacion_de_dso(self, sge_funct,data):
        """ valida si hay DSO para eliminar y regresa True SI HAY dato para eliminar """
        # ************** ELIMINACION DE DSO *******************
        print("87.-Teclear input 15")
        sge_funct.send_text('15')
        print("88.-Presionamos Enter para continuar Enter")
        sge_funct.press_enter()
        print("89.-Presionamos 'TAB'")
        sge_funct.press_tab()
        print("90.-Presionamos Z01")
        sge_funct.send_text('Z01')
        dso_name = sge_funct.doubleclick_axis_y(images.img_r_validacion_existencia_DSO, 20)
        sge_funct.segundos_de_espera(2)
        if data['dso'] == dso_name:
            print("91.-Presionamos ctrl + E")
            sge_funct.press_hotkeys('ctrl+e')
            print("92.-Teclear input S")
            sge_funct.send_text('s')
            print("93.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("94.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            return True
        else:
            return False

    def relleno_cantidad_permante_a_multiple(self, sge_funct,data):
        logging.info("************** RELLENO DE CANTIDAD PERMANENTE A MULTIPLE *******************")
        print("18.-Teclear input m")
        sge_funct.send_text('m')
        print("19.- Presionamos ctrl + D")
        sge_funct.press_hotkeys('ctrl+d')
        print("20.-Teclear input T61B6161G localizacion destino")
        sge_funct.send_text(data["localizacion_destino"])
        print("21.-Teclear input Enter")
        sge_funct.press_enter()
        print("22.-Teclear input 100000")
        sge_funct.send_text(data["cantidad_a_mover"])
        print("23.-Teclear input Enter")
        sge_funct.press_enter()
        print("24.-Teclear input s")
        sge_funct.send_text('s')
        print("25.-Teclear input Enter")
        sge_funct.press_enter()
        print("26.-Teclear input Enter")
        sge_funct.press_enter()
        print("27.-Presionamos ctrl + A")
        sge_funct.press_hotkeys('ctrl+a')
        print("28.-Presionamos ctrl + A")
        sge_funct.press_hotkeys('ctrl+a')

    # SECUENCIA DE ELIMINACION
    # 1 BUSCAR Y ELIMINAR LOCALIZACION
    # 2 BUSCAR Y ELIMINAR ASIGNACION DE LOCALIZACION
    # 3 BUSCAR Y ELIMINAR ASIGNACION DE LA ZONA
    # 4 BUSCAR Y ELIMINAR LOCALIZACION Y TIPO
    # 5 BUSCAR Y ELIMINAR WORKZONE
    # 6 BUSCAR Y ELIMINAR ZONA
    # 7 BUSCAR Y ELIMINAR DSO

    def buscar_y_eliminar_localizacion(self, sge_funct, data):
        self.inicio_comun(sge_funct, data)
        """ Funcion para buscar y eliminar localizacion """
        logging.info("buscar y eliminar localizacion")
        if self.eliminar_localizacion(sge_funct, images.img_r_no_existe_localizacion_1, data):
            logging.info("localizacion no encontrada")
            message = "localizacion_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info("************** ELIMINANDO LA LOCALIZACION ENCONTRADA *******************")
            self.relleno_cantidad_permante_a_multiple(sge_funct, data)
            message = "localizacion_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()

    def buscar_y_eliminar_asignacion_de_localizacion(self, sge_funct, data):
        self.inicio_comun(sge_funct, data)

        """ Funcion para buscar y eliminar la asignacion de localizacion """
        if self.quitar_la_asignacion_de_la_localizacion(sge_funct, data):
            logging.info("asignacion de localizacion no encontrada")
            message = "asignacion_de_localizacion_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            sge_funct.segundos_de_espera(1)
            sge_funct.clean_field()
            print("40.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("41.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("42.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            sge_funct.segundos_de_espera(2)
            print("43.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            print("44.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            print("45.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("46.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("47.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            print("48.-Presionamos Enter para continuar Enter")
            sge_funct.press_enter()
            message = "asignacion_localizacion_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()


    def buscar_y_eliminar_asignacion_de_la_zona(self,sge_funct, data):
        """ Funcion para buscar y eliminar asignacion de la zona """
        logging.info("buscar y eliminar asignacion de la zona")
        self.inicio_comun(sge_funct, data)

        if self.quitar_la_asignacion_de_la_zona(sge_funct, data):
            logging.info("asignacion de la zona no encontrada")
            message = "asignacion_de_zona_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info("************** ELIMINANDO LA ASIGNACION DE ZONA ENCONTRADA *******************")
            print("50.-Teclear input 002")
            sge_funct.send_text('002')
            print("51.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            print("52.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            print("53.-Presionamos ctrl + A")
            sge_funct.press_hotkeys('ctrl+a')
            message = "asignacion_de_zona_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()

    def buscar_y_eliminar_localizacion_y_tipo(self, sge_funct, data):
        self.inicio_comun(sge_funct, data)

        """ Funcion para buscar y eliminar Localizacion y Tipo """
        logging.info("buscar y eliminar Localizacion y Tipo")
        if self.eliminacion_de_la_localizacion_y_tipo(sge_funct, data):
            logging.info("Localizacion y Tipo encontrada")
            logging.info("************** ELIMINANDO LA LOCALIZACION Y TIPO ENCONTRADA *******************")
            message = "localizacion_y_tipo_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info(" localizacion y tipo no encontrada ")
            message = "localizacion_y_tipo_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()


    def buscar_y_eliminar_workzone(self, sge_funct, data):
        """ Funcion para buscar y eliminar Workzone """
        logging.info("buscar y eliminar Workzone")
        self.inicio_comun(sge_funct, data)
        if self.eliminacion_de_work_zone(sge_funct, data):
            logging.info("************** ELIMINANDA LA WORKZONE ENCONTRADA *******************")
            message = "workzone_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info("Workzone no encontrada ")
            message = "workzone_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()

    def buscar_y_eliminar_zona(self, sge_funct, data):
        """ Funcion para buscar y eliminar zona """
        logging.info("buscar y eliminar Zona")
        self.inicio_comun(sge_funct, data)
        if self.eliminacion_de_la_zona(sge_funct, data):
            logging.info("Zona encontrada")
            logging.info("************** ELIMINANDO LA ZONA ENCONTRADA *******************")
            message = "zona_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info("Zona no encontrada ")
            message = "zona_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()

    def buscar_y_eliminar_dso(self, sge_funct, data):
        """ Funcion para buscar y eliminar DSO """
        logging.info("buscar y eliminar DSO")
        self.inicio_comun(sge_funct, data)
        if self.eliminacion_de_dso(sge_funct, data):
            logging.info("DSO encontrada")
            logging.info("************** ELIMINANDO LA DSO ENCONTRADA *******************")
            message = "dso_eliminada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()
        else:
            logging.info("DSO no encontrada ")
            message = "dso_no_encontrada"
            sge_funct.take_screenshot(message)
            sge_funct.close_sge_session()








