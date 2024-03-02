import Models.models as models

def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None


def createPatient(hospital,id,name,genre,mail,telephone,birth,address,emergencyContact,policy,clinicHistory):
    patient=validateId(hospital,id)
    print("busca paciente")
    if patient:
        raise Exception("ya existe una persona con esa cedula registrada")
    patient=models.Patient(id,name,genre,mail,telephone,birth,address,emergencyContact,policy,clinicHistory)
    
    hospital.patient.append(patient)
   
    return patient

def findPatient(hospital, id):
    patient = hospital.patient
    for human in patient:
        if human.id == id:
            return human
    return None
