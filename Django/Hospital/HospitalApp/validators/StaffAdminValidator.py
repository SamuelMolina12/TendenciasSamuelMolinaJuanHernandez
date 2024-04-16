import  HospitalApp.validators.TypeValidator as validators
import  HospitalApp.service.StaffAdminService as staffAdminService
from Hospital.conection_mongo import collection


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
    
    # createEmergencyContact(id)
   
    # createPolicy(id)
    clinicHistory={"_id":str(id),"historias":{}}
    collection.insert_one(clinicHistory)

    

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


def deletePatient(id):
    clinicHistory={"_id":str(id),"historias":{}}
    collection.delete_one(clinicHistory)
    return staffAdminService.deletePatient(id)