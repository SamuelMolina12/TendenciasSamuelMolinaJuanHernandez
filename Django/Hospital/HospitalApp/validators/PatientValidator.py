import  HospitalApp.validators.TypeValidator as validators
import  HospitalApp.service.PatientService as staffAdminService



def createPatient(id, name, mail,genre, telephone, birth, address):
    id = validators.numberValidator(id,"cedula de")
   
    validators.textValidator(name, "nombre  \n")


    validators.textValidator(genre, "genero de\n")
    validators.genreValidator(genre, "genero de\n")

    
    validators.textValidator(mail, "correo  \n")
    validators.emailValidator(mail,"correo \n")

    telephone = validators.phoneValidator(telephone, "numero telefonico ")

    birth = validators.dateValidator(birth,"fecha de nacimiento de")

    

    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")

    staffAdminService.createPatient( id, name, mail,genre, telephone, birth, address)
    



    

def createEmergencyContact(name,relationship,telephone,patientId):
    
    validators.textValidator(name,"Nombre del contacto")

   
    validators.textValidator(relationship,"Relacion del contacto de emergencia")

    telephone = validators.phoneValidator(telephone, "numero telefonico ")

    staffAdminService.createEmergencyContact(name,relationship,telephone,patientId)

def createPolicy(insuranceCompany,policyNumber,statePolicy,termPolicy,patientId):

   
    validators.textValidator(insuranceCompany, "nombre de la compañia \n")
    policyNumber = validators.numberValidator(policyNumber, "Numero de poliza")

    if statePolicy == "Inactiva":
        termPolicy = "N/A"
    else:
        termPolicy = validators.policyTermValidator(termPolicy, "fecha de \n")


    staffAdminService.createPolicy(insuranceCompany,policyNumber,statePolicy,termPolicy,patientId)



def createClinicalAppointment (date, hour, doctor, appointmentType,patientId):
  

    validators.dateValidator(date, "fecha  \n")

    validators.timeValidator(hour, "hora de\n")


    validators.textValidator(doctor, "nombre del doctor  \n")
    
    validators.textValidator(appointmentType, "tipo de cita\n")

    staffAdminService.createClinicalAppointment( date, hour, doctor, appointmentType,patientId)
  


def getPatient(id):
    return staffAdminService.getPatient(id)

def getPatients():
    return staffAdminService.getPatients() 



def getEmergencyContact(id):
    return staffAdminService.getEmergencyContact(id)

def getPolicy(id):
    return staffAdminService.getPolicy(id)

def getClinicalAppointment(id):
    return staffAdminService.getClinicalAppointment(id)



def deletePatient(id):

    return staffAdminService.deletePatient(id)

def deleteClinicalAppointment(id):
    return staffAdminService.deleteClinicalAppointment(id)


def updatePatient(id, name, mail,genre, telephone, birth, address):
    validators.textValidator(name, "nombre  \n")


    validators.textValidator(genre, "genero de\n")
    validators.genreValidator(genre, "genero de\n")

    
    validators.textValidator(mail, "correo  \n")
    validators.emailValidator(mail,"correo \n")

    telephone = validators.phoneValidator(telephone, "numero telefonico ")

    birth = validators.dateValidator(birth,"fecha de nacimiento de")

    

    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")

   

    return staffAdminService.updatePatient(id, name, mail,genre, telephone, birth, address)

def updatePolicy(insuranceCompany,policyNumber,statePolicy,termPolicy,patientId):
    validators.textValidator(insuranceCompany, "nombre de la compañia \n")
    policyNumber = validators.numberValidator(policyNumber, "Numero de poliza")

    if statePolicy == "Inactiva":
        termPolicy = "N/A"
    else:
        termPolicy = validators.policyTermValidator(termPolicy, "fecha de \n")

   
    return staffAdminService.updatePolicy(insuranceCompany,policyNumber,statePolicy,termPolicy,patientId)

def updateEmergencyContact(name,relationship,telephone,patientId):
    
    validators.textValidator(name,"Nombre del contacto")

   
    validators.textValidator(relationship,"Relacion del contacto de emergencia")

    telephone = validators.phoneValidator(telephone, "numero telefonico ")

    
    return staffAdminService.updateEmergencyContact(name,relationship,telephone,patientId)


#Ordenes

def createOrder(patient,doctor,date):

    validators.numberValidator(patient, "cedula paciente  \n")

    validators.numberValidator(doctor, "nombre del doctor  \n")

    validators.dateValidator(date, "fecha  \n")
    
    return staffAdminService.createOrder(patient,doctor,date)

def createOrderMedicine(itemMedicine,medicineDose,medicine_id,order_id):

    validators.numberValidator(itemMedicine, "item Medicina \n")

    validators.textValidator(medicineDose, "dosis \n")

    validators.numberValidator(medicine_id, "id de la medicina  \n")

    validators.numberValidator(order_id,"id d ela orden")

    return staffAdminService.createOrderMedicine(itemMedicine,medicineDose,medicine_id,order_id)

def createOrderProcedure(itemProcedure,numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id):

    validators.numberValidator(itemProcedure, "item Procedimiento \n")

    validators.textValidator(numberRepeated, "veces que se repite \n")

    validators.textValidator(frequencyRepeated, "frecuencia con la que se repite  \n")

    if requiresSpecialistP:
         validators.numberValidator(specialist_id, "id especialista")
    else:  
         specialist_id = None


  
    validators.numberValidator(order_id,"id d ela orden")

    validators.numberValidator(procedure_id,"id del procedimiento")


    return staffAdminService.createOrderProcedure(itemProcedure,numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id)

def createOrderDiagnosticHelp(itemDiagnosticHelp,quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id):

    validators.numberValidator(itemDiagnosticHelp, "item ayuda diagnostica \n")

    validators.textValidator(quantity, "Cantidad  \n")

    if requiresSpecialistD:
         validators.numberValidator(specialist_id, "id especialista")
    else:  
         specialist_id = None

    validators.numberValidator(order_id,"id d ela orden")

    validators.numberValidator(diagnosticHelp_id,"id del procedimiento")


    return staffAdminService.createOrderDiagnosticHelp(itemDiagnosticHelp,quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id)


#historias


def createHistoryClinic (patient_id,date, doctor,reason,symptoms,diagnosis):
     
    # validators.numberValidator(patient_id, "paciente")

    validators.dateValidator(date, "fecha  \n")

    validators.textValidator(doctor, "nombre del doctor  \n")
    
    validators.textValidator(reason, "razon \n")

    validators.textValidator(symptoms, "razon \n")

    validators.textValidator(diagnosis, "razon \n")    
    staffAdminService.createHistoryClinic (patient_id,date, doctor,reason,symptoms,diagnosis)