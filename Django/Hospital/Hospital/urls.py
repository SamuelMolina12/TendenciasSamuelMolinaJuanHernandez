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
from HospitalApp.views import EmployerView,PatientView,ClinicalAppointmentView,MedicineView,ProcedureView,DiagnosticHelpView
urlpatterns = [
    path('admin/', admin.site.urls),
# Empleado-----  
    path("hospital/employer", EmployerView.as_view(), name="employers_post"),
    path("hospital/employer/<int:id>", EmployerView.as_view(), name="employers_get_put_delete"),
#--------
#Paciente---------
    path("hospital/patient",PatientView.as_view(),name="patients post"),
    path("hospital/patient/<int:id>",PatientView.as_view(),name="patients get put and delete"),

    # path("hospital/emergencyContact",EmergencyContactView.as_view(),name="emergencyContacts post"),
    # path("hospital/emergencyContact/<id>",EmergencyContactView.as_view(),name="emergencyContacts get put and delete"),

    # path("hospital/policy",PolicyView.as_view(),name="policies post"),
    # path("hospital/policy/<id>",PolicyView.as_view(),name="policies get put and delete")

    path("hospital/patient/clinicalAppointment",ClinicalAppointmentView.as_view(),name="clinicalAppointments post"),
    path("hospital/patient/clinicalAppointment/<id>",ClinicalAppointmentView.as_view(),name="clinicalAppointments get put and delete"),
#-----------------

#Inventario ----------
    path("hospital/inventory/medicine",MedicineView.as_view(),name="medicines post"),
    path("hospital/inventory/medicine/<int:id>",MedicineView.as_view(),name="medicines get put and delete"),
    path("hospital/inventory/procedure",ProcedureView.as_view(),name="procedures post"),
    path("hospital/inventory/procedure/<int:id>",ProcedureView.as_view(),name="procedures get put and delete"),    
    path("hospital/inventory/diagnosticHelp",DiagnosticHelpView.as_view(),name="diagnosticaids post"),
    path("hospital/inventory/diagnosticHelp/<int:id>",DiagnosticHelpView.as_view(),name="diagnosticaids get put and delete"), 
#------
    # path("hospital/PatientInfo",PatientInfoView.as_view(),name="PatientInfo post"),
    # path("hospital/PatientInfo/<int:id>",PatientInfoView.as_view(),name="PatientInfo get put and delete"),
#-----------------

]

