import HospitalApp.validators.InventoryValidator as infoValidator
import HospitalApp.validators.EmployerValidator as AdminValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json

def validateRole(role,validateRoles):
    if role not in validateRoles:
        raise Exception("rol no valido")


# medicina--
def getMedicine(self, request, id=None):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])       
        medicines = [infoValidator.getMedicine(id)] if id else infoValidator.getMedicines()
        medicines = [{"id": medicine.id, "medicineName": medicine.medicineName,"medicineCost":medicine.medicineCost,"medicineQuantity":medicine.medicineQuantity} for medicine in medicines]
        if medicines:
            status = 200
        else:
            status = 404    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(medicines, status=status, safe=False)
    
def createMedicine(self,request):
    try: 
        body=json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
        infoValidator.createMedicine(body["medicineName"],body["medicineCost"],body["medicineQuantity"])
        message="se ha creado la medicina exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)  

def updateMedicine(self, request, id):
    try:
        body=json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])         
        infoValidator.updateMedicine(id, body["medicineName"], body["medicineCost"], body["medicineQuantity"])
        message = "Medicina actualizada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status) 

def deleteMedicine(self, request, id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
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
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])         
        procedures = [infoValidator.getProcedure(id)] if id else infoValidator.getProcedures()
        procedures = [{"id": procedure.id, "procedureName": procedure.procedureName,"procedureCost":procedure.procedureCost} for procedure in procedures]
        if procedures:
            status = 200
        else:
            status = 404    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(procedures, status=status, safe=False)

def createProcedure(self,request):
    
    try:
        body=json.loads(request.body)
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])          
        infoValidator.createProcedure(body["procedureName"],body["procedureCost"])
        message="se ha creado el procedimiento exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)

def updateProcedure(self, request, id): 
    
    try:
        body = json.loads(request.body)
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
        infoValidator.updateProcedure(id,body["procedureName"],body["procedureCost"])
        message = "procedimiento actualizado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)


def deleteProcedure(self, request, id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])         
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
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
        diagnoses = [infoValidator.getDiagnosticHelp(id)] if id else infoValidator.getDiagnosticaids()
        diagnoses = [{"id": diagnostic.id, "diagnosticName": diagnostic.diagnosticName,"diagnosticCost": diagnostic.diagnosticCost} for diagnostic in diagnoses]
        if diagnoses:
            status = 200
        else:
            status = 404    
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(diagnoses, status=status, safe=False)
    

def createDiagnosticHelp(self,request):
    
    try:
        body=json.loads(request.body)
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])         
        infoValidator.createDiagnosticHelp(body["diagnosticName"],body["diagnosticCost"])
        message="se ha creado la ayuda diagnostica exitosamente"
        status=204
    except Exception as error:
        message=str(error)
        status=400
    response = {"message":message}
    return JsonResponse(response,status=status)    

def updateDiagnosticHelp(self, request, id):  
    try:
        body = json.loads(request.body)    
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
        infoValidator.updateDiagnosticHelp(id,body["diagnosticName"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialist_id"])
        message = "Ayuda Diagnstica actualizada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)



def deleteDiagnosticHelp(self, request, id):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["Soporte de informacion"])        
        infoValidator.deleteDiagnosticHelp(id)
        message = "ayuda diagnostica eliminada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status) 





