from Validators import personTypeValidator


def adminMenu(hospital,user):
    while True:
        option=input("1.Gestionar administrador \n2.Gestionar doctor \n3.Gestionar enfermera \n4.Gestionar personal de soporte de informacion\n5.Cerrar sesion\n")
        if option=="1":
            ManageAdmin(hospital)
        if option=="2":
            ManageDoctor(hospital)
        if option == "3":
            ManageNurse(hospital)
        if option =="4":
            ManageSupport(hospital)
        if option == "5":
            print("cerrando sesion")
            return           
        

def ManageAdmin(hospital):
    while True:
        option=input("1.Crear administrador \n2.Editar administrador\n3.Eliminar administrador \n4.Mostrar administradores \n5.Cancelar\n")
        if option=="1":
           createUser(hospital,"admin")
        if option=="2":
           pass
        if option == "3":
           DeleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"admin")
        if option == "5":
          
            return           
        
            
def ManageDoctor(hospital):
     while True:
        option=input("1.Crear doctor \n2.Editar doctor\n3.Eliminar doctor \n4.Mostrar doctores \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"doctor")
        if option=="2":
         print("2")
        if option == "3":
           DeleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"doctor")
        if option == "5":
          
            return  
        

def ManageNurse(hospital):
     while True:
        option=input("1.Crear enfermera \n2.Editar enfermera \n3.Eliminar enfermera \n4.Mostrar enfermera \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"enfermera")
        if option=="2":
         print("2")
        if option == "3":
           DeleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"enfermera")
        if option == "5":
          
            return  
        
def ManageSupport(hospital):
     while True:
        option=input("1.Crear soporte \n2.Editar soporte \n3.Eliminar soporte \n4.Mostrar soporte \n5.Cancelar\n")
        if option=="1":
            createUser(hospital,"soporte")
        if option=="2":
         print("2")
        if option == "3":
           DeleteUser(hospital, id)
        if option == "4":
          showUser(hospital,"soporte")
        if option == "5":
          
            return  
        

def createUser(hospital,role):
    try:
        personTypeValidator.createUser(hospital,role)
        print("se ha creado el " + role)
    except Exception as error:
        print(str(error))

def showUser(hospital,role):
    try:
        personTypeValidator.ShowUsers(hospital,role)
    except Exception as error:
        print(str(error))

def DeleteUser(hospital, id):
    id = input("Ingrese la identificación del usuario que desea eliminar: ")
    personTypeValidator.DeleteUser(hospital,id)