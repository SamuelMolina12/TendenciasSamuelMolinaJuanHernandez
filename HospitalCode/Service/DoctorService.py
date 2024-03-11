import datetime
import Models.models as models

def validateId(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return patient
    return None

def validateId1(hospital,id):
    for patient in hospital.patient:
        if patient.id==id:
            return id
    return None

def ValidateOrder(hospital,orderId):
    for order in hospital.orders:
        if order.orderId==orderId:
            return orderId
    return None




def createHistoryClinicQuery(hospital,patientId,doctorId,consultationReason,symptomatology,diagnosis,order):
    patient = validateId(hospital,patientId)
    if not patient:
        raise Exception("no existe el paciente")
    newhistoryClinic ={}
    date = datetime.datetime.today()
    newhistoryClinic["doctorId"]=doctorId
    newhistoryClinic["consultationReason"]=consultationReason
    newhistoryClinic["symptomatology"]=symptomatology
    newhistoryClinic["diagnosis"]=diagnosis
    newhistoryClinic["order"]=order     
    hospital.historyClinic[str(patientId)][date] = newhistoryClinic
  






def showHistoryClinicQuery(hospital, patientId):
    patient = validateId(hospital, patientId)
    if not patient:
        raise Exception("no existe el paciente")
    
    patient_history = hospital.historyClinic.get(str(patientId))
    if not patient_history:
        raise Exception("No hay historial clinico para este paciente.")
    
def createOrder(hospital, orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure):
    patientId = validateId1(hospital,patientId)
    if not patientId:
        raise Exception("no existe el paciente")   
    order= models.Order(orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure) 
    hospital.orders.append(order)
    return order 
    
     
def createMedicine(hospital,orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost):
    medicine = models.Medicine(orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost)
    hospital.medicines.append(medicine)
    return medicine
   


def createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
    procedure = models.Procedure(orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    hospital.procedures.append(procedure)
    return procedure

    
def createDiagnosticHelp(hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId):
    diagnosticHelp = models.DiagnosticHelp(orderId,itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    hospital.diagnosticHelp.append(diagnosticHelp)
    return diagnosticHelp
    


