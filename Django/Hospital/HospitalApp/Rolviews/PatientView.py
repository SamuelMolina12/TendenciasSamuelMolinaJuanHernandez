
import HospitalApp.validators.PatientValidator as staffAdminValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
import HospitalApp.validators.EmployerValidator as AdminValidator

def validateRole(role,validateRoles):
    if role not in validateRoles:
        raise Exception("rol no valido")



def getPatient(self, request, id=None):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
 
        # validateRole(role,["Personal Administrativo","Doctor","Enfermera"])         
        patients = [staffAdminValidator.getPatient(id)] if id else staffAdminValidator.getPatients()
        patientsdata = [{"id": patient.id, "name": patient.name,"mail":patient.mail, "genre": patient.genre,"telephone": patient.telephone,"birth":patient.birth,"address":patient.address} for patient in patients]
    
        if not id is None:
            emergencies = staffAdminValidator.getEmergencyContact(id)
            if emergencies:       
                for patient, emergency in zip(patientsdata, emergencies):
                    patient["emergencyContact"] = {"emergencyContactId": emergency.id,"nameC": emergency.name,"relationship": emergency.relationship,"telephoneC": emergency.telephone}
                
            policies = staffAdminValidator.getPolicy(id)
            if policies:       
                for patient, policy in zip(patientsdata, policies):
                    patient["Policy"] = {"Policy": policy.id,"insuranceCompany": policy.insuranceCompany,"policyNumber": policy.policyNumber,"statePolicy": policy.statePolicy,"termPolicy": policy.termPolicy}
                
 
            
        if patients:
            status = 200
        else:
            status = 404    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse({"patients": patientsdata}, status=status, safe=False)
    

def createPatient(self,request):

    try:
        body = json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Personal Administrativo"])         
        staffAdminValidator.createPatient(body["id"],body["name"],body["mail"],body["genre"],body["telephone"],body["birth"],body["address"])
        staffAdminValidator.createPolicy(body["Policy"]["insuranceCompany"],body["Policy"]["policyNumber"],body["Policy"]["statePolicy"],body["Policy"]["termPolicy"],body["id"])
        staffAdminValidator.createEmergencyContact(body["emergencyContact"]["nameC"],body["emergencyContact"]["relationship"],body["emergencyContact"]["telephoneC"],body["id"])
        message = "Se ha creado el paciente exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)



    

def updatePatient(self, request, id):
    try:
        body = json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["Personal Administrativo"])   
        staffAdminValidator.updatePatient(id, body["name"],body["mail"],body["genre"],body["telephone"],body["birth"],body["address"])
        staffAdminValidator.updatePolicy(body["Policy"]["insuranceCompany"],body["Policy"]["policyNumber"],body["Policy"]["statePolicy"],body["Policy"]["termPolicy"],id)
        staffAdminValidator.updateEmergencyContact(body["emergencyContact"]["nameC"],body["emergencyContact"]["relationship"],body["emergencyContact"]["telephoneC"],id)            
        message = "Paciente actualizado exitosamente" 
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def deletePatient(self, request, id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["Personal Administrativo"])          
        staffAdminValidator.deletePatient(id) 
        message = "Paciente eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)


def getClinicalAppointment(self, request, id=None):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role = sesion.user.role
        # validateRole(role, ["Personal Administrativo"]) 
        if id:
            appointments = staffAdminValidator.getClinicalAppointment(id)
        else:
            appointments = staffAdminValidator.getAllClinicalAppointments()
        
        clinicalAppointments = []
        for appointment in appointments:
            appointmentDict = {
                "id": appointment.id,
                "date": appointment.date,
                "hour": appointment.hour,
                "doctor": appointment.doctor,
                "appointmentType": appointment.appointmentType,
                "patientId": appointment.patient.id
            }
            clinicalAppointments.append(appointmentDict)
        
        if clinicalAppointments:
            status = 200
        else:
            status = 404
    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(clinicalAppointments, status=status, safe=False)
    

def createClinicalAppointment(self,request): 
    try:
        body=json.loads(request.body) 
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["Personal Administrativo"])           
        staffAdminValidator.createClinicalAppointment(body["date"],body["hour"],body["doctor"],body["appointmentType"],body["patientId"])
        message="se ha creado la cita exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)

def deleteClinicalAppointment(self,request,id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["Personal Administrativo"])        
        staffAdminValidator.deleteClinicalAppointment(id)
        message = "Cita medica eliminada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)
