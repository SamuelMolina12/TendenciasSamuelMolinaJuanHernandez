import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.InfoSupportService as infoService



#Medicina ---------------
def createMedicine(medicineName,medicineDose,durationMedication,medicineCost):
    validators.textValidator(medicineName,"medicina\n")

    validators.textValidator(medicineDose,"dosis de la medicina " )

    validators.textValidator(durationMedication, "duracion de la medicacion ")
    medicineCost = float(medicineCost)
    # validators.costValidator(medicineCost,"costo")
    
    infoService.createMedicine(medicineName,medicineDose,durationMedication,medicineCost)

def getMedicine(id):
    return infoService.getMedicine(id)

def getMedicines():
    return infoService.getMedicines()

def deleteMedicine(id):
    return infoService.deleteMedicine(id) 

def updateMedicine(id,medicineName,medicineDose,durationMedication,medicineCost):
    validators.textValidator(medicineName,"medicina\n")

    validators.textValidator(medicineDose,"dosis de la medicina " )

    validators.textValidator(durationMedication, "duracion de la medicacion ")
    medicineCost = float(medicineCost)
    # validators.costValidator(medicineCost,"costo")

    return infoService.updateMedicine(id, medicineName,medicineDose,durationMedication,medicineCost)   

#----------------------




#Procedimiento -----------
def createProcedure(procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id):
    validators.textValidator(procedureName, "procedimiento")
    validators.textValidator(numberRepeated, "numero")
    validators.textValidator(frequencyRepeated, "frecuencia ")  

    if requiresSpecialistP:
        validators.numberValidator(specialist_id, "id especialista")
    else:  
        specialist_id = None

    procedureCost = float(procedureCost)
    
    infoService.createProcedure(procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id)

def getProcedure(id):
    return infoService.getProcedure(id)

def getProcedures():
    return infoService.getProcedures()  

def deleteProcedure(id):
    return infoService.deleteProcedure(id) 


def updateProcedure(id,procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id):
    validators.textValidator(procedureName, "procedimiento")
    validators.textValidator(numberRepeated, "numero")
    validators.textValidator(frequencyRepeated, "frecuencia ")  

    if requiresSpecialistP:
        validators.numberValidator(specialist_id, "id especialista")
    else:  
        specialist_id = None

    procedureCost = float(procedureCost)

    return infoService.updateProcedure(id, procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id) 
#----------------------



#Ayuda diagnostica -----------
def createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id):
    validators.textValidator(diagnosticName, "procedimiento")
    validators.textValidator(quantity, "cantidad") 

    if requiresSpecialistD:
        validators.numberValidator(specialist_id, "id especialista")
    else:  
        specialist_id = None

    diagnosticCost = float(diagnosticCost)
    
    infoService.createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id)


def getDiagnosticHelp(id):
    return infoService.getDiagnosticHelp(id)

def getDiagnosticaids():
    return infoService.getDiagnosticaids()  

def deleteDiagnosticHelp(id):
    return infoService.deleteDiagnosticHelp(id) 

def updateDiagnosticHelp(id,diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id):
    validators.textValidator(diagnosticName, "procedimiento")
    validators.textValidator(quantity, "cantidad") 

    if requiresSpecialistD:
        validators.numberValidator(specialist_id, "id especialista")
    else:  
        specialist_id = None

    diagnosticCost = float(diagnosticCost)

    return infoService.updateDiagnosticHelp(id,diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id) 
#----------------------