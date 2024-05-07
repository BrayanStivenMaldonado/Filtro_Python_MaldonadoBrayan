from os import system
import json

def abrirArchivo():
    miJSON=[]
    with open('Datos.json','r',encoding='utf-8') as openfile:
        miJSON = json.load(openfile)  
    return miJSON
  
def guardarArchivo(miData): 
    with open("Datos.json","w",encoding='utf-8') as outfile:
        json.dump(miData,outfile)

#Inicio del programa: 
boolProgramaGeneral = True
while boolProgramaGeneral == True: 

    boolTryCatch = True
    while boolTryCatch == True: 
        try: 
            eleccion = int(input("\n-----MENU PRINCIPAL-----\n1. Administrador \n2. Gestión de Servicios\n3. Reportes\n4. Realizar ventas\n5. Bonificaciones para clientes leales\n\n¿Qué desea hacer?: "))
            system("cls")
            break
        except ValueError:
            input("Debe ingresar un valor numerico, presione ENTER para continuar"),system("cls")
    
    #                                                       MODULO DE ADMINISTRACION
    if eleccion == 1: 
        print("-----ADMINISTRACION-----")
        boolAdministracion = True
        while boolAdministracion == True:
    
            boolTryCatch = True
            while boolTryCatch == True:
                try:
                    eleccionAdmin = int(input("\n1. Ver clientes\n2. Registrar nuevo cliente\n3. Eliminar Cliente\n4. Actualizar Datos Cliente\n5. Salir del módulo de administración\n\nEscoja una opción: "))
                    system("cls")
                    break
                except ValueError:
                    input("Debe ingresar un valor numerico, presione ENTER para continuar")
                    system("cls")
            
            if eleccionAdmin == 1:
                print("----VER CLIENTES----")
                GeneralData = abrirArchivo()
                contador = 0
                for i in GeneralData[0]["Usuarios"]:
                    contador += 1
                    print("Usario #",contador),print("Nombre:",i["Nombre"]),print("Dirección:",i["Direccion"]),print("Contacto:",i["InfoContacto"]),print("Categoria:",i["Categoria"]),print("=====\n")
                input("Presione ENTER para continuar")
                system("cls")

            elif eleccionAdmin == 2:
                print("----REGISTRAR----")
                print("Datos del cliente: ")
                NombreNuevo = input("Nombre Completo: ")
                DireccionNuevo = input("Dirección: ")
                ContactoNuevo = input("Número/correo para contactar: ")
                GeneralData = abrirArchivo()
                GeneralData[0]["Usuarios"].append(
                    {
                        "Nombre" : NombreNuevo,
                        "Direccion" : DireccionNuevo,
                        "InfoContacto" : ContactoNuevo,
                        "Categoria" : "Cliente Nuevo",
                        "ServiciosUsados" : []
                    }
                )
                guardarArchivo(GeneralData)
                input("\nCambios guardados!, Presione Enter para continuar")
                system("cls")
            
            elif eleccionAdmin == 3: 
                print("----ELIMINAR----")
                GeneralData = abrirArchivo()
                contador = 0
                for i in GeneralData[0]["Usuarios"]:
                    contador+=1
                    print("Usario #",contador),print("Nombre:",i["Nombre"]),print("Dirección:",i["Direccion"]),print("Contacto:",i["InfoContacto"]),print("Categoria:",i["Categoria"]),print("=====\n")
                UsuarioEliminar = int(input("\n¿Qué usuario desea eliminar?: "))

                del GeneralData[0]["Usuarios"][UsuarioEliminar-1]
                guardarArchivo(GeneralData)
                input("\nUsuario Eliminado!, Presione ENTER para continuar")
                system("cls")

            elif eleccionAdmin == 4:
                print("----ACTUALIZAR----\n")
                contador = 0
                GeneralData = abrirArchivo()
                for i in GeneralData[0]["Usuarios"]:
                    contador+=1
                    print("Usario #",contador),print("Nombre:",i["Nombre"]),print("Dirección:",i["Direccion"]),print("Contacto:",i["InfoContacto"]),print("Categoria:",i["Categoria"]),print("")
                UsuarioActualizar = int(input("\n¿Qué usuario desea actualizar?: "))
                system("cls")
                DatoActualizar = int(input("\n1. Nombre \n2. Dirección \n3. Info de Contacto\n\n¿Qué dato desea actualizar?: "))
                if DatoActualizar == 1:
                    print("----ACTUALIZAR NOMBRE----")
                    GeneralData = abrirArchivo()
                    NombreActualizar = input("Ingrese el nuevo nombre del cliente: ")
                    GeneralData[0]["Usuarios"][UsuarioActualizar-1]["Nombre"] = NombreActualizar

                elif DatoActualizar == 2:
                    print("----ACTUALIZAR DIRECCION----")
                    GeneralData = abrirArchivo()
                    DireccionActualizar = input("Ingrese la nueva dirección del cliente: ")
                    GeneralData[0]["Usuarios"][UsuarioActualizar-1]["Direccion"] = DireccionActualizar

                elif DatoActualizar == 3:
                    print("----ACTUALIZAR INFO DE CONTACTO----")
                    GeneralData = abrirArchivo()
                    NombreActualizar = input("Ingrese el nuevo número/correo de contacto del cliente: ")
                    GeneralData[0]["Usuarios"][UsuarioActualizar-1]["InfoContacto"] = NombreActualizar
                
                elif eleccionAdmin == 5:
                    input("Saliendo del módulo de coordinación, presione ENTER para continuar")
                    boolAdministracion = False

                else:
                    input("Esta no es una opción válida, presione ENTER para continuar")
                    system("cls")

                guardarArchivo(GeneralData)
                input("\nDatos Cambiados!, Presione ENTER para continuar")
                system("cls")

            elif eleccionAdmin == 5:
                input("Saliendo del modulo de administración, presione ENTER para continuar"), system("cls")
                boolAdministracion = False

            else:
                print("Esta no es una opción válida, presione ENTER para continuar"),system("cls")

            
    #                                                         GESTION DE SERVICIOS
    elif eleccion == 2: 
        print("-----GESTION DE SERVICIOS-----")
        boolServicios = True
        while boolServicios == True:
            boolTryCatch = True
            while boolTryCatch == True:
                try:
                    eleccionSer = int(input("\n1. Ver servicios disponibles\n2. Crear un nuevo servicio\n3. Eliminar servicio\n4. Modificar Servicio\n5. Salir del módulo de gestión de servicios\n\nEscoja una opción: "))
                    system("cls")
                    break
                except ValueError:
                    input("Debe ingresar un valor numerico, presione ENTER para continuar")
                    system("cls")
        
            if eleccionSer == 1:
                print("----VER SERVICIOS----")
                GeneralData = abrirArchivo()
                contador = 0
                for i in GeneralData[1]["Servicios"]:
                    contador += 1
                    print("Servicio #",contador),print("Nombre:",i["Servicio"][0]["Nombre"]),print("Descripción:",i["Servicio"][0]["Descripcion"]),print("precio:",i["Servicio"][0]["Precio"]),print("")
                input("\nPresione ENTER para continuar"),system("cls")

            elif eleccionSer == 2:
                print("----CREAR SERVICIO----\n")
                NombreSerNuevo = input("Ingrese el nombre del servicio que desea crear: ")
                DescripSerNuevo = input("Ingrese una breve descripción del nuevo servicio: ")
                PrecioSerNuevo = int(input("Ingrese el valor del servicio: "))
                GeneralData = abrirArchivo()
                GeneralData[1]["Servicios"].append({
                    "Servicio" : [
                        {
                            "Nombre": NombreSerNuevo,
                            "Descripcion": DescripSerNuevo,
                            "Precio": PrecioSerNuevo
                        }
                    ]
                }      
                )
                guardarArchivo(GeneralData)
                input("\nCambios guardados!, Presione ENTER para continuar"),system("cls")

            elif eleccionSer == 3:
                print("----ELIMINAR SERVICIO----")
                GeneralData = abrirArchivo()
                contador = 0
                for i in GeneralData[1]["Servicios"]:
                    contador += 1
                    print("Servicio #",contador),print("Nombre:",i["Servicio"][0]["Nombre"]),print("Descripción:",i["Servicio"][0]["Descripcion"]),print("precio:",i["Servicio"][0]["Precio"]),print("")
                ServicioEliminar = int(input("¿Qué servicio desea eliminar?: "))
                system("cls")
                del GeneralData[1]["Servicios"][ServicioEliminar-1]
                guardarArchivo(GeneralData)
                input("\nServicio eliminado!, presione ENTER para continuar"),system("cls")
            
            elif eleccionSer == 4:
                print("----MODIFICAR SERVICIO----")
                GeneralData = abrirArchivo()
                contador = 0
                for i in GeneralData[1]["Servicios"]:
                    contador += 1
                    print("Servicio #",contador),print("Nombre:",i["Servicio"][0]["Nombre"]),print("Descripción:",i["Servicio"][0]["Descripcion"]),print("precio:",i["Servicio"][0]["Precio"]),print("")
                ModificarSer = int(input("¿Qué servicio desea modificar?: "))
                DatoParaModificarSer = int(input("\n1. Nombre del servicio\n2. Descripción del servicio\n3. Precio del servicio\n\n¿Qué dato del servicio desea editar?: "))
               
                if DatoParaModificarSer == 1:
                    print("----MODIFICAR NOMBRE DEL SERVICIO----")
                    NuevoNombreSer = input("Ingrese el nuevo nombre del servicio: ")
                    GeneralData[1]["Servicios"][ModificarSer-1]["Servicio"][0]["Nombre"] = NuevoNombreSer
                
                elif DatoParaModificarSer == 2:
                    print("----MODIFICAR DESCRIPCION DEL SERVICIO----")
                    NuevaDecrSer = input("Ingrese la nueva descripción del servicio: ")
                    GeneralData[1]["Servicios"][ModificarSer-1]["Servicio"]["Descripcion"] = NuevaDecrSer
                
                elif DatoParaModificarSer == 3:
                    print("----MODIFICAR PRECIO SERVICIO----")
                    nuevoPrecioSer = int(input("Ingrese el nuevo precio del servicio: "))
                    GeneralData[1]["Servicios"][ModificarSer-1]["Servicio"]["Precio"] = nuevoPrecioSer

                guardarArchivo(GeneralData)
                input("Cambios guardados!, Presione ENTER para continuar"),system("cls")
            
            elif eleccionSer == 5:
                input("Saliendo del módulo de Servicios, presione ENTER para continuar"),system("cls")
                boolServicios = False
            
            else:
                input("Esta no es una opción válida, presione ENTER para continuar"),system("cls")            

                                                            
    elif eleccion == 3: 
        print("-----REPORTES-----")
    #                                                               VENTAS
    elif eleccion == 4: 
        boolVentas = True
        while boolVentas == True: 
            print("----REALIZAR VENTAS-----")
            print("\n----CLIENTES DENTRO DEL SISTEMA----")
            GeneralData = abrirArchivo()
            contador = 0
            for i in GeneralData[0]["Usuarios"]:
                contador+=1
                print("Usario #",contador),print("Nombre:",i["Nombre"]),print("Dirección:",i["Direccion"]),print("Contacto:",i["InfoContacto"]),print("Categoria:",i["Categoria"]),print("=====\n")
            ClienteParaVenta = int(input("¿A qué cliente desea venderle el servicio?: "))
            system("cls")
            print("\n----SERVICIOS DISPONIBLES----")
            GeneralData = abrirArchivo()
            contador = 0
            for i in GeneralData[1]["Servicios"]:
                contador += 1
                print("Servicio #",contador),print("Nombre:",i["Servicio"][0]["Nombre"]),print("Descripción:",i["Servicio"][0]["Descripcion"]),print("precio:",i["Servicio"][0]["Precio"]),print("")
            ServicioParaVenta = int(input("¿Qué servicio le va a vender?: "))
            system("cls")
            GeneralData[0]["Usuarios"][ClienteParaVenta-1]["ServiciosUsados"].append(GeneralData[1]["Servicios"][ServicioParaVenta-1]["Servicio"][0]["Nombre"])
            guardarArchivo(GeneralData)
            boolChepe = True
            while boolChepe == True:
                seguirNoSeguir = input("Cambios guardados!, ¿Desea realizar otra venta? si/no")
                if seguirNoSeguir == "no":
                    boolVentas = False
                    boolChepe = False
                elif seguirNoSeguir == "si":
                    boolChepe = False
                else:
                    input("Esta no es una opción válida, presione ENTER para volver a intentar")
                    system("cls")

    
    elif eleccion == 5: 
        print("----BONIFICACIONES-----")
    
    else: 
        input("Esta no es una opción válida, presione ENTER para continuar"),system("cls")
        
# Desarrollado por Brayan Maldonado - Camper - TI 1.090.404.470