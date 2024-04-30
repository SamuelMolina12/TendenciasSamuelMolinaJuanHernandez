from datetime import datetime
from datetime import date
import HospitalApp.models as models
from Hospital.conection_mongo import collection,collectionB





def createPatient(id, name, mail,genre, telephone, birth, address):
    patient = models.Patient.objects.filter(id=id)
    if patient.exists():
        raise Exception("Ya existe una persona con esa cédula registrada")
    patient = models.Patient(id, name, mail,genre, telephone, birth, address)
    patient.save()
    clinicHistory={"_id":str(id),"historias":{}}
    collection.insert_one(clinicHistory)
    visitHistory={"_id":str(id),"historias":{}}
    collectionB.insert_one(visitHistory)
    return patient.id
   

   


def createEmergencyContact(name, relationship, telephone, patientId):
    # emergencyContact = models.Patient.objects.filter(id=patientId)
    # if not emergencyContact.exists():
    #     raise Exception("No existe un paciente con esa cédula registrada")
    

    emergencyContact = models.EmergencyContact(name=name, relationship=relationship, telephone=telephone, patient_id=patientId)
    emergencyContact.save()


    
def createPolicy(insuranceCompany, policyNumber, statePolicy, termPolicy,patientId):

    # policy = models.Patient.objects.filter(id=patientId)
    # if not policy.exists():
    #     raise Exception("No existe un paciente con esa cédula registrada")
    
    policy = models.Policy(insuranceCompany=insuranceCompany, policyNumber=policyNumber, statePolicy=statePolicy, termPolicy=termPolicy, patient_id=patientId)
    policy.save()





def createClinicalAppointment(date,hour,doctor,appointmentType,patientId):
    appointment = models.Patient.objects.filter(id=patientId)
    if not appointment.exists():
         raise Exception("No existe un paciente con esa cédula registrada")
    
    appointment = models.ClinicalAppointment(date=date, hour=hour, doctor=doctor, appointmentType=appointmentType,patient_id=patientId)
    appointment.save()







def getPatients():
    patient = models.Patient.objects.all()
    if patient:
        return patient
    else:
        raise Exception("No hay pacientes para mostrar")

def getPatient(id):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        return patient
    else:
        raise Exception("No hay un paciente con ese id")
    


def getEmergencyContact(id):
    emergencyContact = models.EmergencyContact.objects.filter(patient_id=id)
    return list(emergencyContact)

def getPolicy(id):
    policy = models.Policy.objects.filter(patient_id=id)
    return list(policy)  

def getClinicalAppointment(id):
    appointments = models.ClinicalAppointment.objects.filter(patient_id=id)
    if appointments.exists():
        return appointments
    else:
        raise Exception("No hay citas médicas para este paciente")


def deletePatient(id):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        patient.delete()
    else:
        raise Exception("paciente no encontrado")
    clinicHistory = {"_id": str(id), "historias": []}
    collection.delete_one(clinicHistory)
    visitHistory = {"_id": str(id), "historias": {}}
    collectionB.delete_one(visitHistory)


def deleteClinicalAppointment(id):
    appointment = models.ClinicalAppointment.objects.filter(id=id).first()
    if appointment:
        appointment.delete()
    else:
        raise Exception("cita medica no encontrada")


def updatePatient( id,name, mail,genre, telephone, birth, address):
    patient = models.Patient.objects.filter(id=id).first()
    if patient:
        patient.name = name
        patient.genre = genre
        patient.mail = mail
        patient.telephone = telephone
        patient.birth = birth
        patient.address = address
        patient.save()
    else:
        raise Exception("Paciente no encontrado")
def updatePolicy(insuranceCompany, policyNumber, statePolicy, termPolicy,patientId):
    policy = models.Policy.objects.filter(patient_id=patientId).first()
    if policy:
        policy.insuranceCompany = insuranceCompany
        policy.policyNumber = policyNumber
        policy.statePolicy = statePolicy
        policy.termPolicy = termPolicy
        policy.save()
    else:
        raise Exception("Poliza no encontrada")
    
