import Service.NurseService as nurseService
from Validators.TypeValidator import *



def showPatient(hospital, id):
    print(id)
    patient = nurseService.validateId(hospital, id)
    if patient:
        print(f"Cedula: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Genero: {patient.genre}")
        print(f"Email: {patient.mail}")
        print(f"Telefono: {patient.telephone}")
        print(f"Fecha de nacimiento: {patient.birth}")
        print(f"Direccion: {patient.address}")
        if patient.emergencyContact:
            print("Contacto de Emergencia:")
            print(f"Nombre: {patient.emergencyContact.name}")
            print(f"Relación: {patient.emergencyContact.relationship}")
            print(f"Teléfono: {patient.emergencyContact.telephone}")                  
        if patient.policy:
            print("Poliza:")
            print(f"Compañía de Seguros: {patient.policy.insuaranceCompany}")
            print(f"Número de Póliza: {patient.policy.policynumber}")
            print(f"Estado de la Póliza: {patient.policy.statePolicy}")
            print(f"Término de la Póliza: {patient.policy.termPolicy}")         
        print()
    else:
        print("Paciente no encontrado.")

def createHistoryVisitsQuery(hospital,id):
    patientId = id
    id=len(hospital.patient)
    bloodPressure = input("ingrese la presion arterial \n")
    textValidator(bloodPressure,"presion arterial")
    temperature = input("ingrese la temperatura \n ")
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