from Validators.TypeValidator import *
import Service.StaffAdminService as staffAdminService


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

        # Información del contacto de emergencia
    emergency_contact_info={
        'name': input("Ingrese el nombre del contacto de emergencia:\n"),
        'relationship': input("Ingrese la relación con el paciente:\n"),
        'telephone': numberValidator(input("Ingrese el número telefónico del contacto de emergencia:\n"), "telefono del contacto de emergencia")
        }

        # Información de la póliza
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