def updateEmergencyContact(name, relationship, telephone, patientId):
    emergency = models.EmergencyContact.objects.filter(patient_id=patientId).first()
    if emergency:
        emergency.name = name
        emergency.relationship = relationship
        emergency.telephone = telephone
        emergency.save()
    else:
        raise Exception("Contacto de emergencia no encontrado")


#----- orden
def getOrder(id):
    order = models.Order.objects.filter(id=id).first()
    if order:
        return order
    else:
        raise Exception("No hay una orden con ese id")
    
def createOrder(patient,doctor,date):
    patient = models.Patient.objects.get(id=patient)

    doctor = models.Employer.objects.get(id=doctor,role="doctor")
      
    order = models.Order()
    order.doctor=doctor
    order.patient=patient
    order.date=date
    order.save()   

    #orden medicina
def getOrderMedicine(id):
    medicine = models.OrderMedicine.objects.filter(order_id=id)
    if medicine:
        return medicine
    else:
        raise Exception("No hay una medicina asociada a esa orden")
        
def createOrderMedicine(medicineDose,durationMedication,medicine_id,order_id):
    



    medicine = models.Medicine.objects.filter(id=medicine_id)
    if not medicine.exists():
         raise Exception("No existe una medicina con ese id")
    order = models.Order.objects.filter(id=order_id)
    if not order.exists():
         raise Exception("No existe una orden con ese id")
    lastItemM = models.OrderMedicine.objects.filter(order_id=order_id).order_by('-itemMedicine').first()
    lastItemP = models.OrderProcedure.objects.filter(order_id=order_id).order_by('-itemProcedure').first()
    lastItemD = models.OrderDiagnosticHelp.objects.filter(order_id=order_id).order_by('-itemDiagnosticHelp').first()  

    if lastItemM:
        nextItemM = lastItemM.itemMedicine + 1
    else:
        nextItemM = 1
    if lastItemP and lastItemP.itemProcedure == nextItemM:
        nextItemM += 1
    if lastItemD and lastItemD.itemDiagnosticHelp == nextItemM:
        nextItemM += 1

    medicine = models.OrderMedicine(itemMedicine=nextItemM, medicineDose=medicineDose,durationMedication=durationMedication, medicine_id=medicine_id,order_id=order_id)
    medicine.save()


        
    #orden procedimiento
def getOrderProcedure(id):
    procedure = models.OrderProcedure.objects.filter(order_id=id)
    if procedure:
        return procedure
    else:
        raise Exception("No hay un procedimiento asociado a esa orden")

def createOrderProcedure(numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id):

    prcedure = models.Procedure.objects.filter(id=procedure_id)
    if not prcedure.exists():
         raise Exception("No existe un procedimiento con ese id")
    order = models.Order.objects.filter(id=order_id)
    if not order.exists():
         raise Exception("No existe una orden con ese id")
    if not specialist_id  is None:
        diagnosticHelp = models.Specialist.objects.filter(id=specialist_id)
        if not diagnosticHelp:
           raise Exception("No existe un especialista con ese id")
    lastItemM = models.OrderMedicine.objects.filter(order_id=order_id).order_by('-itemMedicine').first()
    lastItemP = models.OrderProcedure.objects.filter(order_id=order_id).order_by('-itemProcedure').first()
    lastItemD = models.OrderDiagnosticHelp.objects.filter(order_id=order_id).order_by('-itemDiagnosticHelp').first()  

    if lastItemP:
        nextItemP = lastItemP.itemProcedure + 1
    else:
        nextItemP = 1
    if lastItemM and lastItemM.itemMedicine == nextItemP:
        nextItemP += 1
    if lastItemD and lastItemD.itemDiagnosticHelp == nextItemP:
        nextItemP += 1

    prcedure = models.OrderProcedure(itemProcedure=nextItemP, numberRepeated=numberRepeated, frequencyRepeated=frequencyRepeated,requiresSpecialistP=requiresSpecialistP,order_id=order_id,procedure_id=procedure_id,specialist_id=specialist_id)
    prcedure.save()
    
    #orden ayuda diagnostica

