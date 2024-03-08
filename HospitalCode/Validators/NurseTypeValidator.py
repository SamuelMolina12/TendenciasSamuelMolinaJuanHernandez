import Service.NurseService as nurseService
from Validators.TypeValidator import *



def showPatient(hospital, id):
    patient = nurseService.validateId(hospital, id)
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

def createHistoryVisitsQuery(hospital,id):
    patientId = id

    bloodPressure = input("ingrese la presion arterial \n")
    textValidator(bloodPressure,"presion arterial")
    temperature = input("ingrese la temperatura \n")
    textValidator(temperature,"la temperatura")
    pulse =input("ingrese el pulso \n")
    textValidator(pulse,"pulso")
    oxygenBlood = input("ingrese el nivel de oxigeno en la sangre \n")
    textValidator(oxygenBlood,"ingrese el nivel de oxigeno en la sangre")
    medicine=input("ingrese medicamento\n")
    if medicine=="":
        medicine="N/A"
    textValidator(medicine,"ingrese el medicamento")
    medicineDose=input("dosis de medicamento\n")
    if medicineDose=="":
        medicineDose="N/A"
    procedure=input("ingrese el procedimiento\n")
    if procedure=="":
        procedure="N/A"
    textValidator(procedure,"procedimiento")
    procedureDetail=input("detalle del procedimiento \n")
    if procedureDetail=="":
        procedureDetail="N/A"
    textValidator(procedureDetail,"detalle procedimiento")    
    medicaltests = input("Pruebas medicas realizadas\n")
    textValidator(medicaltests,"pruebas medicas")
    observation = input("observaciones \n")
    if observation=="":
       observation="N/A"
    textValidator(observation,"observaciones")   
    nurseService.createHistoryVisitsQuery(hospital,patientId,bloodPressure,temperature,pulse,oxygenBlood,medicine,medicineDose,procedure,procedureDetail,medicaltests,observation)
 



def showHistoryVisitsQuery(hospital, patientId):
    nurseService.showHistoryVisitsQuery(hospital,patientId)
    patient_history = hospital.historyVisits.get(str(patientId))
    print("Historial de visitas para el paciente:")
    for visit_date, visit_details in patient_history.items():
        print(f"Fecha de visita: {visit_date}")
        for key, value in visit_details.items():
            print(f"{key}: {value}")
        print("")

