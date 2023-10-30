from Config.config import images
from Sge_functions.sge_functions2 import sge_functions2

def MTC_SURSGE_015_steps(sge_funct, data):
    sge_funct.segundos_de_espera(1)
    sge_funct.activar_cambio_usuario()
    print("3 Teclear el nombre del usuario")
    sge_funct.send_text('sfabian0')
    print("4 Teclear input")
    sge_funct.press_enter()
    print("5 Ingresar en el teclado el <<Numero de sucursal>>")
    sge_funct.send_text(data["sucursal"])
    sge_funct.segundos_de_espera(1)
    sge_funct.validar_sucursal_12_seleccionada()
    print("6 Teclear input")
    sge_funct.press_enter()
    print("7 Teclear input")
    sge_funct.send_text('2')
    print("8 Teclear input")
    sge_funct.press_enter()
    print("9 Teclear input")
    sge_funct.send_text('9')
    print("10 Teclear input")
    sge_funct.press_enter()
    print("11 Capturar la opcion 13 Abastecimiento y Relleno")
    sge_funct.send_text('13')
    print("12 Teclear input")
    sge_funct.press_enter()
    print("13 Capturar c para consultar")
    sge_funct.send_text('c')
    print("14 Leer archivo permanente_a_multiple.json para capturar la clave del almacen")
    sge_funct.send_text(data["almacen"])
    print("15 Teclear input")
    sge_funct.press_enter()
    print("16 Leer archivo permanente_a_multiple.json para capturar la linea del producto")
    sge_funct.send_text(data["linea"])
    print("17 Teclear input")
    sge_funct.press_enter()
    print("18 Leer archivo permanente_a_multiple.json para capturar el codigo del producto")
    sge_funct.send_text(data["codigo"])
    print("19 Teclear input")
    sge_funct.press_enter()
    print("20 Capturar m para modificar")
    sge_funct.send_text('m')
    print("21 Presionar la combinacion de teclas: Ctrl + d para ver los detalles")
    sge_funct.press_hotkeys('ctrl+d')
    print("22 Leer archivo permanente_a_multiple.json para capturar la localizacion destino")
    sge_funct.send_text(data["localizacion_destino"])
    print("23 Teclear input")
    sge_funct.press_enter()
    print("24 Leer archivo permanente_a_multiple.json para capturar la cantidad a mover")
    sge_funct.send_text(data["cantidad_a_mover"])
    print("25 Teclear input")
    sge_funct.press_enter()
    print("26 Capturar s para continuar")
    sge_funct.send_text('s')
    print("24 Teclear input")
    sge_funct.press_enter()










