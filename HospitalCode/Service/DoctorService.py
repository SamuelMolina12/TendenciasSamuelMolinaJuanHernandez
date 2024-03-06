
def validateId(hospital,id):
    print(id)
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None

def createHistoryClinic(hospital):
    pass
   