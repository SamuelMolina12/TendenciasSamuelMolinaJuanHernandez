from Validators import PersonTypeValidator


def humanRMenu(hospital):
    while True:
        option=input("1.Gestionar Recursos Humanos \n2.Gestionar doctor \n3.Gestionar enfermera \n4.Gestionar administrador \n5.Gestionar personal de soporte de informacion \n6.Cerrar sesion\n")
        if option=="1":
            manage(hospital,"RecursosHumanos")
        if option=="2":
            manage(hospital,"doctor")
        if option == "3":
            manage(hospital,"enfermera")
        if option =="4":
            manage(hospital,"administrador")
        if option =="5":
            manage(hospital,"Soporte")    
        if option == "6":
            print("cerrando sesion")
            return           
        

def manage(hospital,role):
    while True:
        option=input("1.Crear "+ role +" \n2.Editar "+ role +"\n3.Eliminar "+ role +" \n4.Mostrar "+ role +" \n5.Cancelar\n")
        if option=="1":
           createUser(hospital,role)
        if option=="2":
           updateUser (hospital,id)
        if option == "3":
           deleteUser(hospital, id)
        if option == "4":
          showUser(hospital,role)
        if option == "5":
          
            return           
        

def createUser(hospital,role):
    try:
        PersonTypeValidator.createUser(hospital,role)
        print("se ha creado el " + role)
    except Exception as error:
        print(str(error))

def showUser(hospital,role):
    try:
        PersonTypeValidator.showUsers(hospital,role)
    except Exception as error:
        print(str(error))

def deleteUser(hospital, id):
    try:
        id = input("Ingrese la identificación del usuario que desea eliminar: ")
        PersonTypeValidator.deleteUser(hospital, id)
    except Exception as error:
        print(str(error))

def updateUser(hospital,id):
    try:
        id = input("Ingrese la identificación del usuario que desea actualizar: ")
        PersonTypeValidator.updateUser(hospital, id)
    except Exception as error:
        print(str(error))