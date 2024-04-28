
import HospitalApp.validators.EmployerValidator as AdminValidator

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


def validateRole(role,validateRoles):
    if role not in validateRoles:
        raise Exception("rol no valido")




def getEmployers(self, request, id=None):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])        
        employers = [AdminValidator.getUser(id)] if id else AdminValidator.getUsers()
        employers = [{"id": employer.id, "name": employer.name,"genre":employer.genre,"mail":employer.mail, "telephone": employer.telephone,"birth":employer.birth, "address":employer.address, "role":employer.role, "userName":employer.userName,"password":employer.password} for employer in employers]
        status = 204 if employers else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(employers, status=status, safe=False)

def createEmployer(self, request):
    try:
        body = json.loads(request.body)        
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])         
        AdminValidator.createUser(body["name"], body["id"], body["genre"], body["mail"], body["telephone"], body["birth"], body["address"], body["role"], body["userName"], body["password"])
        message = "Se ha creado el Empleado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def updateEmployer(self, request, id):
    try:
        body = json.loads(request.body)        
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])
        AdminValidator.updateUser(id, body["name"], body["genre"], body["mail"], body["telephone"], body["birth"], body["address"], body["role"], body["userName"], body["password"])
        message = "Empleado actualizado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)

   

def deleteEmployer(self, request, id):
    try:
       
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])        
        AdminValidator.deleteUser(id)
        message = "Empleado eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status) 

#login



def postLogin(self,request):
    try:
        body=json.loads(request.body)
        session =AdminValidator.login(body["username"],body["password"])
        message="loguin exitoso"
        status=200
        response = {"message":message,"token":session.token}
    except Exception as error:
        message=str(error)
        status=400
        response = {"message":message}
    return JsonResponse(response,status=status)
    
def getLogin(self,request):
    try:
        token = request.META.get('HTTP_TOKEN')
        sesion = AdminValidator.getSession(token)
        role=sesion.user.role
        status=200
        message = "token encontrado"
        role=sesion.user.role
    except Exception as error:
        message = str(error)
        status = 400
        role=None
    response = {"message":message, "role": role}
    return JsonResponse(response,status=status)


#especialista  Specialist

def getSpecialists(self, request, id=None):
    try:
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])        
        Specialists = [AdminValidator.getSpecialist(id)] if id else AdminValidator.getSpecialists()
        Specialists = [{"id":  Specialist.id, "nameSpecialist":  Specialist.nameSpecialist} for  Specialist in  Specialists]
        status = 204 if  Specialists else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse( Specialists, status=status, safe=False)
    
def createSpecialist(self, request):
    try:
        body = json.loads(request.body)        
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])         
        AdminValidator.createSpecialist(body["nameSpecialist"])
        message = "Se ha creado el especialista exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def updateSpecialist(self, request, id):
    try:
        body = json.loads(request.body)        
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])
        AdminValidator.updateSpecialist(id, body["nameSpecialist"])
        message = "Especialista actualizado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)

def deleteSpecialist(self, request, id):
    try:
       
        # token = request.META.get('HTTP_TOKEN')
        # sesion = AdminValidator.getSession(token)
        # role=sesion.user.role
        # validateRole(role,["admin"])        
        AdminValidator.deleteSpecialist(id)
        message = "Especialista eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status) 