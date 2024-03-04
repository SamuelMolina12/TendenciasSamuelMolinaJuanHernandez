import Models.models as models

def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None


def createPatient(hospital, id, name, genre, mail, telephone, birth, address, emergency_contact_info, policy_info):
    patient = validateId(hospital, id)
    if patient:
        raise Exception("Ya existe una persona con esa cédula registrada")
    patient = models.Patient(id, name, genre, mail, telephone, birth, address)
    emergency_contact = models.EmergencyContact(id, emergency_contact_info['name'], emergency_contact_info['relationship'], emergency_contact_info['telephone'])
    patient.emergencyContact = emergency_contact
    policy = models.Policy(id, policy_info['insuranceCompany'], policy_info['policynumber'], policy_info['statePolicy'], policy_info['termPolicy'])
    patient.policy = policy
    hospital.patient.append(patient)

    return patient

def findPatient(hospital, id):
    patient = hospital.patient
    for human in patient:
        if human.id == id:
            return human
    return None

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

