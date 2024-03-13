import Service.NurseService as nurseService
import Validators.TypeValidator as validators
import datetime

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

def createHistoryVisitsQuery(hospital,id,nurseId):
    patientId = id
    bloodPressure = input("ingrese la presion arterial \n")
    validators.textValidator(bloodPressure,"presion arterial")
    temperature = input("ingrese la temperatura \n")
    validators.textValidator(temperature,"la temperatura")
    pulse =input("ingrese el pulso \n")
    validators.textValidator(pulse,"pulso")
    oxygenBlood = input("ingrese el nivel de oxigeno en la sangre \n")
    validators.textValidator(oxygenBlood,"ingrese el nivel de oxigeno en la sangre")
    observation = input("observaciones \n")
    if observation=="":
       observation="N/A"
    validators.textValidator(observation,"observaciones") 
    order = createOrder(hospital, patientId, nurseId)
    orderd = vars(order)  
    nurseService.createHistoryVisitsQuery(hospital,patientId,nurseId,bloodPressure,temperature,pulse,oxygenBlood,observation,orderd)
 



def showHistoryVisitsQuery(hospital, patientId):
    nurseService.showHistoryVisitsQuery(hospital,patientId)
    patientHistory = hospital.historyVisits.get(str(patientId))
    print("Historial de visitas para el paciente:")
    for visitDate, visitDetails in patientHistory.items():
        printVisitDetails(visitDate, visitDetails)


def printVisitDetails(visitDate, visitDetails):
    print(f"Fecha: {visitDate}")
    for key, value in visitDetails.items():
        if key == 'order':
            printOrderDetails(value)
        else:
            print(f"{key}: {value}")
    print("")

def printOrderDetails(orderDetails):
    print("Orden:")
    for orderKey, orderValue in orderDetails.items():
        if orderKey not in ['medicines', 'procedure']:
            print(f"  {orderKey}: {orderValue}")
    printMedicines(orderDetails.get('medicines', []))
    printProcedures(orderDetails.get('procedure', []))
   

def printMedicines(medicines):
    if medicines:
        print("  Medicamentos:")
        for medicine in medicines:
            printMedicineDetails(medicine)

def printMedicineDetails(medicine):
    print(f"    Item: {medicine['itemMedicine']}")
    print(f"    Nombre: {medicine['medicineName']}")
    print(f"    Dosis: {medicine['medicineDose']}")
    print(f"    Duración: {medicine['durationMedication']}")
    print(f"    Costo: {medicine['medicineCost']}")
    print("")

def printProcedures(procedures):
    if procedures:
        print("  Procedimientos:")
        for procedure in procedures:
            printProcedureDetails(procedure)

def printProcedureDetails(procedure):
    print(f"    Item: {procedure['itemProcedure']}")
    print(f"    Nombre: {procedure['nameProcedure']}")
    print(f"    Repetición: {procedure['numberRepeated']}")
    print(f"    Frecuencia: {procedure['frequencyRepeated']}")
    print(f"    Costo: {procedure['procedureCost']}")
    print(f"    Requiere Especialista: {procedure['requiresSpecialistP']}")
    if procedure['requiresSpecialistP'].lower() == 'si':
        print(f"    ID del Especialista: {procedure['specialistId']}")
    print("")    



def createOrder(hospital, patientId, nurseId):
    orderId = len(hospital.orders)
    date=datetime.date.today()
    procedures = []
    medicines = []
    diagnosticHelp = []

    while True:
        print("Seleccione una opción:")
        print("1. Agregar procedimiento")
        print("2. Agregar medicina")
        print("3. Finalizar")
        option = input("Ingrese el número correspondiente a la opción deseada: ")
        if option == '1':
            procedure = createProcedure(hospital, orderId)
            procedures.append(procedure)
        elif option == '2':
            medicine = createMedicine(hospital, orderId)
            medicines.append(medicine)
        elif option == '3':
            break
        else:
            print("Opción no válida. Debe seleccionar 1, 2 o 3.")

    order = nurseService.createOrder(hospital, orderId, patientId, nurseId, date, diagnosticHelp, medicines, procedures)
    return order





def createMedicine(hospital,orderId):
    itemMedicine = len(hospital.medicines) + 1

    medicineName = input("ingrese el nombre de la medicina \n")
    validators.textValidator(medicineName,"medicinas")
    medicineDose =input("ingrese la dosis de la medicina \n")
    validators.textValidator(medicineDose,"dosis")
    durationMedication = input("ingrese la duracion de la medicacion \n")
    validators.textValidator(durationMedication,"duracion ")
    medicineCost = input("ingrese el costo de la medicina \n")
    validators.costValidator(medicineCost,"costo")       
    medicine=nurseService.createMedicine(hospital,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost) 
    medicine = vars(medicine)

    return medicine

def createProcedure(hospital,orderId):
    itemProcedure = len(hospital.procedures) + 1
    nameProcedure = input("ingrese el nombre del procedimiento \n")
    validators.textValidator(nameProcedure,"procedimiento")
    numberRepeated =input("ingrese el numero de veces que se repite el procedimiento \n")
    validators.textValidator(numberRepeated,"numero")
    frequencyRepeated = input("ingrese la frecuencia que se repite el procedimiento \n")
    validators.textValidator(frequencyRepeated,"frecuencia ")
    procedureCost = input("ingrese el costo del procedimiento \n")
    validators.costValidator(procedureCost,"costo")   
    requiresSpecialistP = input("ingrese  si requiere especialista (si/no) \n")
    validators.textValidator(requiresSpecialistP,"especialista ")
    if requiresSpecialistP.lower() == 'si':
        specialistId = input("Ingrese el ID del especialista: ")
        validators.numberValidator(specialistId,"id especialista")      
    else:
         requiresSpecialistP= "no"
         specialistId = "N/A"
    procedure=nurseService.createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    procedure = vars(procedure)
    return procedure 
    
