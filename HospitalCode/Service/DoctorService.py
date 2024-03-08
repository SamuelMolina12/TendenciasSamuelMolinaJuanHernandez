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
    
def createOrder(hospital, orderId, patientId, doctorId,date):
    patientId = validateId1(hospital,patientId)
    if not patientId:
        raise Exception("no existe el paciente")   
    order= models.Order(orderId, patientId, doctorId,date) 
    hospital.orders.append(order)
    print("Exito")
     
def createMedicine(hospital,orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost):
    order = None
    for o in hospital.orders:
        if o.orderId == orderId:
            order = o
            break
    if order is None:
        raise Exception("No se encontró ninguna orden con ese ID")
    medicine = models.Medicine(orderId, itemMedicine, medicineName, medicineDose, durationMedication, medicineCost)
    order.medicines.append(medicine)
    hospital.orders.append(medicine)

def createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
    order = None
    for o in hospital.orders:
        if o.orderId == orderId:
            order = o
            break
    if order is None:
        raise Exception("No se encontró ninguna orden con ese ID")
    procedure = models.Procedure(orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    order.procedure.append(procedure)
    hospital.orders.append(procedure)

def createDiagnosticHelp(hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId):
    order = None
    for o in hospital.orders:
        if o.orderId == orderId:
            order = o
            break
    if order is None:
        raise Exception("No se encontró ninguna orden con ese ID")    
    diagnosticHelp = models.DiagnosticHelp(orderId,itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    order.diagnosticHelp.append(diagnosticHelp)
    hospital.orders.append(diagnosticHelp)


    


