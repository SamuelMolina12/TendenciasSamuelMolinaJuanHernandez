import Validators.TypeValidator as validators
import Models.models as models
import Service.StaffAdminService as staffAdminService



def createPatient(hospital):
    id = validators.numberValidator(input("Ingrese la cédula:\n"), "cedula de")
    name = input("Ingrese el nombre :\n")
    validators.textValidator(name, "nombre  \n")
    genre = input("Ingrese el género: masculino o femenino\n")
    validators.textValidator(genre, "genero de\n")
    validators.genreValidator(genre, "genero de\n")
    mail = input("Ingrese el correo:\n")
    validators.textValidator(mail, "correo  \n")
    validators.emailValidator(mail,"correo \n")
    telephone = validators.phoneValidator(input("ingrese el numero telefonico " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
    birth = validators.dateValidator(input("ingrese la fecha de nacimiento " + "Formato DD/MM/YYYY, max 150 años\n"),"fecha de nacimiento de")
    address = input("ingrese la direccion " + "Máximo 30 caracteres  \n")
    validators.textValidator(address, "direccion de    \n")
    validators.addressValidator(address, "direccion de  \n")
    staffAdminService.createPatient(hospital, id, name, genre, mail, telephone, birth, address)
    print("Contacto de emergencia")
    createEmergencyContact(hospital,id)
    print("Póliza")
    createPolicy(hospital,id)
    print("Paciente creado con exito")

    

def createEmergencyContact(hospital,patientId):
    name = input("Ingrese el nombre del contacto de emergencia del paciente: \n") 
    validators.textValidator(name,"Nombre del paciente")
    relationship = input("Ingrese la relacion del contacto de emergencia:\n")
    validators.textValidator(relationship,"Relacion del contacto de emergencia")
    telephone = validators.phoneValidator(input("ingrese el numero de contacto de emergencia " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefonico ")
    staffAdminService.createEmergencyContact(hospital,patientId,name,relationship,telephone)

def createPolicy(hospital,patientId):
    insuranceCompany = input("Ingrese el nombre de la compañia: \n")
    validators.textValidator(insuranceCompany, "nombre de la compañia \n")
    policynumber = validators.numberValidator(input("Ingrese el numero de poliza: \n"), "Numero de poliza")
    statePolicy = input("Ingrese el estado de la poliza: (activa/inactiva) \n")
    validators.policyStateValidator(statePolicy, "estado de la poliza \n")
    termPolicy = input("Ingrese la fecha de terminacion de la poliza: Formato (DD/MM/YYYY) \n")
    validators.dateValidator(termPolicy, "fecha de \n")
    staffAdminService.createPolicy(hospital,patientId,insuranceCompany,policynumber,statePolicy,termPolicy)

def showPatient(hospital, id):
    patient = staffAdminService.validateId(hospital, id)
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


def deletePatient(hospital,id):
    id = int(id)
    if staffAdminService.deletePatient(hospital, id):
         deletePatient2(hospital, id)
    else:
        print("No se encontró ningún usuario con esa identificación.")

def deletePatient2(hospital, id):
    for i, user in enumerate(hospital.patient):
        if user.id == id:
            del hospital.patient[i]
            print("Usuario eliminado exitosamente.")
            return
def updatePatient(hospital,id):
    patient = staffAdminService.validateId(hospital,id)
    if patient:
        print("Paciente encontrado. Introduzca los nuevos datos:")

        newName = input("ingrese el nuevo nombre \n")
        newGenre = input("ingrese el nuevo genero: (masculino/femenino) \n")
        newMail = input("ingrese el nuevo correo " + " dominio y el @ \n")
        newTelephone = input("Nuevo telefono: " + "Debe contener entre 1 y 10 dígitos") 
        newBirth = input("nueva fecha de nacimiento: " + "Formato DD/MM/YYYY")
        newAddress = input("ingrese la nueva direccion " + "Máximo 30 caracteres\n")
        updateEmergencyContact(patient)
        updatePolicy(patient)
            
        if newName:
            validators.textValidator(newName,"el nuevo nombre \n")
            patient.name = newName
        if newGenre:
            validators.genreValidator(newGenre, "nuevo genero: masculino o femenino\n")
            
        if newMail:
            newMail=validators.emailValidator( newMail,"nuevo correo \n")
            
        if newTelephone:
            newTelephone=validators.phoneValidator(newTelephone, "nuevo numero de telefono\n")
            
        if newBirth:
            newBirth=validators.dateValidator(newBirth, "nueva fecha de nacimiento\n")
            
        if newAddress:
            newAddress=validators.addressValidator(newAddress, "direccion \n")
            


        #patient.name = newName if newName else patient.name
        patient.genre = newGenre if newGenre else patient.genre
        patient.mail = newMail if newMail else patient.mail
        patient.telephone = newTelephone if newTelephone else patient.telephone
        patient.birth = newBirth if newBirth else patient.birth
        patient.address = newAddress if newAddress else patient.address 


        print("Paciente actualizado correctamente.")
    else:
        print("No se encontró ningún paciente con ese ID.")

def updateEmergencyContact(patient):
    
    newName = input("Nuevo nombre de contacto de emergencia: ")
    newRelationship = input("Nueva relación con el paciente: ")
    newTelephone = input("Nuevo telefono de contacto de emergencia: " + "Debe contener entre 1 y 10 dígitos: ") 
    
    
    if newName:
        validators.textValidator(newName,"el nuevo nombre \n")
        patient.emergencyContact.name = newName
        
    if newRelationship:
        validators.textValidator(newRelationship,"nueva relacion con el paciente \n")
        patient.emergencyContact.relationship = newRelationship

    if newTelephone:
        newTelephone=validators.phoneValidator(newTelephone, "nuevo numero de telefono\n")
        
    #patient.emergencyContact.name = newName if newName else patient.emergencyContact.name
    #patient.emergencyContact.relationship = newRelationship if newRelationship else patient.emergencyContact.relationship     
    patient.emergencyContact.telephone = newTelephone if newTelephone else patient.emergencyContact.telephone    

def updatePolicy(patient):
    newInsuranceCompany = input("Nuevo nombre del la compañia: ")
    
    newPolicynumber = input("Nuevo numero de poliza: ")
    
    newStatePolicy = input("Nuevo estado de la poliza: (activa/inactiva) ")
    
    newTermPolicy = input("Nueva fecha de finalizacion de poliza: formato (DD/MM/YYYY) ")
    

    if newInsuranceCompany :
        validators.textValidator(newInsuranceCompany,"el nuevo nombre \n")
        patient.policy.insuranceCompany = newInsuranceCompany 
    if newPolicynumber:
        validators.numberValidator(newPolicynumber," nuevo numero de poliza \n")
        patient.policy.policynumber = newPolicynumber
    if newStatePolicy:
        validators.textValidator(newStatePolicy,"nuevo estado de la poliza \n")
        patient.policy.statePolicy =  newStatePolicy
    if  newTermPolicy:
        validators.dateValidator(newTermPolicy,"nueva fecha de finalizacion de poliza \n")
       

    #patient.policy.insuranceCompany = newInsuranceCompany if newInsuranceCompany else patient.policy.insuranceCompany
    #patient.policy.policynumber =newPolicynumber if newPolicynumber else patient.policy.policynumber
    #patient.policy.statePolicy =newStatePolicy if newStatePolicy else patient.policy.statePolicy
    
    patient.policy.termPolicy =newTermPolicy if newTermPolicy else patient.policy.termPolicy

def createClinicalAppointment(hospital,id):
    patientId = id
    date= input("Ingrese la fecha de la cita: Formato (DD/MM/YYYY)\n")
    validators.dateValidator(date, "fecha  \n")
    hour = input("ingrese la hora de la cita: formato 24 horas\n")
    validators.timeValidator(hour, "hora de\n")
    doctor = input("Ingrese el nombre del doctor al que se le asignara la cita:\n")
    validators.textValidator(doctor, "correo  \n")
    appointmentType = input("ingrese el tipo de cita\n")
    validators.textValidator(appointmentType, "direccion de\n")
    staffAdminService.createClinicalAppointment(hospital,patientId,date,hour, doctor,appointmentType)
    print("Cita medica creada con exito")

def showClinicalAppointment(hospital,id):
    patientId = id
    appointment = staffAdminService.validateClinicalAppointment(hospital,patientId)
    if appointment:
       for appointment in hospital.clinicalAppointment:
            print(f"Cedula Paciente: {appointment.id}")
            print(f"Fecha: {appointment.date}")
            print(f"Hora: {appointment.hour}")
            print(f"Doctor: {appointment.doctor}")
            print(f"Tipo de cita: {appointment.appointmentType}")
            print() 
    else:
        print("No hay citas programadas")


def createBilling(hospital, patientId): 
    doctorName = input("Ingrese el nombre del doctor: ")
    validators.textValidator(doctorName, "nombre del doctor")
    policy = None
    for pol in hospital.policy:
        if pol.patientId == patientId:
            policy = pol
            break

    if policy is None:
        raise Exception("El paciente no tiene ninguna póliza asociada")
    policy = vars(policy)

    
    orders = [order for order in hospital.orders if order.patientId == patientId and order not in hospital.paidOrders]

    totalCost = 0  
   
    for order in orders:
        for procedure in order.procedure:
            totalCost += int(procedure['procedureCost'].replace('.', '').replace(',', ''))
        for medicine in order.medicines:
            totalCost += int(medicine['medicineCost'].replace('.', '').replace(',', ''))
        for diagnostic_help in order.diagnosticHelp:
            totalCost += int(diagnostic_help['diagnosticCost'].replace('.', '').replace(',', ''))
  
    if orders:
        statePolicy = policy['statePolicy']
        copay = 50000 
        if statePolicy == 'activo' and totalCost >= copay:
            totalCost -= copay 
 

    cost = totalCost  
    billing=staffAdminService.createBilling(hospital, patientId, doctorName, policy, orders, cost)
    printBillingDetails(billing)


  
def printBillingDetails(billing):
    print("Detalles de la factura:")
    printPatientDetails(billing)
    printDoctorName(billing.get('doctorName', ''))
    printPolicyDetails(billing.get('policy', {}))
    printOrderDetails(billing.get('order', {}))
    print(f"Costo total: {billing.get('cost', 0)}")

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
    print(f"    Item: {medicine.get('itemMedicine', '')}")
    print(f"    Nombre: {medicine.get('medicineName', '')}")
    print(f"    Dosis: {medicine.get('medicineDose', '')}")
    print(f"    Duración: {medicine.get('durationMedication', '')}")
    print(f"    Costo: {medicine.get('medicineCost', '')}")
    print("")

def printProcedures(procedures):
    if procedures:
        print("  Procedimientos:")
        for procedure in procedures:
            printProcedureDetails(procedure)

def printProcedureDetails(procedure):
    print(f"    Item: {procedure.get('itemProcedure', '')}")
    print(f"    Nombre: {procedure.get('nameProcedure', '')}")
    print(f"    Repetición: {procedure.get('numberRepeated', '')}")
    print(f"    Frecuencia: {procedure.get('frequencyRepeated', '')}")
    print(f"    Costo: {procedure.get('procedureCost', '')}")
    print(f"    Requiere Especialista: {procedure.get('requiresSpecialistP', '')}")
    if procedure.get('requiresSpecialistP', '').lower() == 'si':
        print(f"    ID del Especialista: {procedure.get('specialistId', '')}")
    print("")    

def printDiagnosticHelp(diagnosticHelp):
    if diagnosticHelp:
        print("  Ayudas Diagnósticas:")
        for diagnostic in diagnosticHelp:
            printDiagnosticDetails(diagnostic)

def printDiagnosticDetails(diagnostic):
    print(f"    Item: {diagnostic.get('itemDiagnostic', '')}")
    print(f"    Nombre: {diagnostic.get('nameDiagnostic', '')}")
    print(f"    Cantidad: {diagnostic.get('quantity', '')}")
    print(f"    Costo: {diagnostic.get('diagnosticCost', '')}")
    print(f"    Requiere Especialista: {diagnostic.get('requiresSpecialistD', '')}")
    if diagnostic.get('requiresSpecialistD', '').lower() == 'si':
        print(f"    ID del Especialista: {diagnostic.get('specialistId', '')}")
    print("")

def printPatientDetails(billing):
    print(f"Paciente: {billing.get('patient_name', '')}")
    print(f"Número de ID del paciente: {billing.get('patient_id', '')}")
    print(f"Fecha de nacimiento del paciente: {billing.get('patient_birth', '')}")
    print("")

def printDoctorName(doctorName):
    print(f"Nombre del doctor: {doctorName}")
    print("")

def printPolicyDetails(policy):
    print(f"Compañía de seguros: {policy.get('insuaranceCompany', '')}")
    print(f"Número de póliza: {policy.get('policynumber', '')}")
    print(f"Estado de la póliza: {policy.get('statePolicy', '')}")
    print(f"Término de la póliza: {policy.get('termPolicy', '')}")
    print("")


