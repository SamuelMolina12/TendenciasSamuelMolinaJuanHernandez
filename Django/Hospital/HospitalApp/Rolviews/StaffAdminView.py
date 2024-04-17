
import HospitalApp.validators.StaffAdminValidator as staffAdminValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json







def getPatient(self, request, id=None):
    try:
        patients = [staffAdminValidator.getPatient(id)] if id else staffAdminValidator.getPatients()
        patients = [{"id": patient.id, "name": patient.name,"mail":patient.mail, "genre": patient.genre,"telephone": patient.telephone,"birth":patient.birth,"address":patient.address} for patient in patients]
        if not id is None:
            emergencies = staffAdminValidator.getEmergencyContact(id)
            if emergencies:       
                for patient, emergency in zip(patients, emergencies):
                    patient["emergencyContact"] = {"emergencyContactId": emergency.id,"nameC": emergency.name,"relationship": emergency.relationship,"telephoneC": emergency.telephone,}
            policies = staffAdminValidator.getPolicy(id)
            if policies:       
                for patient, policy in zip(patients, policies):
                    patient["Policy"] = {"Policy": policy.id,"insuranceCompany": policy.insuranceCompany,"policyNumber": policy.policyNumber,"statePolicy": policy.statePolicy,"termPolicy": policy.termPolicy}
                                

        status = 204 if patients else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(patients, status=status, safe=False)
    

def createPatient(self,request):
    body = json.loads(request.body)
    try:
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
    body = json.loads(request.body)
    
    try:
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
        staffAdminValidator.deletePatient(id) 
        message = "Paciente eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)
