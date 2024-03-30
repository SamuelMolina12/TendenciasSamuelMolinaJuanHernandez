from Validators import DoctorTypeValidator

# def checkPatient(hospital,id):
#     DoctorTypeValidator.checkPatientExistence(hospital)
#     print(id)
#     doctorMenu(hospital,id)


def doctorMenu(hospital,user):
    while True:
        
        option = input("1. Mostrar paciente \n2. Agregar historia clinica  \n3. Mostrar historia clinica  \n4. Cerrar sesion\n")
        if option == "1":
            id = int(input("Ingrese el ID del paciente: "))
            showPatient(hospital,id)
        elif option == "2":
           patientId = int(input("Ingrese el ID del paciente: "))
           createHistoryClinicQuery(hospital,patientId,user)              
        elif option == "3":
           patientId = int(input("Ingrese el ID del paciente: "))
           showHistoryClinicQuery(hospital,patientId)  
        elif option == "4":
            print("Cerrando sesión")
            return
        else:
            print("Opción inválida. Intente de nuevo.")

def showPatient(hospital,id):
    try:
        DoctorTypeValidator.showPatient(hospital,id)
    except Exception as error:
        print(str(error))

def createHistoryClinicQuery(hospital,patientId,user):
    try:
        doctorId = user.id
        DoctorTypeValidator.createHistoryClinicQuery(hospital,patientId,doctorId)
    except Exception as error:
        print(str(error))


def showHistoryClinicQuery(hospital,patientId):
    try:
        DoctorTypeValidator.showHistoryClinicQuery(hospital,patientId)
    except Exception as error:
        print(str(error))

