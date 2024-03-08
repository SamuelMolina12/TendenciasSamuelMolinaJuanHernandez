import datetime


def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None

def createHistoryClinicQuery(hospital,patientId,doctorId,consultationReason,symptomatology,diagnosis):
    patient = validateId(hospital,patientId)
    if not patient:
        raise Exception("no existe el paciente")
    newhistoryClinic ={}
    date = datetime.datetime.today()
    newhistoryClinic["doctorId"]=doctorId
    newhistoryClinic["consultationReason"]=consultationReason
    newhistoryClinic["symptomatology"]=symptomatology
    newhistoryClinic["diagnosis"]=diagnosis
         
    hospital.historyClinic[str(patientId)][date] = newhistoryClinic
    print(newhistoryClinic)
    print("historia clinica")
    print(hospital.historyClinic[str(patientId)])
   
def showHistoryClinicQuery(hospital, patientId):
    patient = validateId(hospital, patientId)
    if not patient:
        raise Exception("no existe el paciente")
    
    patient_history = hospital.historyClinic.get(str(patientId))
    if not patient_history:
        raise Exception("No hay historial clinico para este paciente.")