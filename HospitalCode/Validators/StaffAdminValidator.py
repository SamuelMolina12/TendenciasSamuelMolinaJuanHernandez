import Validators.TypeValidator as validators
import Models.models as models
import Service.StaffAdminService as staffAdminService



def createPatient(hospital):
    id = validators.numberValidator(input("Ingrese la cédula:\n"), "cedula de")
    name = input("Ingrese el nombre :\n")
    validators.textValidator(name, "nombre  \n")
    genre = input("Ingrese el género: masculino o femenino\n")
    validators.textValidator(genre, "genero de\n")
    validators.genreValidator(genre, "genero de\n")
    mail = input("Ingrese el correo:\n")
    validators.textValidator(mail, "correo  \n")
    validators.emailValidator(mail,"correo \n")
    telephone = validators.phoneValidator(input("ingrese el numero telefonico " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
    birth = validators.dateValidator(input("ingrese la fecha de nacimiento " + "Formato DD/MM/YYYY, max 150 años\n"),"fecha de nacimiento de")
    address = input("ingrese la direccion " + "Máximo 30 caracteres  \n")
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")
    staffAdminService.createPatient(hospital, id, name, genre, mail, telephone, birth, address)
    print("Contacto de emergencia")
    createEmergencyContact(hospital,id)
    print("Póliza")
    createPolicy(hospital,id)
    print("Paciente creado con exito")

    

def createEmergencyContact(hospital,patientId):
    name = input("Ingrese el nombre del contacto de emergencia del paciente: \n") 
    validators.textValidator(name,"Nombre del paciente")
    relationship = input("Ingrese la relacion del contacto de emergencia:\n")
    validators.textValidator(relationship,"Relacion del contacto de emergencia")
    telephone = validators.phoneValidator(input("ingrese el numero de contacto de emergencia " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
    staffAdminService.createEmergencyContact(hospital,patientId,name,relationship,telephone)

def createPolicy(hospital,patientId):
    insuranceCompany = input("Ingrese el nombre de la compañia: \n")
    validators.textValidator(insuranceCompany, "nombre de la compañia \n")
    policynumber = validators.numberValidator(input("Ingrese el numero de poliza: \n"), "Numero de poliza")
    statePolicy = input("Ingrese el estado de la poliza: \n")
    validators.policyStateValidator(statePolicy, "estado de la poliza \n")
    termPolicy = input("Ingrese la fecha de terminacion de la poliza: \n")
    validators.dateValidator(termPolicy, "fecha de \n")
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

        newName = input("ingrese el nuevo nombre \n")
        newGenre = input("ingrese el nuevo genero \n")
        newMail = input("ingrese el nuevo correo " + " dominio y el @ \n")
        newTelephone = input("Nuevo telefono: " + "Debe contener entre 1 y 10 dígitos") 
        newBirth = input("nueva fecha de nacimiento: " + "Formato DD/MM/YYYY")
        newAddress = input("ingrese la nueva direccion " + "Máximo 30 caracteres\n")
        updateEmergencyContact(patient)
        updatePolicy(patient)
            
        if newName:
            validators.textValidator(newName,"el nuevo nombre \n")
            patient.name = newName
        if newGenre:
            validators.genreValidator(newGenre, "nuevo genero: masculino o femenino\n")
            
        if newMail:
            newMail=validators.emailValidator( newMail,"nuevo correo \n")
            
        if newTelephone:
            newTelephone=validators.phoneValidator(newTelephone, "nuevo numero de telefono\n")
            
        if newBirth:
            newBirth=validators.dateValidator(newBirth, "nuevo fecha de nacimiento\n")
            
        if newAddress:
            newAddress=validators.addressValidator(newAddress, "direccion \n")
            


        #patient.name = newName if newName else patient.name
        patient.genre = newGenre if newGenre else patient.genre
        patient.mail = newMail if newMail else patient.mail
        patient.telephone = newTelephone if newTelephone else patient.telephone
        patient.birth = newBirth if newBirth else patient.birth
        patient.address = newAddress if newAddress else patient.address 


        print("Paciente actualizado correctamente.")
    else:
        print("No se encontró ningún paciente con ese ID.")

def updateEmergencyContact(patient):
    
    newName = input("Nuevo nombre de contacto de emergencia: ")
    newRelationship = input("Nueva relación con el paciente: ")
    newTelephone = input("Nuevo telefono de contacto de emergencia: " + "Debe contener entre 1 y 10 dígitos") 
    
    
    if newName:
        validators.textValidator(newName,"el nuevo nombre \n")
        patient.emergencyContact.name = newName
        
    if newRelationship:
        validators.textValidator(newRelationship,"nueva relacion con el paciente \n")
        patient.emergencyContact.relationship = newRelationship

    if newTelephone:
        newTelephone=validators.phoneValidator(newTelephone, "nuevo numero de telefono\n")
        
    #patient.emergencyContact.name = newName if newName else patient.emergencyContact.name
    #patient.emergencyContact.relationship = newRelationship if newRelationship else patient.emergencyContact.relationship     
    patient.emergencyContact.telephone = newTelephone if newTelephone else patient.emergencyContact.telephone    

def updatePolicy(patient):
    newInsuranceCompany = input("Nuevo nombre del la compañia: ")
    
    newPolicynumber = input("Nuevo numero de poliza: ")
    
    newStatePolicy = input("Nuevo estado de la poliza: ")
    
    newTermPolicy = input("Nueva fecha de termino de poliza: ")
    

    if newInsuranceCompany :
        validators.textValidator(newInsuranceCompany,"el nuevo nombre \n")
        patient.policy.insuranceCompany = newInsuranceCompany 
    if newPolicynumber:
        validators.numberValidator(newPolicynumber," nuevo numero de poliza \n")
        patient.policy.policynumber = newPolicynumber
    if newStatePolicy:
        validators.textValidator(newStatePolicy,"nuevo estado de la poliza \n")
        patient.policy.statePolicy =  newStatePolicy
    if  newTermPolicy:
        validators.textValidator(newTermPolicy,"nueva fecha de finalizacion de poliza \n")
        patient.policy.termPolicy =  newTermPolicy

    #patient.policy.insuranceCompany = newInsuranceCompany if newInsuranceCompany else patient.policy.insuranceCompany
    #patient.policy.policynumber =newPolicynumber if newPolicynumber else patient.policy.policynumber
    #patient.policy.statePolicy =newStatePolicy if newStatePolicy else patient.policy.statePolicy
    #patient.policy.termPolicy =newTermPolicy if newTermPolicy else patient.policy.termPolicy


def createClinicalAppointment(hospital,id):
    patientId = id
    date= input("Ingrese la fecha de la cita:\n")
    validators.dateValidator(date, "fecha  \n")
    hour = input("ingrese la hora de la cita\n")
    validators.timeValidator(hour, "hora de\n")
    doctor = input("Ingrese el nombre del doctor al que se le asignara la cita:\n")
    validators.textValidator(doctor, "correo  \n")
    appointmentType = input("ingrese el tipo de cita\n")
    validators.textValidator(appointmentType, "direccion de\n")
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



def createBilling(hospital, patientId):
    try:
       
        patient = None
        for p in hospital.patient:
            if p.id == patientId:
                patient = p
                break

        if patient is None:
            raise Exception("No se encontró ningún paciente con ese ID")

        doctorName = input("Ingrese el nombre del doctor: ")
        validators.textValidator(doctorName, "nombre del doctor")

       
        policy = None
        for pol in hospital.policy:
            if pol.patientId == patientId:
                policy = pol
                break

        if policy is None:
            raise Exception("El paciente no tiene ninguna póliza asociada")

       
        orders = [order for order in hospital.orders if order.patientId == patientId]

        cost = input("Ingrese el costo: ")
        validators.costValidator(cost, "costo")

        billing = models.Billing(patientId, patient.name, patient.id, patient.birth, doctorName, policy, orders, cost)
        
        billing = vars(billing)
        print (billing)
        return billing
        
    except Exception as error:
        print(str(error))



