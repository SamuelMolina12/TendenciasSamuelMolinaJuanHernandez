import HospitalApp.models as models

def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None

def validateDoctorName(hospital, doctorName):
    for person in hospital.persons:
        if person.name == doctorName and person.role == "doctor":
            return True
    return False





def createPatient(id, name, mail,genre, telephone, birth, address):
    patient = models.Patient.objects.filter(id=id)
    if patient.exists():
        raise Exception("Ya existe una persona con esa cédula registrada")
    patient = models.Patient(id, name, mail,genre, telephone, birth, address)
    patient.save()
    return patient.id

   


def createEmergencyContact(name, relationship, telephone, patientId):
    # emergencyContact = models.Patient.objects.filter(id=patientId)
    # if not emergencyContact.exists():
    #     raise Exception("No existe un paciente con esa cédula registrada")
    

    emergencyContact = models.EmergencyContact(name=name, relationship=relationship, telephone=telephone, patient_id=patientId)
    emergencyContact.save()


    
def createPolicy(insuranceCompany, policyNumber, statePolicy, termPolicy,patientId):

    # policy = models.Patient.objects.filter(id=patientId)
    # if not policy.exists():
    #     raise Exception("No existe un paciente con esa cédula registrada")
    
    policy = models.Policy(insuranceCompany=insuranceCompany, policyNumber=policyNumber, statePolicy=statePolicy, termPolicy=termPolicy, patient_id=patientId)
    policy.save()





def createClinicalAppointment(date,hour,doctor,appointmentType,patientId):
    appointment = models.Patient.objects.filter(id=patientId)
    if not appointment.exists():
         raise Exception("No existe un paciente con esa cédula registrada")
    
    appointment = models.ClinicalAppointment(date=date, hour=hour, doctor=doctor, appointmentType=appointmentType,patient_id=patientId)
    appointment.save()

def getPatients():
    patient = models.Patient.objects.all()
    if patient:
        return patient
    else:
        raise Exception("No hay pacientes para mostrar")

def getPatient(id):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        return patient
    else:
        raise Exception("No hay un paciente con ese id")
    


def getEmergencyContact(id):
    emergencyContact = models.EmergencyContact.objects.filter(patient_id=id)
    return list(emergencyContact)

def getPolicy(id):
    policy = models.Policy.objects.filter(patient_id=id)
    return list(policy)  



def deletePatient(id):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        patient.delete()
    else:
        raise Exception("paciente no encontrado")
    
def updatePatient( id,name, mail,genre, telephone, birth, address):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        patient.name = name
        patient.genre = genre
        patient.mail = mail
        patient.telephone = telephone
        patient.birth = birth
        patient.address = address
        patient.save()
    else:
        raise Exception("Paciente no encontrado")
def updatePolicy(insuranceCompany, policyNumber, statePolicy, termPolicy,patientId):
    policy = models.Policy.objects.filter(patient_id=patientId).first()
    if policy:
        policy.insuranceCompany = insuranceCompany
        policy.policyNumber = policyNumber
        policy.statePolicy = statePolicy
        policy.termPolicy = termPolicy
        policy.save()
    else:
        raise Exception("Poliza no encontrada")
    
def updateEmergencyContact(name, relationship, telephone, patientId):
    emergency = models.EmergencyContact.objects.filter(patient_id=patientId).first()
    if emergency:
        emergency.name = name
        emergency.relationship = relationship
        emergency.telephone = telephone
        emergency.save()
    else:
        raise Exception("Contacto de emergencia no encontrado")            