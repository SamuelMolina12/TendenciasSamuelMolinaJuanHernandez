from django.shortcuts import render
from django.views import View
import HospitalApp.validators.AdminTypeValidator as AdminValidator
import HospitalApp.validators.StaffAdminValidator as StaffAdminValidator
import HospitalApp.validators.InfoSupportValidator as InfoValidator
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json



class EmployerView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        try:
            employers = [AdminValidator.getUser(id)] if id else AdminValidator.getUsers()
            employers = [{"id": employer.id, "name": employer.name,"genre":employer.genre,"mail":employer.mail, "telephone": employer.telephone,
            "birth":employer.birth, "address":employer.address, "role":employer.role, "userName":employer.userName,"password":employer.password} for employer in employers]
            status = 204 if employers else 404
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
            return JsonResponse(response, status=status)
        else:
            return JsonResponse(employers, status=status, safe=False)


        
 
    def post(self,request):
        body=json.loads(request.body)
        try:
            AdminValidator.createUser(body["name"],body["id"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"],body["role"],body["userName"],body["password"])
            message="se ha creado el Empleado exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 

 
    def put(self, request, id):
        if id:
            message, status = self.putUser(request, id)
        
        response = {"message": message}
        return JsonResponse(response, status=status)

    def putUser(self,request, id):
        body = json.loads(request.body)
        try:
            AdminValidator.updateUser(id, body["name"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"],body["role"],body["userName"],body["password"])
            message = "Empleado actualizado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        return message, status
    def delete(self, request, id):
        try:
            AdminValidator.deleteUser(id)
            message = "Empleado eliminado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)    
  

#Paciente---------------------
class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        try:
            patients = [StaffAdminValidator.getPatient(id)] if id else StaffAdminValidator.getPatients()
            patients = [{"id": patient.id, "name": patient.name,"mail":patient.mail, "genre": patient.genre,"telephone": patient.telephone,
            "birth":patient.birth} for patient in patients]
            if not id is None:
                emergencies = StaffAdminValidator.getEmergencyContact(id)
                if emergencies:       
                    for patient, emergency in zip(patients, emergencies):
                        patient["emergencyContact"] = {"emergencyContactId": emergency.id,"nameC": emergency.name,"relationship": emergency.relationship,"telephoneC": emergency.telephone,}
                policies = StaffAdminValidator.getPolicy(id)
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
 
    def post(self, request):
        body = json.loads(request.body)
        try:
            StaffAdminValidator.createPatient(body["id"],body["name"],body["mail"],body["genre"],body["telephone"],body["birth"],body["address"])
            StaffAdminValidator.createPolicy(body["insuranceCompany"],body["policyNumber"],body["statePolicy"],body["termPolicy"],body["id"])
            StaffAdminValidator.createEmergencyContact(body["nameC"],body["relationship"],body["telephoneC"],body["id"])
            message = "Se ha creado el paciente exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
 
    def put(self, request, id):
        if id:
            message, status = self.putPatient(request, id)
        
        response = {"message": message}
        return JsonResponse(response, status=status)

    def putPatient(self,request, id):
        body = json.loads(request.body)
        try:
            StaffAdminValidator.updatePatient(id, body["name"],body["genre"],body["mail"],body["telephone"],body["birth"],body["address"],body["role"],body["userName"],body["password"])
            message = "Empleado actualizado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        return message, status
 
    def delete(self, request, id):
        try:
            StaffAdminValidator.deletePatient(id) 
            message = "Paciente eliminado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)


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
#-------------------------
#inventario ------------

      #medicina
class MedicineView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        try:
            medicines = [InfoValidator.getMedicine(id)] if id else InfoValidator.getMedicines()
            medicines = [{"id": medicine.id, "medicineName": medicine.medicineName,"medicineDose":medicine.medicineDose,"durationMedication": medicine.durationMedication,
            "medicineCost":medicine.medicineCost} for medicine in medicines]
            status = 204 if medicines else 404
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
            return JsonResponse(response, status=status)
        else:
            return JsonResponse(medicines, status=status, safe=False)
 
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
 
    def put(self, request, id):
        if id:
            message, status = self.UpdateMedicine(request, id)
        response = {"message": message}
        return JsonResponse(response, status=status)

    def UpdateMedicine(self,request, id):
        body = json.loads(request.body)
        try:
            InfoValidator.updateMedicine(id,body["medicineName"],body["medicineDose"],body["durationMedication"],body["medicineCost"])
            message = "Medicina actualizada exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        return message, status
 
    def delete(self, request, id):
        try:
            InfoValidator.deleteMedicine(id)
            message = "Medicina Eliminada exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)


         ##Procedimiento
class ProcedureView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        try:
            procedures = [InfoValidator.getProcedure(id)] if id else InfoValidator.getProcedures()
            procedures = [{"id": procedure.id, "procedureName": procedure.procedureName,"numberRepeated":procedure.numberRepeated,"frequencyRepeated": procedure.frequencyRepeated,
            "procedureCost":procedure.procedureCost,"requiresSpecialistP":procedure.requiresSpecialistP,"specialistId":procedure.specialistId} for procedure in procedures]
            status = 204 if procedures else 404
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
            return JsonResponse(response, status=status)
        else:
            return JsonResponse(procedures, status=status, safe=False)
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            InfoValidator.createProcedure(body["procedureName"],body["numberRepeated"],body["frequencyRepeated"],body["procedureCost"],body["requiresSpecialistP"],body["specialistId"])
            message="se ha creado el procedimiento exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self, request, id):
        if id:
            message, status = self.UpdateProcedure(request, id)
        response = {"message": message}
        return JsonResponse(response, status=status)

    def UpdateProcedure(self,request, id):
        body = json.loads(request.body)
        try:
            InfoValidator.updateProcedure(id,body["procedureName"],body["numberRepeated"],body["frequencyRepeated"],body["procedureCost"],body["requiresSpecialistP"],body["specialistId"])
            message = "procedimiento actualizado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        return message, status
 
    def delete(self, request, id):
        try:
            InfoValidator.deleteProcedure(id)
            message = "Procedimiento eliminado exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)

      #Ayudas Diagnosticas
class DiagnosticHelpView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        try:
            diagnoses = [InfoValidator.getDiagnosticHelp(id)] if id else InfoValidator.getDiagnosticaids()
            diagnoses = [{"id": diagnostic.id, "diagnosticName": diagnostic.diagnosticName,"quantity":diagnostic.quantity,"diagnosticCost": diagnostic.diagnosticCost,
            "requiresSpecialistD":diagnostic.requiresSpecialistD,"specialistId":diagnostic.specialistId} for diagnostic in diagnoses]
            status = 204 if diagnoses else 404
        except Exception as error:
            message = str(error)
            status = 400
            response = {"message": message}
            return JsonResponse(response, status=status)
        else:
            return JsonResponse(diagnoses, status=status, safe=False)
 
    def post(self,request):
        body=json.loads(request.body)
        try: 
            InfoValidator.createDiagnosticHelp(body["diagnosticName"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialistId"])
            message="se ha creado la ayuda diagnostica exitosamente"
            status=204
        except Exception as error:
            message=str(error)
            status=400
        response = {"message":message}
        return JsonResponse(response,status=status)
 
    def put(self, request, id):
        if id:
            message, status = self.UpdateDiagnosticHelp(request, id)
        response = {"message": message}
        return JsonResponse(response, status=status)

    def UpdateDiagnosticHelp(self,request, id):
        body = json.loads(request.body)
        try:
            InfoValidator.updateDiagnosticHelp(id,body["diagnosticName"],body["quantity"],body["diagnosticCost"],body["requiresSpecialistD"],body["specialistId"])
            message = "Ayuda Diagnstica actualizada exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        return message, status
 
    def delete(self, request, id):
        try:
            InfoValidator.deleteDiagnosticHelp(id)
            message = "ayuda diagnostica eliminada exitosamente"
            status = 204
        except Exception as error:
            message = str(error)
            status = 400
        
        response = {"message": message}
        return JsonResponse(response, status=status)
#---------






#Funciones 

