from Validators.TypeValidator import *
import Service.StaffAdminService as staffAdminService



def createPatient(hospital):
    id = numberValidator(input("Ingrese la cédula:\n"), "cedula de")
    name = input("Ingrese el nombre :\n")
    textValidator(name, "nombre  \n")
    genre = input("Ingrese el género: masculino o femenino\n")
    textValidator(genre, "genero de\n")
    genreValidator(genre, "genero de\n")
    mail = input("Ingrese el correo:\n")
    textValidator(mail, "correo  \n")
    emailValidator(mail,"correo \n")
    telephone = phoneValidator(input("ingrese el numero telefonico " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
    birth = dateValidator(input("ingrese la fecha de nacimiento " + "Formato DD/MM/YYYY, max 150 años\n"),"fecha de nacimiento de")
    address = input("ingrese la direccion " + "Máximo 30 caracteres  \n")
    textValidator(address, "direccion de    \n")
    addressValidator(address, "direccion de  \n")
    staffAdminService.createPatient(hospital, id, name, genre, mail, telephone, birth, address)
    print("Contacto de emergencia")
    createEmergencyContact(hospital,id)
    print("Póliza")
    createPolicy(hospital,id)
    print("Paciente creado con exito")

    

def createEmergencyContact(hospital,patientId):
    name = input("Ingrese el nombre del contacto de emergencia del paciente: \n") 
    textValidator(name,"Nombre del paciente")
    relationship = input("Ingrese la relacion del contacto de emergencia:\n")
    textValidator(relationship,"Relacion del contacto de emergencia")
    telephone = phoneValidator(input("ingrese el numero de contacto de emergencia " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
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

        new_name = input("ingrese el nuevo nombre \n")
        textValidator(new_name,"el nuevo nombre \n")
        new_genre = input("ingrese el nuevo genero \n")
        textValidator(new_genre, "nuevo genero\n")
        genreValidator(new_genre, "nuevo genero: masculino o femenino\n")
        new_mail = input("ingrese el nuevo correo " + " dominio y el @ \n")
        textValidator(new_mail, "correo  \n")
        emailValidator( new_mail,"correo \n")
        new_telephone = input("Nuevo telefono: " + "Debe contener entre 1 y 10 dígitos") 
        phoneValidator(new_telephone, "nuevo numero de telefono\n")
        new_birth = input("nueva fecha de nacimiento: " + "Formato DD/MM/YYYY")
        dateValidator(new_birth, "nuevo fecha de nacimiento\n")
        new_address = input("ingrese la nueva direccion " + "Máximo 30 caracteres\n")
        textValidator(new_address, "direccion  \n")
        addressValidator(new_address, "direccion \n")
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
    textValidator(new_name,"el nuevo nombre \n")
    new_relationship = input("Nueva relación con el paciente: ")
    textValidator(new_relationship,"nueva relacion con el paciente \n")
    new_telephone = input("Nuevo telefono de contacto de emergencia: " + "Debe contener entre 1 y 10 dígitos") 
    phoneValidator(new_telephone, "nuevo numero de telefono\n")
    
    if new_name:
        patient.emergencyContact.name = new_name
    if new_relationship:
        patient.emergencyContact.relationship = new_relationship
    if new_telephone:
        patient.emergencyContact.telephone = new_telephone

def updatePolicy(patient):
    new_insuranceCompany = input("Nuevo nombre del la compañia: ")
    textValidator(new_insuranceCompany,"el nuevo nombre \n")
    new_policynumber = input("Nuevo numero de poliza: ")
    numberValidator(new_policynumber," nuevo numero de poliza \n")
    new_statePolicy = input("Nuevo estado de la poliza: ")
    textValidator(new_statePolicy,"nuevo estado de la poliza \n")
    new_termPolicy = input("Nueva fecha de termino de poliza: ")
    textValidator(new_termPolicy,"nueva fecha de finalizacion de poliza \n")

    if new_insuranceCompany :
        patient.policy.insuranceCompany = new_insuranceCompany 
    if new_policynumber:
        patient.policy.policynumber = new_policynumber
    if new_statePolicy:
        patient.policy.statePolicy =  new_statePolicy
    if  new_termPolicy:
        patient.policy.termPolicy =  new_termPolicy


def createClinicalAppointment(hospital,id):
    patientId = id
    date= input("Ingrese la fecha de la cita:\n")
    textValidator(date, "fecha  \n")
    hour = input("ingrese la hora de la cita\n")
    textValidator(hour, "hora de\n")
    doctor = input("Ingrese el nombre del doctor al que se le asignara la cita:\n")
    textValidator(doctor, "correo  \n")
    appointmentType = input("ingrese el tipo de cita\n")
    textValidator(appointmentType, "direccion de\n")
    staffAdminService.createClinicalAppointment(hospital,patientId,date,hour, doctor,appointmentType)
    print("Cita medica creada con exito")

def showClinicalAppointment(hospital,id):
    patientId = id
    appointment = staffAdminService.validateClinicalAppointment(hospital,patientId)
    if appointment:
       for appointment in hospital.clinicalAppointment:
            print(f"Cedula Paciente: {appointment.id}")
            print(f"Fecha: {appointment.date}")
            print(f"Hora: {appointment.hour}")
            print(f"Doctor: {appointment.doctor}")
            print(f"Tipo de cita: {appointment.appointmentType}")
            print() 
    else:
        print("No hay citas programadas")

