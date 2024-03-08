import datetime

def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None

# def validateNurseId(hospital, id):
#     for nurse in hospital.persons:
#         if nurse.id == id:
#             return nurse
#     return None



def createHistoryVisitsQuery(hospital,patientId,bloodPressure,temperature,pulse,oxygenBlood,medicine,medicineDose,procedure,procedureDetail,medicaltests,observation):
    patient = validateId(hospital,patientId)
    if not patient:
        raise Exception("no existe el id")
    
    
    newVisitHistory={}
    date = datetime.datetime.today()
    newVisitHistory["bloodPressure"]=bloodPressure
    newVisitHistory["temperature"]=temperature
    newVisitHistory["pulse"]=pulse
    newVisitHistory["oxygenBlood"]=oxygenBlood
    if medicine!="N/A":
        newVisitHistory["medicine"]=medicine
        newVisitHistory["medicineDose"]=medicineDose 
    if procedure!="N/A":
        newVisitHistory["procedure"]=procedure
        newVisitHistory["procedureDetail"]=procedureDetail
    newVisitHistory["medicaltests"]= medicaltests 
    if observation!="N/A":
        newVisitHistory["observation"]=observation        
    hospital.historyVisits[str(patientId)][date] = newVisitHistory



def showHistoryVisitsQuery(hospital, patientId):
    patient = validateId(hospital, patientId)
    if not patient:
        raise Exception("no existe el paciente")
    
    patient_history = hospital.historyVisits.get(str(patientId))
    if not patient_history:
        raise Exception("No hay historial de visitas para este paciente.")
        
    
    
