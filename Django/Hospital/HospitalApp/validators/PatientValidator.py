import  HospitalApp.validators.TypeValidator as validators
import  HospitalApp.service.PatientService as staffAdminService



def createPatient(id, name, mail,genre, telephone, birth, address):
    id = validators.numberValidator(id,"id")

    
    id= validators.documentValidator(id,"id")

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


    validators.numberValidator(doctor, "nombre del doctor  \n")
    
    validators.textValidator(appointmentType, "tipo de cita\n")

    validators.numberValidator(patientId, "paciente\n")

    staffAdminService.createClinicalAppointment( date, hour, doctor, appointmentType,patientId)
  


def getPatient(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getPatient(id)

def getPatients():

    return staffAdminService.getPatients() 



def getEmergencyContact(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getEmergencyContact(id)

def getPolicy(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getPolicy(id)

def getClinicalAppointment(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getClinicalAppointment(id)

def getClinicalAppointmentPatient(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getClinicalAppointmentPatient(id)

def deletePatient(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.deletePatient(id)

def deleteClinicalAppointment(id):
    id = validators.numberValidator(id,"id")
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

def createOrder(patient,doctor):

    validators.numberValidator(patient, "cedula paciente  \n")

    validators.numberValidator(doctor, "nombre del doctor  \n")


    
    return staffAdminService.createOrder(patient,doctor)

def getOrder(id):
    id = validators.numberValidator(id,"id")    
    return staffAdminService.getOrder(id)


    #orden medicina
def getOrderMedicine(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getOrderMedicine(id)
    
def createOrderMedicine(medicineDose,durationMedication,medicine_id,order_id):

    # validators.numberValidator(itemMedicine, "item Medicina \n")

    validators.textValidator(medicineDose, "dosis \n")

    validators.textValidator(durationMedication, "duracion \n")

    validators.numberValidator(medicine_id, "id de la medicina  \n")

    validators.numberValidator(order_id,"id d ela orden")

    return staffAdminService.createOrderMedicine(medicineDose,durationMedication,medicine_id,order_id)


    #order procedimiento

def getOrderProcedure(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getOrderProcedure(id)
   
def createOrderProcedure(numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id):

    # validators.numberValidator(itemProcedure, "item Procedimiento \n")

    validators.textValidator(numberRepeated, "veces que se repite \n")

    validators.textValidator(frequencyRepeated, "frecuencia con la que se repite  \n")

    requiresSpecialistP=validators.booleanValidator(requiresSpecialistP, "requiere especialista \n")

    
    if requiresSpecialistP:
         validators.numberValidator(specialist_id, "id especialista")
    else:  
         specialist_id = None


  
    validators.numberValidator(order_id,"id d ela orden")

    validators.numberValidator(procedure_id,"id del procedimiento")


    return staffAdminService.createOrderProcedure(numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id)

    #Orden ayuda dignostica
def getOrderDiagnosticHelp(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getOrderDiagnosticHelp(id)
    
def createOrderDiagnosticHelp(quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id):

    # validators.numberValidator(itemDiagnosticHelp, "item ayuda diagnostica \n")

    validators.textValidator(quantity, "Cantidad  \n")
    requiresSpecialistD=validators.booleanValidator(requiresSpecialistD, "requiere especialista \n")

    if requiresSpecialistD:
         validators.numberValidator(specialist_id, "id especialista")
    else:  
         specialist_id = None

    validators.numberValidator(order_id,"id d ela orden")

    validators.numberValidator(diagnosticHelp_id,"id del procedimiento")


    return staffAdminService.createOrderDiagnosticHelp(quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id)


#historias
 #historia clinica
def getHistoryClinic(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getHistoryClinic(id)

def createHistoryClinic(patient_id, doctor,reason,symptoms,diagnosis,order):   
    validators.numberValidator(patient_id, "paciente")

    # validators.dateValidator(date, "fecha  \n")

    validators.textValidator(doctor, "nombre del doctor  \n")
    
    validators.textValidator(reason, "razon \n")

    validators.textValidator(symptoms, "razon \n")

    validators.textValidator(diagnosis, "razon \n")

    validators.numberValidator(order, "orden \n")   
    staffAdminService.createHistoryClinic(patient_id, doctor,reason,symptoms,diagnosis,order)

#historia visita

def getHistoryVisits(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getHistoryVisits(id)


def createHistoryVisits(patient, doctor,bloodPressure,temperature,pulse,bloodOxygeLevel,order,items):   
    
    validators.numberValidator(patient, "paciente")

    validators.textValidator(doctor, "nombre del doctor  \n")
    
    validators.textValidator(bloodPressure, "presion arterial \n")

    validators.textValidator(temperature, "temperatura \n")

    validators.textValidator(pulse, "pulse \n") 

    validators.textValidator(bloodOxygeLevel, "nivel deoxigeno en la sangre \n")   

    validators.numberValidator(order, "orden \n")   

    staffAdminService.createHistoryVisits(patient, doctor,bloodPressure,temperature,pulse,bloodOxygeLevel,order,items)

#factura
def createBilling(patient_id,doctor_id,order_id):   
    
    validators.numberValidator(patient_id, "paciente")
    
    validators.numberValidator(doctor_id, "total \n")
    
    validators.numberValidator(order_id, "orden \n")

    staffAdminService.createBilling(patient_id,doctor_id,order_id)

def getBilling(id):
    id = validators.numberValidator(id,"id")
    return staffAdminService.getBilling(id)    

