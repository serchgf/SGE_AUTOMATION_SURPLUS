def MTC_SURSGE_creation_steps(sge_funct, archivo_cm_Dso_temp, archivo_cm_zonas_temp, archivo_cm_workzone_temp, archivo_cm_localizaciones_permanentes_temp, archivo_cm_asignacion_producto_localizacion_temp, archivo_cm_asignacion_zona_producto_temp):
    print("1 Ingresar uu (cambiar usuario) ")
    sge_funct.activar_cambio_usuario()
    print("2 Ingresar el usuario sfabian0")
    sge_funct.send_text("sfabian0")
    print("3 Press Enter")
    sge_funct.press_enter()
    print("4 Ingresar numero de sucursal ")
    sge_funct.send_text('12')
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("5  Press Enter")
    sge_funct.press_enter()
    print("6 Teclear input 2")
    sge_funct.send_text('2')
    print("7 Teclear input Enter")
    sge_funct.press_enter()
    print("8 Teclear input 9")
    sge_funct.send_text('9')
    print("9 Teclear input Enter")
    sge_funct.press_enter()
    print("10 Teclear input 15")
    sge_funct.send_text('15')
    print("11 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA DSO *******************
    print("12 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("13 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_dso.txt")
    sge_funct.leer_archivo_productos(archivo_cm_Dso_temp)


    sge_funct.segundos_de_espera(1)
    print("14 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("15 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("16 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("17 introducimos el password ")
    sge_funct.send_text('123')
    print("18 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("19 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("20 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("21 Teclear input 8")
    sge_funct.send_text('8')
    print("22 Teclear input Enter")
    sge_funct.press_enter()

    # ************** CREACION CARGA MASIVA ZONAS *******************
    print("23 Presionamos ctrl + F para vizualizar controsl de zonas")
    sge_funct.press_hotkeys('ctrl+f')
    print("24 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    sge_funct.segundos_de_espera(3)
    print("25 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_zonas_temp)

    print("26 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("27 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("28 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("29 introducimos el password ")
    sge_funct.send_text('123')
    print("30 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("31 Teclear input Enter")
    sge_funct.press_enter()
    print("32 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("33 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("34 Teclear input 12")
    sge_funct.send_text('12')
    print("35 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA WORKZONE *******************
    print("36 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("37 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_workzone_temp)
    sge_funct.segundos_de_espera(3)
    print("38 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("39 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("40 Presionamos Enter para cambiar al campo password de sfabian0 ")
    sge_funct.press_enter()
    print("41 introducimos el password ")
    sge_funct.send_text('123')
    print("42 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("43 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("44 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("45 Teclear input 14")
    sge_funct.send_text('14')
    print("46 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA LOCALIZACIONES *******************
    print("47 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("48 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_localizaciones_permanentes_temp)
    sge_funct.segundos_de_espera(3)
    print("49 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("50 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("51 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("52 introducimos el password ")
    sge_funct.send_text('123')
    print("53 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("54 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("55 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("56 Teclear input 8")
    sge_funct.send_text('8')
    print("57 Teclear input Enter")
    sge_funct.press_enter()
    # ************** CREACION CARGA MASIVA ASIGNACION LOCALIZACION Y ZONA *******************
    # ************** LOCALIZACION DEL ARTICULO Y LIMITES *******************
    print("58 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("59 Seleccionamos Localizaciones y Limites ")
    sge_funct.send_text('1')
    print("60 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("61 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_asignacion_producto_localizacion_temp)
    sge_funct.segundos_de_espera(3)
    print("62 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("63 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("64 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("65 introducimos el password ")
    sge_funct.send_text('123')
    print("66 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("67 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("68 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("69 Teclear input 8")
    sge_funct.send_text('8')
    print("70 Teclear input Enter")
    sge_funct.press_enter()
    # ************** ASIGNACION DE ZONA DEL ARTICULO *******************
    print("71 Presionamos ctrl + U para carga masiva")
    sge_funct.press_hotkeys('ctrl+u')
    print("Seleccionamos Localizaciones y Limites ")
    sge_funct.send_text('2')
    print("72 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("73 Oprimir click derecho del mouse para Pegar los datos de carga masiva cm_zonas.txt")
    sge_funct.leer_archivo_productos(archivo_cm_asignacion_zona_producto_temp)
    sge_funct.segundos_de_espera(3)
    print("74 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("75 Presionamos ctrl + W")
    sge_funct.press_hotkeys('ctrl+w')
    print("76 Presionamos Enter para cambiar al campo password de sfabian ")
    sge_funct.press_enter()
    print("77 introducimos el password ")
    sge_funct.send_text('123')
    print("78 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("79 Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("80 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("81 Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    #RELLENAR CANTIDAD PRODUCTO DE  TEMPORAL A LOCALIZACION PERMANENTE
    print("82 Teclear input 13")
    sge_funct.send_text('13')
    print("83 Teclear input Enter")
    sge_funct.press_enter()
    print("84 Teclear input c")
    sge_funct.send_text('c')
    print("85 Teclear input Enter")
    sge_funct.press_enter()
    print("86 Teclear input 99")
    sge_funct.send_text('99')
    print("87 Teclear input Enter")
    sge_funct.press_enter()
    print("88 Teclear input CH243")
    sge_funct.send_text('ch243')
    print("89 Teclear input Enter")
    sge_funct.press_enter()
    print("90 Teclear input m")
    sge_funct.send_text('m')
    print("91 selecionar la temporal ")
    sge_funct.flecha_abajo()
    print("92 Presionamos ctrl + D")
    sge_funct.press_hotkeys('ctrl+d')
    print("93 Teclear input P01B0101A")
    sge_funct.send_text('P01B0101A')
    print("94 Teclear input Enter")
    sge_funct.press_enter()
    print("95 Teclear input 100000")
    sge_funct.send_text('100000')
    print("96 Teclear input Enter")
    sge_funct.press_enter()
    print("97 Teclear input s")
    sge_funct.send_text('s')
    print("98 Teclear input Enter")
    sge_funct.press_enter()
    print("99 Teclear input Enter")
    sge_funct.press_enter()








def MTC_SURSGE_regresion_steps(sge_funct,data):
    # esta funcion recibe como parametro una instancia de la clase SGE functions y un archivo co los productos
    print("Ingresar uu (cambiar usuario) ")
    sge_funct.activar_cambio_usuario()
    print("Ingresar el usuario sfabian0")

    sge_funct.send_text(data["usuario"].lower())
    print("Press Enter")
    sge_funct.press_enter()
    print("Ingresar numero de sucursal ")
    sge_funct.send_text(data["sucursal_origen"])
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_seleccionada(data["sucursal_origen"])
    print("Press Enter")
    sge_funct.press_enter()
    print("Teclear input 2")
    sge_funct.send_text('2')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 9")
    sge_funct.send_text('9')
    print("Teclear input Enter")
    sge_funct.press_enter()
    # ************** LIBERAR LA LOCALIZACION *******************
    print("Teclear input 13")
    sge_funct.send_text('13')
    print("Teclear input Enter")
    sge_funct.press_enter()

    print("Teclear input c")
    sge_funct.send_text('c')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input 99")
    sge_funct.send_text(data["linea"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input ch243")
    sge_funct.send_text(data["codigo"])
    print("Teclear input Enter")
    sge_funct.press_enter()
#funcion 1
    # validacion No tiene localizacion funcion

    assert sge_funct.validar_imagen_x(img_notieneLocalizacion), "No se puede eliminar porque No tiene localizacion o ya fue eliminada"


# funcion 2 borrrar la asignacion de localizacion





    print("Teclear input m")
    sge_funct.send_text('m')
    print("13 Presionamos ctrl + D")
    sge_funct.press_hotkeys('ctrl+d')
    print("Teclear input T61B6161G localizacion destino")
    sge_funct.send_text(data["localizacion_destino"])
    print("Teclear input Entger")
    sge_funct.press_enter()
    print("Teclear input 100000")
    sge_funct.send_text(data["cantidad_a_mover"])
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input s")
    sge_funct.send_text('s')
    print("Teclear input Enter")
    sge_funct.press_enter()
    print("Teclear input Enter")
    sge_funct.press_enter()

    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    # ************** QUITAR LA ASIGNACION DE LA LOCALIZACION *******************
    print("Teclear input 8")
    sge_funct.send_text('8')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input 01 ingresar almacen")
    sge_funct.send_text(data["almacen"])
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input 99")
    sge_funct.send_text(data["linea"])
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input CH243")
    sge_funct.send_text(data["codigo"])
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input 1")
    sge_funct.send_text('1')
    print("Teclear input ''")
    sge_funct.clean_field()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    sge_funct.segundos_de_espera(2)
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input 2")
    sge_funct.send_text('2')
    print("Teclear input 002")
    sge_funct.send_text('002')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    # ************** ELIMINACION DE LA LOCALIZACION Y TIPO *******************
    print("Teclear input 14")
    sge_funct.send_text('14')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Tab para buscar por workzone")
    sge_funct.press_tab()
    sge_funct.segundos_de_espera(2)
    print("Teclear input T_WZ_01M")
    sge_funct.escribir_wz_temporal()#
    print("Presionamos ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("Teclear input S")
    sge_funct.send_text('s')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    # ************** ELIMINACION DE WORK ZONE *******************
    print("Teclear input 12")
    sge_funct.send_text('12')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Teclear input 01 ")
    sge_funct.send_text('01 ')# almacen lleva el espacio
    print("Presionamos Tab para buscar por workzone")
    sge_funct.press_tab()
    sge_funct.segundos_de_espera(2)
    print("Teclear input T_WZ_01P")
    sge_funct.escribir_wz_temporal() #
    print("Presionamos ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("Teclear input S")
    sge_funct.send_text('s')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    # ************** ELIMINACION DE ZONA *******************
    print("Teclear input 8")
    sge_funct.send_text('8')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + F")
    sge_funct.press_hotkeys('ctrl+f')
    print("Presionamos C")
    sge_funct.send_text('c')
    print("Presionamos 12")
    sge_funct.send_text('12')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos 01")
    sge_funct.send_text('01')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos 990")# zona de producto depende de donde esta el articulo
    sge_funct.send_text('990')#
    print("Presionamos B")
    sge_funct.send_text('b')
    print("Presionamos S")
    sge_funct.send_text('s')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    print("Presionamos ctrl + A")
    sge_funct.press_hotkeys('ctrl+a')
    #************** ELIMINACION DE DSO *******************
    print("Teclear input 15")
    sge_funct.send_text('15')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos 'TAB'")
    sge_funct.press_tab()
    print("Presionamos Z01") # esta es la DSO
    sge_funct.send_text('Z01') #
    print("Presionamos ctrl + E")
    sge_funct.press_hotkeys('ctrl+e')
    print("Teclear input S")
    sge_funct.send_text('s')
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("Presionamos Enter para continuar Enter")
    sge_funct.press_enter()
    print("SE HA ELIMINADO TODO EXITOSAMENTE :) ")









