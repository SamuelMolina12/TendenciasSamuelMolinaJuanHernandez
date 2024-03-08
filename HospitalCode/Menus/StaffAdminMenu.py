from Validators import StaffAdminValidator


def staffAdminMenu(hospital):
    while True:
        option=input("1.Crear Paciente  \n2.Gestionar Paciente \n3.Cerrar sesion\n")
        if option=="1":
            createPatient(hospital)
        if option=="2":
            id=input("ingrese el id del paciente \n")
            managePatient(hospital,int(id))
        if option == "3":
            print("cerrando sesion")
            return       

def createPatient(hospital): 
    try:
        StaffAdminValidator.createPatient(hospital)
        print("se ha creado el paciente")
    except Exception as error:
        print(str(error))

def managePatient(hospital,id):
    while True:
        option=input("1.Mostrar informacion del  Paciente \n2.Editar Paciente  \n3.Eliminar Paciente \n4.Agendar Cita \n5.ver citas programadas \n6.Facturacion  \n7.Cancelar\n")
        if option=="1":
            showPatient(hospital,id)
        if option=="2":
           updatePatient(hospital,id)
        if option=="3":
            deletePatient(hospital, id)
            return 
        if option=="4":
           createClinicalAppointment(hospital,id)
        if option=="5":
           showClinicalAppointment(hospital,id)
        if option=="6":
            pass
        if option == "7":
            print("cerrando sesion")
            return 


def showPatient(hospital,id):
    try:
        StaffAdminValidator.showPatient(hospital,id)
    except Exception as error:
        print(str(error))

def deletePatient(hospital, id):
    try:     
        StaffAdminValidator.deletePatient(hospital,id)
       
    except Exception as error:
        print(str(error))


def updatePatient(hospital,id):
    try:
        StaffAdminValidator.updatePatient(hospital, id)
    except Exception as error:
        print(str(error))

def createClinicalAppointment(hospital,id):
    try:
        StaffAdminValidator.createClinicalAppointment(hospital, id)
    except Exception as error:
        print(str(error))

def showClinicalAppointment(hospital,id):
    try:
        StaffAdminValidator.showClinicalAppointment(hospital, id)
    except Exception as error:
        print(str(error))