def getOrderDiagnosticHelp(id):
    diagnostic = models.OrderDiagnosticHelp.objects.filter(order_id=id)
    if diagnostic:
        return diagnostic
    else:
        raise Exception("No hay un procedimiento asociado a esa orden")

def createOrderDiagnosticHelp(quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id):

    diagnostic = models.DiagnosticHelp.objects.filter(id=diagnosticHelp_id)
    if not diagnostic.exists():
         raise Exception("No existe una ayuda diagnostica con ese id")
    order = models.Order.objects.filter(id=order_id)
    if not order.exists():
         raise Exception("No existe una orden con ese id")
    if not specialist_id  is None:
        diagnosticHelp = models.Specialist.objects.filter(id=specialist_id)
        if not diagnosticHelp:
           raise Exception("No existe un especialista con ese id")
    lastItemM = models.OrderMedicine.objects.filter(order_id=order_id).order_by('-itemMedicine').first()
    lastItemP = models.OrderProcedure.objects.filter(order_id=order_id).order_by('-itemProcedure').first()
    lastItemD = models.OrderDiagnosticHelp.objects.filter(order_id=order_id).order_by('-itemDiagnosticHelp').first()  

    if lastItemD:
        nextItemD = lastItemD.itemDiagnosticHelp + 1
    else:
        nextItemD = 1
    if lastItemP and lastItemP.itemProcedure == nextItemD:
        nextItemD += 1
    if lastItemM and lastItemM.itemMedicine == nextItemD:
        nextItemD += 1                  
    diagnostic = models.OrderDiagnosticHelp(itemDiagnosticHelp=nextItemD, quantity=quantity, requiresSpecialistD=requiresSpecialistD,diagnosticHelp_id=diagnosticHelp_id,order_id=order_id,specialist_id=specialist_id)
    diagnostic.save()

#------- historia clinica

def createHistoryClinic(patient_id, date, doctor, reason, symptoms, diagnosis, order_id):
    patientHistory = collection.find_one({"_id": patient_id})
    
    if not patientHistory:
        raise Exception("El paciente no tiene historia clínica")

    order = models.Order.objects.filter(id=order_id).first()
    if not order:
        raise Exception("No existe una orden con ese id")
        
    # medicinas 
    medicines = models.OrderMedicine.objects.filter(order_id=order_id)
    medicineList = []
    for medicine in medicines:
        medicineId = models.Medicine.objects.filter(id=medicine.medicine_id).first()
        medicineInfo = {"id": medicine.id,"itemMedicine": medicine.itemMedicine,"medicineDose": medicine.medicineDose,"durationMedication": medicine.durationMedication,
                        "medicine_id": {"id": medicineId.id,"medicineName": medicineId.medicineName,"medicineQuantity": medicineId.medicineQuantity,"medicineCost": medicineId.medicineCost}}
        medicineList.append(medicineInfo)
        
    #procedimientos rent please
    procedures = models.OrderProcedure.objects.filter(order_id=order_id)
    procedureList = []
    for procedure in procedures:
        procedureId= models.Procedure.objects.filter(id=procedure.procedure_id).first()
        specialistId= models.Specialist.objects.filter(id=procedure.specialist_id).first() 
        procedureInfo = {"id": procedure.id,"itemProcedure": procedure.itemProcedure,"numberRepeated": procedure.numberRepeated,"frequencyRepeated": procedure.frequencyRepeated,"requiresSpecialistP": procedure.requiresSpecialistP,
                        "procedure_id": {"id":procedureId.id,"procedureName":procedureId.procedureName,"procedureCost":procedureId.procedureCost},
                        "specialist_id":{"id":specialistId.id if specialistId else None ,"nameSpecialist": specialistId.nameSpecialist if specialistId else None}}
        procedureList.append(procedureInfo)
        
    #ayuda 
    diagnostics = models.OrderDiagnosticHelp.objects.filter(order_id=order_id)
    diagnosticList = []
    for diagnostic in diagnostics:
        diagnosticId= models.DiagnosticHelp.objects.filter(id=diagnostic.diagnosticHelp_id).first()
        specialistId= models.Specialist.objects.filter(id=diagnostic.specialist_id).first()         
        diagnosticInfo = {"id": diagnostic.id,"itemDiagnosticHelp": diagnostic.itemDiagnosticHelp,"quantity": diagnostic.quantity,"requiresSpecialistD": diagnostic.requiresSpecialistD,
                        "diagnosticHelp_id":  {"id":diagnosticId.id,"diagnosticName":diagnosticId.diagnosticName,"diagnosticCost":diagnosticId.diagnosticCost},
                        "specialist_id":{"id":specialistId.id if specialistId else None ,"nameSpecialist": specialistId.nameSpecialist if specialistId else None}}
        diagnosticList.append(diagnosticInfo)

    orderInfo = {"id": order.id,"date": order.date,"patient_id": order.patient.id,"doctor_id": order.doctor.id,"medicines": medicineList,"procedures": procedureList,"diagnostics": diagnosticList}

    newHistory = {"date": date,"doctor": doctor,"reason": reason,"symptoms": symptoms,"diagnosis": diagnosis,"order": orderInfo}

    histories = patientHistory.get("historias", {})
    if not isinstance(histories, list):
        histories = [histories]
    histories.append(newHistory)

    collection.update_one({"_id": patient_id}, {"$set": {"historias": histories}})

    return newHistory


