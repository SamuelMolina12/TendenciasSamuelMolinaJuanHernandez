import Models.models as models

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





def createPatient(hospital, id, name, genre, mail, telephone, birth, address):
    patient = validateId(hospital, id)
    if patient:
        raise Exception("Ya existe una persona con esa cédula registrada")
    patient = models.Patient(id, name, genre, mail, telephone, birth, address)
    hospital.historyVisits[str(id)] ={}
    hospital.patient.append(patient)
    

def createEmergencyContact(hospital, patientId, name, relationship, telephone):
    patient = None
    for p in hospital.patient:
        if p.id == patientId:
            patient = p
            break

    if patient is None:
        raise Exception("No se encontró ningún paciente con ese ID")

    emergencyContact = models.EmergencyContact(patientId, name, relationship, telephone)
    patient.emergencyContact = emergencyContact
    hospital.emergencyContact.append(emergencyContact)

    
def createPolicy(hospital, patientId, insuranceCompany, policynumber, statePolicy, termPolicy):
    patient = None
    for p in hospital.patient:
        if p.id == patientId:
            patient = p
            break

    if patient is None:
        raise Exception("No se encontró ningún paciente con ese ID")
    policy = models.Policy(patientId, insuranceCompany, policynumber, statePolicy, termPolicy)
    patient.policy = policy
    hospital.policy.append(policy)



def deletePatient(hospital,id):
    for user in hospital.patient:
        if user.id == id:
            return True
    return False

def updateUser(hospital,id):
    for user in hospital.patient:
        if user.id == int(id):
            return user
    return None

def createClinicalAppointment(hospital,patientId,date,hour,doctor,appointmentType):
    appointment = validateId(hospital,patientId)
    if not appointment:
        raise Exception("no hay un paciente con esa cedula")
    appointment = models.ClinicalAppointment(patientId,date,hour,doctor,appointmentType)
    hospital.clinicalAppointment.append(appointment)

def validateClinicalAppointment(hospital,id):
    for appointment in hospital.clinicalAppointment:
        if appointment.id==id:
            return appointment
    return None


def validatePatient(hospital, patientId):
    for p in hospital.patient:
        if p.id == patientId:
            return p
    raise Exception("No se encontró ningún paciente con ese ID")

def createBilling(hospital, patientId, doctorName, policy, orders, cost):
    if not validateDoctorName(hospital, doctorName):
        raise Exception("El nombre del doctor ingresado no es válido")
    for order in orders:       
        hospital.paidOrders.append(order)

    patient = validatePatient(hospital, patientId)
    orders = vars(order)
    billing = models.Billing(patientId, patient.name, patient.id, patient.birth, doctorName, policy, orders, cost)
    billing = vars(billing)
    return billing
