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
    
    date=datetime.date.today()
    newVisitHistory={}
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
    print(date)
    print("nueva historia clinica")
    print(newVisitHistory)
    print(str(patientId))
    hospital.historyVisits[str(patientId)][str(date)] = newVisitHistory

def showHistoryVisitsQuery(hospital, patientId):
    patient_history = hospital.historyVisits.get(str(patientId))
    if not patient_history:
        print("No hay historial de visitas para este paciente.")
        return

    print("Historial de visitas para el paciente:")
    for visit_date, visit_details in patient_history.items():
        print(f"Fecha de visita: {visit_date}")
        for key, value in visit_details.items():
            print(f"{key}: {value}")
        print("-----------------------------")
  