#factura

def createBilling(patient_id, doctor_id, order_id):

    dateToday = date.today()    
    patient = models.Patient.objects.get(id=patient_id)
    if not patient:
        raise Exception("No existe un paciente con esa cédula registrada")
    
    birth = patient.birth
    birth = datetime.strptime(birth, "%d/%m/%Y")
 
    today = datetime.now()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day)) 

    doctor = models.Employer.objects.get(id=doctor_id, role="doctor")

    policy = models.Policy.objects.get(patient_id=patient_id)

    order = models.Order.objects.get(id=order_id, patient_id=patient_id)
    
    orderMedicines = models.OrderMedicine.objects.filter(order_id=order_id)
    
    totalCost = 0

    for orderMedicine in orderMedicines:
        medicine = models.Medicine.objects.get(id=orderMedicine.medicine_id)
        totalCost += medicine.medicineCost

    orderProcedures = models.OrderProcedure.objects.filter(order_id=order_id)

    for orderProcedure in orderProcedures:
        procedure = models.Procedure.objects.get(id=orderProcedure.procedure_id)
        totalCost += procedure.procedureCost 
    orderDiagnosticHelps = models.OrderDiagnosticHelp.objects.filter(order_id=order_id)

    for orderDiagnosticHelp in orderDiagnosticHelps:
        diagnosticHelp = models.DiagnosticHelp.objects.get(id=orderDiagnosticHelp.diagnosticHelp_id)
        totalCost += diagnosticHelp.diagnosticCost       

    copay = 50000

    if policy.statePolicy == "Activa":
        year=dateToday.year
        billings = models.Billing.objects.filter(patient_id=patient_id, date__year=year)
        totalCopayYear = sum(b.cost for b in billings)
        if totalCopayYear > 1000000:
            totalPay = 0
        else:       
            totalPay = copay
            totalCost = totalCost + copay
    elif policy.statePolicy == "Inactiva":

        totalPay = totalCost
    
  
    billing = models.Billing()
    billing.date = dateToday

    billing.patient = patient
    billing.patientName = patient.name
    billing.age = age
    
    billing.doctor = doctor
    billing.doctorName = doctor.name
    billing.policy = policy
    billing.policyNumber = policy.policyNumber
    billing.termPolicy = policy.termPolicy
    
    billing.order = order

    billing.cost = totalCost
    billing.totalPay = totalPay
    billing.save()



