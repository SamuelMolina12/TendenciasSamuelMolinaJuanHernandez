from Validators.TypeValidator import *
import Service.DoctorService as doctorService
import datetime


# def checkPatientExistence(hospital,id):
#     id = int(input("Ingrese el ID del paciente: "))
#     patient = doctorService.validateId(hospital, id)
#     if patient:
#         print("El paciente existe")
#     else:
#         print("No se encontró ningún paciente con ese ID")
       
def showPatient(hospital, id):
    
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
    order= createOrder(hospital, patientId, doctorId)
    doctorService.createHistoryClinicQuery(hospital,patientId,doctorId,consultationReason,symptomatology,diagnosis,order)
   

def showHistoryClinicQuery(hospital,patientId):
    doctorService.showHistoryClinicQuery(hospital,patientId)
    patient_history = hospital.historyClinic.get(str(patientId))
    print("Historial clinico para el paciente:")
    for visit_date, visit_details in patient_history.items():
        print(f"Fecha: {visit_date}")
        for key, value in visit_details.items():
            print(f"{key}: {value}")
        print("")



def createOrder(hospital, patientId, doctorId):
    orderId = len(hospital.orders)
    date = datetime.date.today()
    doctorService.createOrder(hospital, orderId, patientId, doctorId, date)
    procedure = "N/A"
    medicine = "N/A"
    
    helpDiagnostic = input("¿Requiere ayuda diagnóstica?: ").lower()
    if helpDiagnostic == 'si':
        createDiagnosticHelp(hospital, orderId)

    else:
            
        print("Seleccione una opción:")
        print("1. Crear procedimiento")
        print("2. Crear medicina")
        print("3. Crear ambos procedimientos y medicamentos")
        option = input("Ingrese el número correspondiente a la opción deseada: ")
        if option == '1':
            createProcedure(hospital, orderId)
        elif option == '2':
            createMedicine(hospital, orderId)
        elif option == '3':
            createProcedure(hospital, orderId)
            createMedicine(hospital, orderId)
        else:
            print("Opción no válida. Debe seleccionar 1, 2 o 3.")





def createMedicine(hospital,orderId):
    itemMedicine = input("ingrese el item de la medicina \n")
    textValidator(itemMedicine,"item ")
    medicineName = input("ingrese el nombre de la medicina \n")
    textValidator(medicineName,"medicinas")
    medicineDose =input("ingrese la dosis de la medicina \n")
    textValidator(medicineDose,"dosis")
    durationMedication = input("ingrese la duracion de la medicacion \n")
    textValidator(durationMedication,"duracion ")
    medicineCost = input("ingrese el costo de la medicina \n")
    textValidator(medicineCost,"costo")
       
    doctorService.createMedicine(hospital,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost) 

def createProcedure(hospital,orderId):
    
    itemProcedure = input("ingrese el item del procedimiento \n")
    textValidator(itemProcedure,"item ")
    nameProcedure = input("ingrese el nombre del procedimiento \n")
    textValidator(nameProcedure,"procedimiento")
    numberRepeated =input("ingrese el numero de veces que se repite el procedimiento \n")
    textValidator(numberRepeated,"numero")
    frequencyRepeated = input("ingrese la frecuencia que se repite el procedimiento \n")
    textValidator(frequencyRepeated,"frecuencia ")
    procedureCost = input("ingrese el costo del procedimiento \n")
    textValidator(procedureCost,"costo")   
    requiresSpecialistP = input("ingrese el si requiere especialista (si/no) \n")
    textValidator(requiresSpecialistP,"especialista ")
    if requiresSpecialistP.lower() == 'si':
       specialistId = input("Ingrese el ID del especialista: ")   
    
    doctorService.createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId) 
    
def createDiagnosticHelp(hospital, orderId):

    itemDiagnostic = input("Ingrese el ítem del diagnóstico:\n ")
    textValidator(itemDiagnostic, "ítem del diagnóstico")
    nameDiagnostic = input("Ingrese el nombre del diagnóstico:\n ")
    textValidator(nameDiagnostic, "nombre del diagnóstico")
    quantity = input("Ingrese la cantidad del diagnóstico:\n")
    textValidator(quantity, "cantidad del diagnóstico")
    diagnosticCost = input("Ingrese el costo del diagnóstico: \n")
    textValidator(diagnosticCost, "costo del diagnóstico")
    requiresSpecialistD = input("¿Requiere un especialista para el diagnóstico? (Si/no):\n ").lower()
    textValidator(requiresSpecialistD, "especialista para el diagnóstico")
    if requiresSpecialistD == 'si':
        specialistId = input("Ingrese el ID del especialista: ")
    doctorService.createDiagnosticHelp(hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
      
def showOrder(hospital, orderId):
    order = None
    for o in hospital.orders:
        if o.orderId == orderId:
            order = o
            break

    if order:
        print(f"ID de la Orden: {order.orderId}")
        print(f"ID del Paciente: {order.patientId}")
        print(f"ID del Doctor: {order.doctorId}")
        print(f"Fecha de la Orden: {order.date}")

        if order.medicines:
            print("Medicamentos:")
            print(f"Item: {medicines.itemMedicine}")
            print(f"Nombre: {medicines.medicineName}")
            print(f"Dosis: {medicines.medicineDose}")
            print(f"Duración: {medicines.durationMedication}")
            print(f"Costo: {medicines.medicineCost}")
            print()

    else:
        print("No se encontró ninguna orden con ese ID.")
  