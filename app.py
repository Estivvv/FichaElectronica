import clase
import interfaz
from basedato import Basedato as bd
import os
import time


def main():
    print(" Código Enigma V1.0")
    print("....presionar para continuar")
    while True:
        contador = 0
        while True:
            input()
            datosLogin =clase.encriptacion().login(input("ingrese Rut sin digito verificador:  "),input("Ingrese Contraseña  "))
        
            if interfaz.api().sesion(datosLogin[0],datosLogin[1])[0] == 200 :
                print("Comprobación por API exitosa\n")
                break
            else:
                print("Error en la comprobación por API , intente nuevamente")
                contador = contador + 1
                print("Intentos restantes: ",3-contador)
                if contador ==3:
                    print("Superó el numero de intentos....Cerrando programa")
                    time.sleep(2)
                    exit()
                
            
        print("Buscando Usuario en Base de datos....\n")
        query = "SELECT Rut,Nombre,pApellido FROM usuario WHERE Rut={}".format(datosLogin[0])
        resultado = bd()._select(query,())
        if  resultado == []:
            print("Usuario no encontrado")
            print("Iniciando proceso de registro....")
            time.sleep(2)
            print("Ingresar datos para registrar")
            nombre = input("Ingrese su nombre: ")
            pApellido = input("Ingrese su primer apellido: ")
            sApellido = input("Ingrese su segundo apellido: ")  
            parametros = (datosLogin[0],datosLogin[1],nombre,pApellido,sApellido,0)
            query = "INSERT INTO usuario (Rut,Contraseña,Nombre,pApellido,sApellido,intentos_con) VALUES (%s,%s,%s,%s,%s,%s)"
            try:
                bd()._transacciones(query,parametros)
                print("Registro exitoso!\n")
                os.system('cls')
            except:
                print("Registro Fallido....Vuelva a intentar")
                input() 
                break  
        else:
            print("Usuario encontrado.\n Ingresando...")
            time.sleep(5)
            os.system('cls')
        while True:
            os.system('cls')
            print("-"*40)
            print("   MODULOS  ")
            print("-"*40)
            
            Lista = interfaz.api().enc()
            C = clase.encriptacion()
            C.desencriptar(Lista)
            Lista_desencript=C.llamar()
        
            a = input("1) DESENCRIPTAR\n2) HISTORIAL\n3) SALIR\n" )

            if a == "1":
                print("-"*40)
                print("   CLAVES      ")
                print("-"*40)
            
                

                print("Claves Encriptadas recibidas durante la sesión actual")
                
                for i in range(0,3):
                    print(str(i+1)+ ")  " + Lista[i])
                
                print("\nClaves Encriptadas con su valor real correspondiente\n")
                
                for i in range(0,3):
                    print("-"*40)
                    print("Clave N°", Lista[i],"    Clave Real: ",Lista_desencript[i])
                
                print("\n")
                query2 = "INSERT INTO sesion (Rut,Hash_login,Hash1,UnHash1,Hash2,UnHash2,Hash3,UnHash3,Fecha) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,NOW())"
                parametros = (datosLogin[0],interfaz.api().sesion(datosLogin[0],datosLogin[1])[1],Lista[0],Lista_desencript[0],Lista[1],Lista_desencript[1],Lista[2],Lista_desencript[2])

                try:
                    bd()._transacciones(query2,parametros)
                except:
                    print("Error de subida de datos")
                    break
                
                if input("\n1) Volver al menu\n2) Salir ")=="1":
                    continue
                else:
                    exit()
       
            if a == "2":    
                
                try:
                    query3 ="SELECT *,DAY(FECHA),MONTH(FECHA) FROM sesion JOIN usuario ON sesion.Rut = usuario.Rut"
                
                    q3 = bd()._select(query3,())
                    print("-"*40)
                    print("   HISTORIAL DE DESENCRIPTACIONES  ")
                    if q3 ==[]:
                        print(" SIN REGISTROS")

                    for i in q3:
                        print("-"*40)
                        print("Usuario {} {} | Fecha {}-{}".format(i[12],i[13],i[16],i[17]))
                        print("Clave :{} | Valor Real: {}".format(i[3],i[4]))
                        print("Clave :{} | Valor Real: {}".format(i[5],i[6]))
                        print("Clave :{} | Valor Real: {}".format(i[7],i[8]))
                except IndexError:
                    print("SIN REGISTROS")

                if input("\n1) Volver al menu\n2) Salir\n")=="1":
                    continue
                else:
                    exit()

            if a == "3":
                exit()



        
    

if __name__ == "__main__":

    main()