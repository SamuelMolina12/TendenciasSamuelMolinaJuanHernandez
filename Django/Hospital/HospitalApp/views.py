from django.shortcuts import render
from django.views import View
import HospitalApp.validators.PersonTypeValidator as PersonValidator
import HospitalApp.validators.StaffAdminValidator as StaffAdminValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json



class EmployerView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try:
            PersonValidator.createUser(body["name"],body["id"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"],body["role"],body["userName"],body["password"])
            message="se ha creado el Empleado exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self,request):
        pass
 
    def delete(self,request):
        pass


class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try:
            StaffAdminValidator.createPatient(body["id"],body["name"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"])
            message="se ha creado el Paciente exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self,request):
        pass
 
    def delete(self,request):
        pass

class EmergencyContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try:
            StaffAdminValidator.createEmergencyContact(body["name"],body["relationship"],body["telephone"],body["patient_id"])
            message="se ha creado el Contacto de emergencia exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self,request):
        pass
 
    def delete(self,request):
        pass
    
class PolicyView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try:
            StaffAdminValidator.createPolicy(body["insuranceCompany"],body["policyNumber"],body["statePolicy"],body["termPolicy"],body["patient_id"])
            message="se ha creado la poliza exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self,request):
        pass
 
    def delete(self,request):
        pass        