from Validators import StaffAdminValidator


def staffAdminMenu(hospital):
    while True:
        option=input("1.Crear Paciente  \n2.Gestionar Paciente \n3.Cerrar sesion\n")
        if option=="1":
            createPacient(hospital)
        if option=="2":
            id=input("ingrese el id del paicente \n")
            managePacient(hospital,int(id))
        if option == "3":
            print("cerrando sesion")
            return       

def createPacient(hospital): 
    try:
        patien=StaffAdminValidator.createPatient(hospital)
        print("se ha creado el paciente  con cedula" + str(patien.id) )
    except Exception as error:
        print(str(error))

def managePacient(hospital,id):
    while True:
        option=input("1.Mostrar informacion del  Paciente \n2.Editar Paciente  \n3.Eliminar Paciente \n4.Agendar Cita \n5.Facturacion  \n6.Cerrar sesion\n")
        if option=="1":
            showPatient(hospital,id)
        if option=="2":
           pass
        if option=="3":
            pass
        if option=="4":
           pass
        if option=="5":
            pass
        if option == "6":
            print("cerrando sesion")
            return 


def showPatient(hospital,id):
    try:
        StaffAdminValidator.showPatient(hospital,id)
    except Exception as error:
        print(str(error))