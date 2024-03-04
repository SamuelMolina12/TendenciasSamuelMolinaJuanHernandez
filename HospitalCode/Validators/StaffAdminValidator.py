from Validators.TypeValidator import *
import Service.StaffAdminService as staffAdminService

# def processPatient(hospital, id):

#     patient = staffAdminService.validateId(hospital, id)
#     id = int(input("Ingrese el ID del paciente: "))
#     if patient:
#         print("ID válido. Continuar con el proceso.")
        
#     else:
#         print("ID inválido. No se encontró ningún paciente con ese ID.")


def createPatient(hospital):
    id = numberValidator(input("Ingrese la cédula:\n"), "cedula de")
    name = input("Ingrese el nombre de " + str(id) + ":\n")
    textValidator(name, "nombre  " + "\n")
    genre = input("Ingrese el género:\n")
    textValidator(genre, "genero de " + "\n")
    mail = input("Ingrese el correo:\n")
    textValidator(mail, "correo  " + "\n")
    telephone = numberValidator(input("Ingrese el número telefónico:\n"), "telefono" )
    birth = numberValidator(input("Ingrese la fecha de nacimiento:\n"), "fecha de nacimiento" )
    address = input("Ingrese la dirección:\n")
    textValidator(address, "direccion   " + "\n")
    emergency_contact_info={
        'name': input("Ingrese el nombre del contacto de emergencia:\n"),
        'relationship': input("Ingrese la relación con el paciente:\n"),
        'telephone': numberValidator(input("Ingrese el número telefónico del contacto de emergencia:\n"), "telefono del contacto de emergencia")
        }
    policy_info ={
        'insuranceCompany': input("Ingrese el nombre de la compañía de seguros:\n"),
        'policynumber': input("Ingrese el número de póliza:\n"),
        'statePolicy': input("Ingrese el estado de la póliza:\n"),
        'termPolicy': input("Ingrese el término de la póliza:\n")}

    return staffAdminService.createPatient(hospital, id, name, genre, mail, telephone, birth, address, emergency_contact_info, policy_info)


def showPatient(hospital, id):
    patient = staffAdminService.findPatient(hospital, id)
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
def updatePatient(hospital, id):
    patient = staffAdminService.validateId(hospital, id)
    if patient:
        print("Paciente encontrado. Introduzca los nuevos datos:")

        new_name = input("Nuevo nombre: ").strip()
        new_genre = input("Nuevo género: ").strip()
        new_mail = input("Nuevo correo: ").strip()
        new_telephone = input("Nuevo teléfono: ").strip()
        new_birth = input("Nueva fecha de nacimiento: ").strip()
        new_address = input("Nueva dirección: ").strip()
        new_emergency_contact_info = {
            'name': input("Ingrese el nombre del contacto de emergencia: ").strip(),
            'relationship': input("Ingrese la relación con el paciente: ").strip(),
            'telephone': input("Ingrese el número telefónico del contacto de emergencia: ").strip()
        }
        new_policy_info = {
            'insuranceCompany': input("Ingrese el nombre de la compañía de seguros: ").strip(),
            'policynumber': input("Ingrese el número de póliza: ").strip(),
            'statePolicy': input("Ingrese el estado de la póliza: ").strip(),
            'termPolicy': input("Ingrese el término de la póliza: ").strip()
        }
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
        if new_emergency_contact_info:
            patient.emergencyContact = new_emergency_contact_info
        if new_policy_info:
            patient.policy = new_policy_info
        print("Paciente actualizado correctamente.")
    else:
        print("No se encontró ningún paciente con ese ID.")
       