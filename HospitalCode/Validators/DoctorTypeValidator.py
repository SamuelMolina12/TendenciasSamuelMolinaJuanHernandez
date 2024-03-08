from Validators.TypeValidator import *
import Service.DoctorService as doctorService



# def checkPatientExistence(hospital,id):
#     id = int(input("Ingrese el ID del paciente: "))
#     patient = doctorService.validateId(hospital, id)
#     if patient:
#         print("El paciente existe")
#     else:
#         print("No se encontró ningún paciente con ese ID")
       
def showPatient(hospital, id):
    print(id)
    patient = doctorService.validateId(hospital, id)
    if patient:
        print(f"Cedula: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Genero: {patient.genre}")
        print(f"Email: {patient.mail}")
        print(f"Telefono: {patient.telephone}")
        print(f"Fecha de nacimiento: {patient.birth}")
        print(f"Direccion: {patient.address}")         
        print()
    else:
        print("Paciente no encontrado.")


def createHistoryClinicQuery(hospital,patientId,doctorId):
    
    consultationReason = input("ingrese la razon de la consulta \n")
    textValidator(consultationReason,"razon de la consulta ")
    symptomatology = input("ingrese los sintomas \n")
    textValidator(symptomatology,"la sintomas")
    diagnosis =input("ingrese el diagnostico \n")
    textValidator(diagnosis,"diagnostico")
    doctorService.createHistoryClinicQuery(hospital,patientId,doctorId,consultationReason,symptomatology,diagnosis)


def showHistoryClinicQuery(hospital,patientId):
    doctorService.showHistoryClinicQuery(hospital,patientId)
    patient_history = hospital.historyClinic.get(str(patientId))
    print("Historial clinico para el paciente:")
    for visit_date, visit_details in patient_history.items():
        print(f"Fecha: {visit_date}")
        for key, value in visit_details.items():
            print(f"{key}: {value}")
        print("")   