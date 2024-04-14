from django.shortcuts import render
from django.views import View
import HospitalApp.validators.PersonTypeValidator as PersonValidator
import HospitalApp.validators.StaffAdminValidator as StaffAdminValidator
import HospitalApp.validators.InfoSupportTypeValidator as InfoValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json



class EmployerView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        employers = [PersonValidator.getUser(id)] if id else PersonValidator.getUsers()
        status = 200 if employers else 404
        employers = [{
            "id": employer.id, 
            "name": employer.name, 
            "genre": employer.genre, 
            "mail": employer.mail, 
            "telephone": employer.telephone,
            "birth": employer.birth, 
            "address": employer.address, 
            "role": employer.role, 
            "userName": employer.userName,
            "password": employer.password
            } for employer in employers]
    
        return JsonResponse(employers, status=status, safe=False)

        
 
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
 
    def put(self,request, id):  # Agrega el parámetro 'id' aquí
        if id:
            body = json.loads(request.body)
            try:
                PersonValidator.updateUser(
                    id,  # Pasa el 'id' aquí
                    body["name"],
                    body["genre"],
                    body["mail"],
                    body["telephone"],
                    body["birth"],
                    body["address"],
                    body["role"],
                    body["userName"],
                    body["password"]
                )
                message = "Empleado actualizado exitosamente"
                status = 204
            except Exception as error:
                message = str(error)
                status = 400
        else:
            message = "Se requiere el parámetro 'id' para actualizar un empleado"
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)


 
    def delete(self, request, id):
        try:
            PersonValidator.deleteUser(id)
            message = "Empleado eliminado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)

class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self, request):
        body = json.loads(request.body)
        try:
            StaffAdminValidator.createPatient(body["id"],body["name"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"])
            StaffAdminValidator.createPolicy(body["insuranceCompany"],body["policyNumber"],body["statePolicy"],body["termPolicy"],body["id"])
            StaffAdminValidator.createEmergencyContact(body["nameC"],body["relationship"],body["telephoneC"],body["id"])
            message = "Se ha creado el paciente exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
 
    def put(self,request):
        pass
 
    def delete(self,request):
        pass


class ClinicalAppointmentView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            StaffAdminValidator.createClinicalAppointment(body["date"],body["hour"],body["doctor"],body["appointmentType"],body["patientId"])
            message="se ha creado la cita exitosamente"
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




# class EmergencyContactView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args: any, **kwargs: any):
#         return super().dispatch(request, *args, **kwargs)
   
#     def get(self,request):
#         pass
 
#     def post(self,request):
#         body=json.loads(request.body)
#         try:
#             StaffAdminValidator.createEmergencyContact(body["name"],body["relationship"],body["telephone"],body["patient_id"])
#             message="se ha creado el Contacto de emergencia exitosamente"
#             status=204
#         except Exception as error:
#             message=str(error)
#             status=400
#         response = {"message":message}
#         return JsonResponse(response,status=status)
 
#     def put(self,request):
#         pass
 
#     def delete(self,request):
#         pass
    
# class PolicyView(View):
#     @method_decorator(csrf_exempt)
#     def dispatch(self, request, *args: any, **kwargs: any):
#         return super().dispatch(request, *args, **kwargs)
   
#     def get(self,request):
#         pass
 
#     def post(self,request):
#         body=json.loads(request.body)
#         try:
#             StaffAdminValidator.createPolicy(body["insuranceCompany"],body["policyNumber"],body["statePolicy"],body["termPolicy"],body["patient_id"])
#             message="se ha creado la poliza exitosamente"
#             status=204
#         except Exception as error:
#             message=str(error)
#             status=400
#         response = {"message":message}
#         return JsonResponse(response,status=status)
 
#     def put(self,request):
#         pass
 
#     def delete(self,request):
#         pass

#inventario ------------
class MedicineView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            InfoValidator.createMedicine(body["medicineName"],body["medicineDose"],body["durationMedication"],body["medicineCost"])
            message="se ha creado la medicina exitosamente"
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

class ProcedureView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            InfoValidator.createProcedure(body["nameProcedure"],body["numberRepeated"],body["frequencyRepeated"],body["procedureCost"],body["requiresSpecialistP"],body["specialistId"])
            message="se ha creado el procedimiento exitosamente"
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


class DiagnosticHelpView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request):
        pass
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            InfoValidator.createDiagnosticHelp(body["nameDiagnostic"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialistId"])
            message="se ha creado la ayuda diagnostica exitosamente"
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
#---------