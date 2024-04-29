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
        
def createOrderMedicine(itemMedicine,medicineDose,durationMedication,medicine_id,order_id):

    medicine = models.Medicine.objects.filter(id=medicine_id)
    if not medicine.exists():
         raise Exception("No existe una medicina con ese id")
    order = models.Order.objects.filter(id=order_id)
    if not order.exists():
         raise Exception("No existe una orden con ese id")
          
    medicine = models.OrderMedicine(itemMedicine=itemMedicine, medicineDose=medicineDose,durationMedication=durationMedication, medicine_id=medicine_id,order_id=order_id)
    medicine.save()


        
    #orden procedimiento
def getOrderProcedure(id):
    procedure = models.OrderProcedure.objects.filter(order_id=id)
    if procedure:
        return procedure
    else:
        raise Exception("No hay un procedimiento asociado a esa orden")

def createOrderProcedure(itemProcedure,numberRepeated,frequencyRepeated,requiresSpecialistP,order_id,procedure_id,specialist_id):

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
                  
    prcedure = models.OrderProcedure(itemProcedure=itemProcedure, numberRepeated=numberRepeated, frequencyRepeated=frequencyRepeated,requiresSpecialistP=requiresSpecialistP,order_id=order_id,procedure_id=procedure_id,specialist_id=specialist_id)
    prcedure.save()
    
    #orden ayuda diagnostica

def getOrderDiagnosticHelp(id):
    diagnostic = models.OrderDiagnosticHelp.objects.filter(order_id=id)
    if diagnostic:
        return diagnostic
    else:
        raise Exception("No hay un procedimiento asociado a esa orden")

def createOrderDiagnosticHelp(itemDiagnosticHelp,quantity,requiresSpecialistD,diagnosticHelp_id,order_id,specialist_id):

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
                  
    diagnostic = models.OrderDiagnosticHelp(itemDiagnosticHelp=itemDiagnosticHelp, quantity=quantity, requiresSpecialistD=requiresSpecialistD,diagnosticHelp_id=diagnosticHelp_id,order_id=order_id,specialist_id=specialist_id)
    diagnostic.save()

#------- historia clinica

def createHistoryClinic(patient_id, date, doctor, reason, symptoms, diagnosis, order_id):
    patientHistory = collection.find_one({"_id": patient_id})
    
    if not patientHistory:
        raise Exception("El paciente no tiene historia clínica")

    order = models.Order.objects.filter(id=order_id).first()
    if not order:
        raise Exception("No existe una orden con ese id")
        

    order = {"id": order.id,"date": order.date,"patient_id": order.patient.id,"doctor_id": order.doctor.id}
    
    newHistory = {"date": date,"doctor": doctor,"reason": reason,"symptoms": symptoms,"diagnosis": diagnosis,"order": order}

    histories = patientHistory.get("historias", [])
    if not isinstance(histories, list):
        histories = [histories]
    histories.append(newHistory)

    collection.update_one({"_id": patient_id}, {"$set": {"historias": histories}})

    return newHistory







