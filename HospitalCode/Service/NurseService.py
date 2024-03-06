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
    id = patientId
    patient = validateId(hospital,id)
    if not patient:
        raise Exception("no existe el id")
    # patientName = patient.name
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
    hospital.historyVisits[str(id)][date]=newVisitHistory
    print("historia clinica")
    print(hospital.historyVisits[str(id)])