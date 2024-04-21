import HospitalApp.validators.InventoryValidator as infoValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json




# medicina--
def getMedicine(self, request, id=None):
    try:
        medicines = [infoValidator.getMedicine(id)] if id else infoValidator.getMedicines()
        medicines = [{"id": medicine.id, "medicineName": medicine.medicineName,"medicineDose":medicine.medicineDose,"durationMedication": medicine.durationMedication,"medicineCost":medicine.medicineCost} for medicine in medicines]
        status = 204 if medicines else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(medicines, status=status, safe=False)
    
def createMedicine(self,request):
    body=json.loads(request.body)
    try: 
        infoValidator.createMedicine(body["medicineName"],body["medicineDose"],body["durationMedication"],body["medicineCost"])
        message="se ha creado la medicina exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)  

def updateMedicine(self, request, id):
    body = json.loads(request.body)
    try:
        infoValidator.updateMedicine(id, body["medicineName"], body["medicineDose"], body["durationMedication"], body["medicineCost"])
        message = "Medicina actualizada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status) 

def deleteMedicine(self, request, id):
    try:
        infoValidator.deleteMedicine(id)
        message = "Medicina Eliminada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)


#---------

#Procedimientos
 
def getProcedure(self, request, id=None):
    try:
        procedures = [infoValidator.getProcedure(id)] if id else infoValidator.getProcedures()
        procedures = [{"id": procedure.id, "procedureName": procedure.procedureName,"numberRepeated":procedure.numberRepeated,"frequencyRepeated": procedure.frequencyRepeated,"procedureCost":procedure.procedureCost,"requiresSpecialistP":procedure.requiresSpecialistP,"specialist_id":procedure.specialist_id} for procedure in procedures]
        status = 204 if procedures else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(procedures, status=status, safe=False)

def createProcedure(self,request):
    body=json.loads(request.body)
    try: 
        infoValidator.createProcedure(body["procedureName"],body["numberRepeated"],body["frequencyRepeated"],body["procedureCost"],body["requiresSpecialistP"],body["specialist_id"])
        message="se ha creado el procedimiento exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)

def updateProcedure(self, request, id): 
    body = json.loads(request.body)
    try:
        infoValidator.updateProcedure(id,body["procedureName"],body["numberRepeated"],body["frequencyRepeated"],body["procedureCost"],body["requiresSpecialistP"],body["specialist_id"])
        message = "procedimiento actualizado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)


def deleteProcedure(self, request, id):
    try:
        infoValidator.deleteProcedure(id)
        message = "Procedimiento eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)

#----------------

#Ayudas diagnosticas
def getDiagnosticHelp(self, request, id=None):
    try:
        diagnoses = [infoValidator.getDiagnosticHelp(id)] if id else infoValidator.getDiagnosticaids()
        diagnoses = [{"id": diagnostic.id, "diagnosticName": diagnostic.diagnosticName,"quantity":diagnostic.quantity,"diagnosticCost": diagnostic.diagnosticCost,"requiresSpecialistD":diagnostic.requiresSpecialistD,"specialist_id":diagnostic.specialist_id} for diagnostic in diagnoses]
        status = 204 if diagnoses else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(diagnoses, status=status, safe=False)
    

def createDiagnosticHelp(self,request):
    body=json.loads(request.body)
    try: 
        infoValidator.createDiagnosticHelp(body["diagnosticName"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialist_id"])
        message="se ha creado la ayuda diagnostica exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)    

def updateDiagnosticHelp(self, request, id):
    body = json.loads(request.body)
    try:
        infoValidator.updateDiagnosticHelp(id,body["diagnosticName"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialist_id"])
        message = "Ayuda Diagnstica actualizada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)



def deleteDiagnosticHelp(self, request, id):
    try:
        infoValidator.deleteDiagnosticHelp(id)
        message = "ayuda diagnostica eliminada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)            