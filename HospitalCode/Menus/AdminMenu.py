from Validators import PersonTypeValidator


def adminMenu(hospital,user):
    while True:
        option=input("1.Gestionar administrador \n2.Gestionar doctor \n3.Gestionar enfermera \n4.Gestionar personal de soporte de informacion\n5.Cerrar sesion\n")
        if option=="1":
            manageAdmin(hospital)
        if option=="2":
            manageDoctor(hospital)
        if option == "3":
            manageNurse(hospital)
        if option =="4":
            manageAdminStaff(hospital)
        if option == "5":
            print("cerrando sesion")
            return           
        

def manageAdmin(hospital):
    while True:
        option=input("1.Crear administrador \n2.Editar administrador\n3.Eliminar administrador \n4.Mostrar administradores \n5.Cancelar\n")
        if option=="1":
           createUser(hospital,"admin")
        if option=="2":
           updateUser (hospital,id)
        if option == "3":
           deleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"admin")
        if option == "5":
          
            return           
        
            
def manageDoctor(hospital):
     while True:
        option=input("1.Crear doctor \n2.Editar doctor\n3.Eliminar doctor \n4.Mostrar doctores \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"doctor")
        if option=="2":
            updateUser (hospital,id)
        if option == "3":
           deleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"doctor")
        if option == "5":
          
            return  
        

def manageNurse(hospital):
     while True:
        option=input("1.Crear enfermera \n2.Editar enfermera \n3.Eliminar enfermera \n4.Mostrar enfermera \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"enfermera")
        if option=="2":
         print("2")
        if option == "3":
           deleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"enfermera")
        if option == "5":
          
            return  
        
def manageAdminStaff(hospital):
     while True:
        option=input("1.Crear PersonalAdministrativo \n2.Editar PersonalAdministrativo \n3.Eliminar PersonalAdministrativo \n4.Mostrar PersonalAdministrativo \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"PersonalAdministrativo")
        if option=="2":
           updateUser (hospital,id)
        if option == "3":
           deleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"PersonalAdministrativo")
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