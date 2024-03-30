import Validators.TypeValidator as validators
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


def createHistoryClinicQuery(hospital, patientId, doctorId):
    
    consultationReason = input("Ingrese la razón de la consulta: ")
    validators.textValidator(consultationReason, "razón de la consulta")
    symptomatology = input("Ingrese los síntomas: ")
    validators.textValidator(symptomatology, "los síntomas")
    order = createOrder(hospital, patientId, doctorId)
    orderd = vars(order)
    if not orderd.get('diagnosticHelp'):
        diagnosis = input("Ingrese el diagnóstico: ")
        validators.textValidator(diagnosis, "diagnóstico")
    else:
        diagnosis = "N/A"

    doctorService.createHistoryClinicQuery(hospital, patientId, doctorId, consultationReason, symptomatology, diagnosis, orderd)

#-----------------
def showHistoryClinicQuery(hospital, patientId):
    doctorService.showHistoryClinicQuery(hospital, patientId)
    patientHistory = hospital.historyClinic.get(str(patientId))
    print("Historial clínico para el paciente:")
    
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
        if orderKey not in ['medicines', 'procedure', 'diagnosticHelp']:
            print(f"  {orderKey}: {orderValue}")
    printMedicines(orderDetails.get('medicines', []))
    printProcedures(orderDetails.get('procedure', []))
    printDiagnosticHelp(orderDetails.get('diagnosticHelp', []))

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

def printDiagnosticHelp(diagnosticHelp):
    if diagnosticHelp:
        print("  Ayudas Diagnósticas:")
        for diagnostic in diagnosticHelp:
            printDiagnosticDetails(diagnostic)

def printDiagnosticDetails(diagnostic):
    print(f"    Item: {diagnostic['itemDiagnostic']}")
    print(f"    Nombre: {diagnostic['nameDiagnostic']}")
    print(f"    Cantidad: {diagnostic['quantity']}")
    print(f"    Costo: {diagnostic['diagnosticCost']}")
    print(f"    Requiere Especialista: {diagnostic['requiresSpecialistD']}")
    if diagnostic['requiresSpecialistD'].lower() == 'si':
        print(f"    ID del Especialista: {diagnostic['specialistId']}")
    print("")    
#----------------



#...........
def createOrder(hospital, patientId, doctorId):
    orderId = len(hospital.orders)
    date = datetime.date.today()
    procedures = []
    medicines = []
    diagnosticHelp = []

    while True:
        print("Seleccione una opción:")
        print("1. Agregar procedimiento")
        print("2. Agregar medicina")
        print("3. Agregar ayuda diagnóstica")
        print("4. Finalizar")
        option = input("Ingrese el número correspondiente a la opción deseada: ")

        if option == '1':
            addProcedure(diagnosticHelp, procedures, hospital, orderId)
        elif option == '2':
            addMedicine(diagnosticHelp, medicines, hospital, orderId)
        elif option == '3':
            addDiagnosticHelp(procedures, medicines, diagnosticHelp, hospital, orderId)
        elif option == '4':
            break
        else:
            print("Opción no válida. Debe seleccionar 1, 2, 3 o 4.")

    order = doctorService.createOrder(hospital, orderId, patientId, doctorId, date, diagnosticHelp, medicines, procedures)
    return order


def addProcedure(diagnosticHelp, procedures, hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado ayuda diagnóstica. No se pueden agregar procedimientos.")
    else:
        procedure = createProcedure(hospital, orderId)
        procedures.append(procedure)

def addMedicine(diagnosticHelp, medicines, hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado ayuda diagnóstica. No se pueden agregar medicamentos.")
    else:
        medicine = createMedicine(hospital, orderId)
        medicines.append(medicine)

def addDiagnosticHelp(procedures, medicines, diagnosticHelp, hospital, orderId):
    if procedures or medicines:
        print("No se puede agregar ayuda diagnóstica, ya se han agregado procedimientos o medicamentos.")
    else:
        diagnostic = createDiagnosticHelp(hospital, orderId)
        diagnosticHelp.append(diagnostic)

#.............


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
    medicine=doctorService.createMedicine(hospital,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost) 
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
    procedure=doctorService.createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    procedure = vars(procedure)
    return procedure 
    
def createDiagnosticHelp(hospital, orderId):
 
    itemDiagnostic = len(hospital.diagnosticHelp) + 1
    nameDiagnostic = input("Ingrese el nombre del diagnóstico:\n ")
    validators.textValidator(nameDiagnostic, "nombre del diagnóstico")
    quantity = input("Ingrese la cantidad del diagnóstico:\n")
    validators.textValidator(quantity, "cantidad del diagnóstico")
    diagnosticCost = input("Ingrese el costo del diagnóstico: \n")
    validators.costValidator(diagnosticCost, "costo del diagnóstico")
    requiresSpecialistD = input("¿Requiere un especialista para el diagnóstico? (Si/no):\n ").lower()
    validators.textValidator(requiresSpecialistD, "especialista para el diagnóstico")
    if requiresSpecialistD == 'si':
        specialistId = input("Ingrese el ID del especialista: ")
        validators.numberValidator(specialistId,"id especialista")  
    else:
         requiresSpecialistD= "no"
         specialistId = "N/A"   

    diagnosticHelp=doctorService.createDiagnosticHelp(hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    diagnosticHelp = vars(diagnosticHelp)
    return diagnosticHelp
      
