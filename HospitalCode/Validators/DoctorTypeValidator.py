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


def createHistoryClinicQuery(hospital, patientId, doctorId):
    
    consultationReason = input("Ingrese la razón de la consulta: ")
    textValidator(consultationReason, "razón de la consulta")
    symptomatology = input("Ingrese los síntomas: ")
    textValidator(symptomatology, "los síntomas")
    order = createOrder(hospital, patientId, doctorId)
    orderd = vars(order)
    print(orderd)
    if not orderd.get('diagnosticHelp'):
        diagnosis = input("Ingrese el diagnóstico: ")
        textValidator(diagnosis, "diagnóstico")
    else:
        diagnosis = "N/A"

    doctorService.createHistoryClinicQuery(hospital, patientId, doctorId, consultationReason, symptomatology, diagnosis, orderd)

#-----------------
def showHistoryClinicQuery(hospital, patientId):
    doctorService.showHistoryClinicQuery(hospital, patientId)
    patient_history = hospital.historyClinic.get(str(patientId))
    print("Historial clínico para el paciente:")
    
    for visit_date, visit_details in patient_history.items():
        print_visit_details(visit_date, visit_details)

def print_visit_details(visit_date, visit_details):
    print(f"Fecha: {visit_date}")
    for key, value in visit_details.items():
        if key == 'order':
            print_order_details(value)
        else:
            print(f"{key}: {value}")
    print("")

def print_order_details(order_details):
    print("Orden:")
    for order_key, order_value in order_details.items():
        if order_key not in ['medicines', 'procedure', 'diagnosticHelp']:
            print(f"  {order_key}: {order_value}")
    print_medicines(order_details.get('medicines', []))
    print_procedures(order_details.get('procedure', []))
    print_diagnostic_help(order_details.get('diagnosticHelp', []))

def print_medicines(medicines):
    if medicines:
        print("  Medicamentos:")
        for medicine in medicines:
            print_medicine_details(medicine)

def print_medicine_details(medicine):
    print(f"    Item: {medicine['itemMedicine']}")
    print(f"    Nombre: {medicine['medicineName']}")
    print(f"    Dosis: {medicine['medicineDose']}")
    print(f"    Duración: {medicine['durationMedication']}")
    print(f"    Costo: {medicine['medicineCost']}")
    print("")

def print_procedures(procedures):
    if procedures:
        print("  Procedimientos:")
        for procedure in procedures:
            print_procedure_details(procedure)

def print_procedure_details(procedure):
    print(f"    Item: {procedure['itemProcedure']}")
    print(f"    Nombre: {procedure['nameProcedure']}")
    print(f"    Repetición: {procedure['numberRepeated']}")
    print(f"    Frecuencia: {procedure['frequencyRepeated']}")
    print(f"    Costo: {procedure['procedureCost']}")
    print(f"    Requiere Especialista: {procedure['requiresSpecialistP']}")
    if procedure['requiresSpecialistP'].lower() == 'si':
        print(f"    ID del Especialista: {procedure['specialistId']}")
    print("")    

def print_diagnostic_help(diagnostic_help):
    if diagnostic_help:
        print("  Ayudas Diagnósticas:")
        for diagnostic in diagnostic_help:
            print_diagnostic_details(diagnostic)

def print_diagnostic_details(diagnostic):
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
        print_options()
        option = input("Ingrese el número correspondiente a la opción deseada: ")

        if option == '1':
            add_procedure(diagnosticHelp, procedures, hospital, orderId)
        elif option == '2':
            add_medicine(diagnosticHelp, medicines, hospital, orderId)
        elif option == '3':
            add_diagnostic_help(procedures, medicines, diagnosticHelp, hospital, orderId)
        elif option == '4':
            break
        else:
            print("Opción no válida. Debe seleccionar 1, 2, 3 o 4.")

    order = doctorService.createOrder(hospital, orderId, patientId, doctorId, date, diagnosticHelp, medicines, procedures)
    return order

def print_options():
    print("Seleccione una opción:")
    print("1. Agregar procedimiento")
    print("2. Agregar medicina")
    print("3. Agregar ayuda diagnóstica")
    print("4. Finalizar")

def add_procedure(diagnosticHelp, procedures, hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado ayuda diagnóstica. No se pueden agregar procedimientos.")
    else:
        procedure = createProcedure(hospital, orderId)
        procedures.append(procedure)

def add_medicine(diagnosticHelp, medicines, hospital, orderId):
    if diagnosticHelp:
        print("Ya se ha agregado ayuda diagnóstica. No se pueden agregar medicamentos.")
    else:
        medicine = createMedicine(hospital, orderId)
        medicines.append(medicine)

def add_diagnostic_help(procedures, medicines, diagnosticHelp, hospital, orderId):
    if procedures or medicines:
        print("No se puede agregar ayuda diagnóstica, ya se han agregado procedimientos o medicamentos.")
    else:
        diagnostic = createDiagnosticHelp(hospital, orderId)
        diagnosticHelp.append(diagnostic)

#.............


def createMedicine(hospital,orderId):
    itemMedicine = len(hospital.medicines) + 1

    medicineName = input("ingrese el nombre de la medicina \n")
    textValidator(medicineName,"medicinas")
    medicineDose =input("ingrese la dosis de la medicina \n")
    textValidator(medicineDose,"dosis")
    durationMedication = input("ingrese la duracion de la medicacion \n")
    textValidator(durationMedication,"duracion ")
    medicineCost = input("ingrese el costo de la medicina \n")
    textValidator(medicineCost,"costo")       
    medicine=doctorService.createMedicine(hospital,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost) 
    medicine = vars(medicine)
    print(medicine)
    return medicine

def createProcedure(hospital,orderId):
    itemProcedure = len(hospital.procedures) + 1
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
    else:
         requiresSpecialistP= "no"
         specialistId = "N/A"
    procedure=doctorService.createProcedure(hospital,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId)
    procedure = vars(procedure)
    print(procedure)
    return procedure 
    
def createDiagnosticHelp(hospital, orderId):
 
    itemDiagnostic = len(hospital.diagnosticHelp) + 1
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
    else:
         requiresSpecialistD= "no"
         specialistId = "N/A"   

    diagnosticHelp=doctorService.createDiagnosticHelp(hospital,orderId, itemDiagnostic, nameDiagnostic, quantity, diagnosticCost, requiresSpecialistD, specialistId)
    diagnosticHelp = vars(diagnosticHelp)
    print(diagnosticHelp)
    return diagnosticHelp
      
