from Validators.TypeValidator import *
import Service.StaffAdminService as staffAdminService



def createPatient(hospital):
    id = numberValidator(input("Ingrese la cédula:\n"), "cedula de")
    name = input("Ingrese el nombre :\n")
    textValidator(name, "nombre  \n")
    genre = input("Ingrese el género:\n")
    textValidator(genre, "genero de\n")
    mail = input("Ingrese el correo:\n")
    textValidator(mail, "correo  \n")
    telephone = numberValidator(input("Ingrese el número telefónico:\n"), "telefono" )
    birth = numberValidator(input("Ingrese la fecha de nacimiento:\n"), "fecha de nacimiento" )
    address = input("Ingrese la dirección:\n")
    textValidator(address, "direccion  \n")
    staffAdminService.createPatient(hospital, id, name, genre, mail, telephone, birth, address)
    print("Contacto de emergencia")
    createEmergencyContact(hospital,id)
    print("Póliza")
    createPolicy(hospital,id)
   

    

def createEmergencyContact(hospital,patientId):
    name = input("Ingrese el nombre del contacto de emergencia del paciente: \n") 
    textValidator(name,"Nombre del contacto de emergencia del paciente")
    relationship = input("Ingrese la relacion del contacto de emergencia:\n")
    textValidator(relationship,"Relacion del contacto de emergencia")
    telephone = numberValidator(input("Ingrese el numero de telefono: \n"), "Numero del contacto de emergencia")
    staffAdminService.createEmergencyContact(hospital,patientId,name,relationship,telephone)

def createPolicy(hospital,patientId):
    insuranceCompany = input("Ingrese el nombre de la compañia: \n")
    textValidator(insuranceCompany, "nombre de la compañia \n")
    policynumber = numberValidator(input("Ingrese el numero de poliza: \n"), "Numero de poliza")
    statePolicy = input("Ingrese el estado de la poliza: \n")
    textValidator(statePolicy, "estado de la poliza \n")
    termPolicy = input("Ingrese la fecha de terminacion de la poliza: \n")
    textValidator(termPolicy, "fecha de \n")
    staffAdminService.createPolicy(hospital,patientId,insuranceCompany,policynumber,statePolicy,termPolicy)

def showPatient(hospital, id):
    patient = staffAdminService.validateId(hospital, id)
    if patient:
        print(f"Cedula: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Genero: {patient.genre}")
        print(f"Email: {patient.mail}")
        print(f"Telefono: {patient.telephone}")
        print(f"Fecha de nacimiento: {patient.birth}")
        print(f"Direccion: {patient.address}")
        if patient.emergencyContact:
            print("Contacto de Emergencia:")
            print(f"Nombre: {patient.emergencyContact.name}")
            print(f"Relación: {patient.emergencyContact.relationship}")
            print(f"Teléfono: {patient.emergencyContact.telephone}")                  
        if patient.policy:
            print("Poliza:")
            print(f"Compañía de Seguros: {patient.policy.insuaranceCompany}")
            print(f"Número de Póliza: {patient.policy.policynumber}")
            print(f"Estado de la Póliza: {patient.policy.statePolicy}")
            print(f"Término de la Póliza: {patient.policy.termPolicy}")         
        print()
    else:
        print("Paciente no encontrado.")


def deletePatient(hospital,id):
    id = int(id)
    if staffAdminService.deletePatient(hospital, id):
         deletePatient2(hospital, id)
    else:
        print("No se encontró ningún usuario con esa identificación.")

def deletePatient2(hospital, id):
    for i, user in enumerate(hospital.patient):
        if user.id == id:
            del hospital.patient[i]
            print("Usuario eliminado exitosamente.")
            return
def updatePatient(hospital,id):
    patient = staffAdminService.validateId(hospital,id)
    if patient:
        print("Paciente encontrado. Introduzca los nuevos datos:")

        new_name = input("Nuevo nombre: ")
        new_genre = input("Nuevo género: ")
        new_mail = input("Nuevo correo: ")
        new_telephone = int(input("Nuevo teléfono: "))
        new_birth = int(input("Nueva fecha de nacimiento: "))
        new_address = input("Nueva dirección: ")
        updateEmergencyContact(patient)
        updatePolicy(patient)
        if new_name:
            patient.name = new_name
        if new_genre:
            patient.genre = new_genre
        if new_mail:
            patient.mail = new_mail
        if new_telephone:
            patient.telephone = new_telephone
        if new_birth:
            patient.birth = new_birth
        if new_address:
            patient.address = new_address
        print("Paciente actualizado correctamente.")
    else:
        print("No se encontró ningún paciente con ese ID.")

def updateEmergencyContact(patient):
    new_name = input("Nuevo nombre de contacto de emergencia: ")
    new_relationship = input("Nueva relación con el paciente: ")
    new_telephone = input("Nuevo teléfono del contacto de emergencia: ")
    
    if new_name:
        patient.emergencyContact.name = new_name
    if new_relationship:
        patient.emergencyContact.relationship = new_relationship
    if new_telephone:
        patient.emergencyContact.telephone = new_telephone

def updatePolicy(patient):
    new_insuranceCompany = input("Nuevo nombre del la compañia: ")
    new_policynumber = input("Nuevo numero de poliza: ")
    new_statePolicy = input("Nuevo estado de la poliza: ")
    new_termPolicy = input("Nueva fecha de termino de poliza: ")

    if new_insuranceCompany :
        patient.policy.insuranceCompany = new_insuranceCompany 
    if new_policynumber:
        patient.policy.policynumber = new_policynumber
    if new_statePolicy:
        patient.policy.statePolicy =  new_statePolicy
    if  new_termPolicy:
        patient.policy.termPolicy =  new_termPolicy
        