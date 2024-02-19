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
        option=input("1.Crear administrador \n2. Editar administrador\n3. Eliminar administrador \n4. Cancelar\n" )
        if option=="1":
           createAdmin(hospital)
        if option=="2":
         print("2")
        if option == "3":
           print("3")
      
        if option == "4":
            print("cerrando sesion")
            return           
        
    
    
def ManageDoctor(hospital):
    pass
def ManageNurse(hospital):
    pass
def ManageSupport(hospiatal):
    pass

def createAdmin(hospital):
    try:
        personTypeValidator.createAdmin(hospital,"administrador")
        print("se ha creado el administrador")
    except Exception as error:
        print(str(error))
