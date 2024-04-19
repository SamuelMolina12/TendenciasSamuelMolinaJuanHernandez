from django.shortcuts import render
from django.views import View

import HospitalApp.validators.InfoSupportValidator as InfoValidator
import HospitalApp.validators.NurseValidator as nurseValidator
import HospitalApp.validators.AdminTypeValidator as AdminValidator
import HospitalApp.validators.StaffAdminValidator as staffAdminValidator


import HospitalApp.Rolviews.StaffAdminView as staffAdminView
import HospitalApp.Rolviews.AdminView as AdminView
import HospitalApp.Rolviews.InfoSupportView as InfoView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json



class EmployerView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return AdminView.getEmployers(self, request, id)

    def post(self, request):
        return AdminView.createEmployer(self,request)

    def put(self, request, id):
        return AdminView.updateEmployer(self,request, id)

    def delete(self, request, id):
        return AdminView.deleteEmployer(self,request, id)

  

#Paciente---------------------
class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return staffAdminView.getPatient(self, request, id)
 
    def post(self, request):
        return staffAdminView.createPatient(self,request)
 
    def put(self, request, id):
        return staffAdminView.updatePatient(self,request, id)
 
    def delete(self, request, id):
        return staffAdminView.deletePatient(self,request, id)


class ClinicalAppointmentView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request,id):
        return staffAdminView.getClinicalAppointment(self, request, id)
 
    def post(self,request):
        return staffAdminView.createClinicalAppointment(self, request)
    
    def put(self,request):
        pass
 
    def delete(self,request,id):
       return staffAdminView.deleteClinicalAppointment(self, request, id)




#-------------------------
#inventario ------------

      #medicina
class MedicineView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return InfoView.getMedicine(self, request, id)

 
    def post(self,request):
        return InfoView.createMedicine(self, request)
 
    def put(self, request, id):
        return InfoView.updateMedicine(self, request, id)    
 
    def delete(self, request, id):
        return InfoView.deleteMedicine(self, request, id)  


         ##Procedimiento
class ProcedureView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return InfoView.getProcedure(self, request, id)
 
    def post(self,request):
        return InfoView.createProcedure(self, request)
 
    def put(self, request, id):
        return InfoView.updateProcedure(self, request, id)

 
    def delete(self, request, id):
        return InfoView.deleteProcedure(self, request, id)

      #Ayudas Diagnosticas
class DiagnosticHelpView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return InfoView.getDiagnosticHelp(self, request, id)
    
    def post(self,request):
        return InfoView.createDiagnosticHelp(self, request)

    def put(self, request, id):
        return InfoView.updateDiagnosticHelp(self, request, id)

    def delete(self, request, id):
        return InfoView.deleteDiagnosticHelp(self, request, id)

#---------


