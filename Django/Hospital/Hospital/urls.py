"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HospitalApp.views import EmployerView,PatientView,ClinicalAppointmentView,MedicineView,ProcedureView,DiagnosticHelpView,HistoryClinicView,HistoryVisitsView,SpecialistView,Billing
urlpatterns = [
    path('admin/', admin.site.urls),
# Empleado-----  
    path("hospital/admin/employer", EmployerView.as_view(), name="employers post"),
    path("hospital/admin/employer/<int:id>", EmployerView.as_view(), name="employers get put delete"),
    path("hospital/admin/specialist",SpecialistView.as_view(), name="specialist post"),
    path("hospital/admin/specialist/<int:id>",SpecialistView.as_view(), name="specialist get put delete"),    
#--------
#Paciente---------
    path("hospital/patient",PatientView.as_view(),name="patients post"),
    path("hospital/patient/<int:id>",PatientView.as_view(),name="patients get put and delete"),
   #CitaMedica
    path("hospital/patient/clinicalAppointment",ClinicalAppointmentView.as_view(),name="clinicalAppointments post"),
    path("hospital/patient/clinicalAppointment/<id>",ClinicalAppointmentView.as_view(),name="clinicalAppointments get put and delete"),
   #Historia Clinica
    path("hospital/patient/historyClinic",HistoryClinicView.as_view(),name="historyClinic post"),
    path("hospital/patient/historyClinic/<id>",HistoryClinicView.as_view(),name="historyClinic get put and delete"),    
   #Historia de visitas
    path("hospital/patient/historyVisit",HistoryVisitsView.as_view(),name="historyVisits post"),
    path("hospital/patient/historyVisit/<id>",HistoryVisitsView.as_view(),name="historyVisits get put and delete"),     
   #Factura
    path("hospital/patient/billing",Billing.as_view(),name="billings post"),
    path("hospital/patient/billing/<id>",Billing.as_view(),name="billing get put and delete"),     
#-----------------

#Inventario ----------
    #medicina
    path("hospital/inventory/medicine",MedicineView.as_view(),name="medicines post"),
    path("hospital/inventory/medicine/<int:id>",MedicineView.as_view(),name="medicines get put and delete"),
    #procedimiento
    path("hospital/inventory/procedure",ProcedureView.as_view(),name="procedures post"),
    path("hospital/inventory/procedure/<int:id>",ProcedureView.as_view(),name="procedures get put and delete"),  
    #Ayudas diagnosticas
    path("hospital/inventory/diagnosticHelp",DiagnosticHelpView.as_view(),name="diagnosticaids post"),
    path("hospital/inventory/diagnosticHelp/<int:id>",DiagnosticHelpView.as_view(),name="diagnosticaids get put and delete"), 
#------


]

