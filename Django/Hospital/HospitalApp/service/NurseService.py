import datetime
import HospitalApp.models as models













# def validateId(hospital,id):
#     for patient in hospital.patient:
#         if patient.id==id:
#             return patient
#     return None

# # def validateNurseId(hospital, id):
# #     for nurse in hospital.persons:
# #         if nurse.id == id:
# #             return nurse
# #     return None

# def validateId1(hospital,id):
#     for patient in hospital.patient:
#         if patient.id==id:
#             return id
#     return None

# def createHistoryVisitsQuery(hospital,patientId,nurseId,bloodPressure,temperature,pulse,oxygenBlood,observation,orderD):
#     patient = validateId(hospital,patientId)
#     if not patient:
#         raise Exception("no existe el id")
    
    
#     newVisitHistory={}
#     date = datetime.datetime.today()
#     newVisitHistory["nurseId"]=nurseId
#     newVisitHistory["bloodPressure"]=bloodPressure
#     newVisitHistory["temperature"]=temperature
#     newVisitHistory["pulse"]=pulse
#     newVisitHistory["oxygenBlood"]=oxygenBlood
#     newVisitHistory["order"]=orderD 
#     if observation!="N/A":
#         newVisitHistory["observation"]=observation        
#     hospital.historyVisits[str(patientId)][date] = newVisitHistory



# def showHistoryVisitsQuery(hospital, patientId):
#     patient = validateId(hospital, patientId)
#     if not patient:
#         raise Exception("no existe el paciente")
    
#     patient_history = hospital.historyVisits.get(str(patientId))
#     if not patient_history:
#         raise Exception("No hay historial de visitas para este paciente.")
        

# def createOrder(hospital, orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure):
#     patientId = validateId1(hospital,patientId)
#     if not patientId:
#         raise Exception("no existe el paciente")   
#     order= models.Order(orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure) 
#     hospital.orders.append(order)
#     return order  
   
# def createMedicine(hospital,orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost):
#     medicine = models.Medicine(orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost)
#     hospital.medicines.append(medicine)
#     return medicine
   


# def createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
#     procedure = models.Procedure(orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
#     hospital.procedures.append(procedure)
#     return procedure    