#-----
#---- ordenes
def getOrder(self, request, id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])        
        order = staffAdminValidator.getOrder(id)
        orderData = {"id": order.id,"date": order.date,"doctor_id": order.doctor_id,"patient_id": order.patient_id
        }

        medicines = staffAdminValidator.getOrderMedicine(id)
        medicinesList = []
        if medicines:
            for medicine in medicines:
                medicineList = {"id": medicine.id,"itemMedicine": medicine.itemMedicine,"medicineDose": medicine.medicineDose,"durationMedication": medicine.durationMedication,"medicine_id": medicine.medicine_id,"order_id": medicine.order_id}
                medicinesList.append(medicineList)
        procedures = staffAdminValidator.getOrderProcedure(id)
        proceduresList = []
        if procedures:
            for procedure in procedures:
                procedureList = {"id": procedure.id,"itemProcedure": procedure.itemProcedure,"numberRepeated": procedure.numberRepeated,"frequencyRepeated": procedure.frequencyRepeated,"requiresSpecialistP": procedure.requiresSpecialistP,"order_id": procedure.order_id,"specialist_id": procedure.specialist_id}
                proceduresList.append(procedureList)

        diagnostics = staffAdminValidator.getOrderDiagnosticHelp(id)
        diagnosticsList = []
        if diagnostics:
            for diagnostic in diagnostics:
                diagnosticList = {"id": diagnostic.id,"itemDiagnosticHelp": diagnostic.itemDiagnosticHelp,"quantity": diagnostic.quantity,"requiresSpecialistD": diagnostic.requiresSpecialistD,"order_id": diagnostic.order_id,"specialist_id": diagnostic.specialist_id}
                diagnosticsList.append(diagnosticList)   

        response = {"order": orderData, "medicines": medicinesList,"procedures":proceduresList,"diagnosticHelp":diagnosticsList}
        status = 200 if order else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
    return JsonResponse(response, status=status)

    


def createOrder(self,request):
    try: 
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])          
        body=json.loads(request.body)    
        staffAdminValidator.createOrder(body["patient"],body["doctor"])
        message="se ha creado la orden exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)




   
    #ordenMedicina
def createOrderMedicine(self,request):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])       
        body=json.loads(request.body)    
        staffAdminValidator.createOrderMedicine(body["medicineDose"],body["durationMedication"],body["medicine_id"],body["order_id"])
        message="se ha creado la orden de la medicina exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)
    #ordenProcedimiento
def createOrderProcedure(self,request):
    try: 
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])          
        body=json.loads(request.body)    
        staffAdminValidator.createOrderProcedure(body["numberRepeated"],body["frequencyRepeated"],body["requiresSpecialistP"],body["order_id"],body["procedure_id"],body["specialist_id"])
        message="se ha creado la orden del Procedimiento exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)
    #ordenAyuda
def createOrderDiagnosticHelp(self,request):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])           
        body=json.loads(request.body)    
        staffAdminValidator.createOrderDiagnosticHelp(body["quantity"],body["requiresSpecialistD"],body["diagnosticHelp_id"],body["order_id"],body["specialist_id"])
        message="se ha creado la orden del Procedimiento exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)

#---- Historia clinica

def getHistoryClinic(self, request, id):
    try:
        token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])          
        historyClinic = staffAdminValidator.getHistoryClinic(id)
        status = 200
        response = {"id": historyClinic["_id"],"historias": historyClinic["historias"]}
    except Exception as error:
        status = 400
        response = {"message": str(error)}
        
    return JsonResponse(response, status=status)



def createHistoryClinic(self,request):
    try:
        body=json.loads(request.body)        
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["doctor"])           
        staffAdminValidator.createHistoryClinic(body["patient_id"],body["doctor"],body["reason"],body["symptoms"],body["diagnosis"],body["order"])
        message="se ha creado la historia clinica exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)


#---- Historia de visitas

def getHistoryVisits(self, request, id):
    try:
       
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["enfermera"])        
        historyVisits = staffAdminValidator.getHistoryVisits(id)
        status = 200
        response = {"id": historyVisits["_id"],"historias": historyVisits["historias"]}
    except Exception as error:
        status = 400
        response = {"message": str(error)}
        
    return JsonResponse(response, status=status)

def createHistoryVisits(self,request):
    try:
        body=json.loads(request.body)
       
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["enfermera"])         
        staffAdminValidator.createHistoryVisits(body["patient"],body["doctor"],body["bloodPressure"],body["temperature"],body["pulse"],body["bloodOxygeLevel"],body["order"],body["items"])
        message="se ha creado la historia de visita exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)

#facturacion
def createBilling(self,request):

    try: 
        body=json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["enfermera"])           
        staffAdminValidator.createBilling(body["patient_id"],body["doctor_id"],body["order_id"])
        message="se ha creado la factura exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)


def getBilling(self,request,id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role 
        # validateRole(role,["Personal Administrativo"])           
        billings = staffAdminValidator.getBilling(id)
        billingsData = []
        for billing in billings:
            billingDict = {"id": billing.id,"doctorName":billing.doctorName,"policyNumber":billing.policyNumber,"termPolicy":billing.termPolicy,"cost":billing.cost,"totalPay":billing.totalPay,"date":billing.date,"patientId": billing.patient.id }
            billingsData.append(billingDict)
        if billings:
            status = 200
        else:
            status = 404    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(billingsData, status=status, safe=False)
  
  



