from django.shortcuts import render
from django.views import View

import HospitalApp.validators.PatientValidator as staffAdminValidator


import HospitalApp.Rolviews.PatientView as patientView
import HospitalApp.Rolviews.EmployerView as employerView
import HospitalApp.Rolviews.InventoryView as inventoryView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json


# Empleados/especialistas


class EmployerView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return employerView.getEmployers(self, request, id)

    def post(self, request):
        return employerView.createEmployer(self,request)

    def put(self, request, id):
        return employerView.updateEmployer(self,request, id)

    def delete(self, request, id):
        return employerView.deleteEmployer(self,request, id)
    
class SpecialistView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return employerView.getSpecialists(self, request, id)

    def post(self, request):
        return employerView.createSpecialist(self,request)

    def put(self, request, id):
        return employerView.updateSpecialist(self,request, id)

    def delete(self, request, id):
        return employerView.deleteSpecialist(self,request, id)
 
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self,request):
        return employerView.postLogin(self,request)
    
    def get(self,request):
        return employerView.getLogin(self, request)       
#------
#Paciente---------------------
class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return patientView.getPatient(self, request, id)
 
    def post(self, request):
        return patientView.createPatient(self,request)
 
    def put(self, request, id):
        return patientView.updatePatient(self,request, id)
 
    def delete(self, request, id):
        return patientView.deletePatient(self,request, id)


class ClinicalAppointmentView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self,request,id=None):
        return patientView.getClinicalAppointment(self, request, id)
 
    def post(self,request):
        return patientView.createClinicalAppointment(self, request)
    
    # def put(self,request):
    #     pass
 
    def delete(self,request,id):
       return patientView.deleteClinicalAppointment(self, request, id)
#Ordenes      
class OrderView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id):
        return patientView.getOrder(self,request,id)
 
    def post(self, request):
        return patientView.createOrder(self, request)
 
    # def put(self, request, id):
    #    pass
 
    # def delete(self, request, id):
    #     pass 

class OrderMedicineView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        pass
 
    def post(self, request):
        return patientView.createOrderMedicine(self, request)
 
    # def put(self, request, id):
    #    pass
 
    # def delete(self, request, id):
    #     pass

class OrderProcedureView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        pass
 
    def post(self, request):
        return patientView.createOrderProcedure(self, request)
 
    # def put(self, request, id):
    #    pass
 
    # def delete(self, request, id):
    #     pass

class OrderDiagnosticHelpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        pass
 
    def post(self, request):
        return patientView.createOrderDiagnosticHelp(self, request)
 
    # def put(self, request, id):
    #    pass
 
    # def delete(self, request, id):
    #     pass

#historia
class HistoryClinicView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id):
        return patientView.getHistoryClinic(self,request,id)
 
    def post(self, request):
        return patientView.createHistoryClinic(self, request)
 
    def put(self, request, id):
        pass
 
    def delete(self, request, id):
        pass
    
class HistoryVisitsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return patientView.getHistoryVisits(self, request, id)
 
    def post(self, request):
        return patientView.createHistoryVisits(self, request)
 
    def put(self, request, id):
       pass
 
    def delete(self, request, id):
        pass 

class Billing(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id):
        return patientView.getBilling(self, request, id)
 
    def post(self, request):
        return patientView.createBilling(self, request)
 
    def put(self, request, id):
        pass
 
    def delete(self, request, id):
        pass

#-------------------------
#inventario ------------

      #medicina
class MedicineView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return inventoryView.getMedicine(self, request, id)

 
    def post(self,request):
        return inventoryView.createMedicine(self, request)
 
    def put(self, request, id):
        return inventoryView.updateMedicine(self, request, id)    
 
    def delete(self, request, id):
        return inventoryView.deleteMedicine(self, request, id)  


         ##Procedimiento
class ProcedureView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return inventoryView.getProcedure(self, request, id)
 
    def post(self,request):
        return inventoryView.createProcedure(self, request)
 
    def put(self, request, id):
        return inventoryView.updateProcedure(self, request, id)

 
    def delete(self, request, id):
        return inventoryView.deleteProcedure(self, request, id)

      #Ayudas Diagnosticas
class DiagnosticHelpView(View):
   
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)
   
    def get(self, request, id=None):
        return inventoryView.getDiagnosticHelp(self, request, id)
    
    def post(self,request):
        return inventoryView.createDiagnosticHelp(self, request)

    def put(self, request, id):
        return inventoryView.updateDiagnosticHelp(self, request, id)

    def delete(self, request, id):
        return inventoryView.deleteDiagnosticHelp(self, request, id)

#---------


   