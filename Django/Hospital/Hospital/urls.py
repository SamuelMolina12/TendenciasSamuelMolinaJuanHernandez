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
from HospitalApp.views import EmployerView,PatientView,ClinicalAppointmentView
urlpatterns = [
    path('admin/', admin.site.urls),
  
    path("hospital/employer", EmployerView.as_view(), name="employers_post"),
    path("hospital/employer/<int:id>", EmployerView.as_view(), name="employers_get_put_delete"),

    path("hospital/patient",PatientView.as_view(),name="patients post"),
    path("hospital/patient/<id>",PatientView.as_view(),name="patients get put and delete"),

    # path("hospital/emergencyContact",EmergencyContactView.as_view(),name="emergencyContacts post"),
    # path("hospital/emergencyContact/<id>",EmergencyContactView.as_view(),name="emergencyContacts get put and delete"),

    # path("hospital/policy",PolicyView.as_view(),name="policies post"),
    # path("hospital/policy/<id>",PolicyView.as_view(),name="policies get put and delete")

    path("hospital/clinicalAppointment",ClinicalAppointmentView.as_view(),name="clinicalAppointments post"),
    path("hospital/clinicalAppointment/<id>",ClinicalAppointmentView.as_view(),name="clinicalAppointments get put and delete"),
]
