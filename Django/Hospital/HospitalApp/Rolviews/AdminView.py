
import HospitalApp.validators.AdminTypeValidator as AdminValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json





def getEmployers(self, request, id=None):
    try:
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
    body = json.loads(request.body)
    try:
        AdminValidator.createUser(body["name"], body["id"], body["genre"], body["mail"], body["telephone"], body["birth"], body["address"], body["role"], body["userName"], body["password"])
        message = "Se ha creado el Empleado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def updateEmployer(self, request, id):
    body = json.loads(request.body)
    try:
        AdminValidator.updateUser(id, body["name"], body["genre"], body["mail"], body["telephone"], body["birth"], body["address"], body["role"], body["userName"], body["password"])
        message = "Empleado actualizado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    return JsonResponse({"message": message}, status=status)

   

def deleteEmployer(self, request, id):
    try:
        AdminValidator.deleteUser(id)
        message = "Empleado eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
        
    response = {"message": message}
    return JsonResponse(response, status=status)      