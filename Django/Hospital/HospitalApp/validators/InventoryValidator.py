import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.InventoryService as infoService



#Medicina ---------------
def createMedicine(medicineName,medicineCost,medicineQuantity):
    validators.textValidator(medicineName,"medicina\n")
  
    medicineCost = float(medicineCost)
    # validators.costValidator(medicineCost,"costo")

    validators.textValidator(medicineQuantity, "cantidad de la medicina ") 

    infoService.createMedicine(medicineName,medicineCost,medicineQuantity)

def getMedicine(id):
    validators.numberValidator(id, "id de la medicina")
    return infoService.getMedicine(id)

def getMedicines():
    return infoService.getMedicines()

def deleteMedicine(id):
    validators.numberValidator(id, "id de la medicina")
    return infoService.deleteMedicine(id) 

def updateMedicine(id,medicineName,medicineCost,medicineQuantity):
    validators.numberValidator(id, "id de la medicina")        
    validators.textValidator(medicineName,"medicina\n")
  
    medicineCost = float(medicineCost)
    # validators.costValidator(medicineCost,"costo")

    validators.textValidator(medicineQuantity, "cantidad de la medicina ") 

    return infoService.updateMedicine(id, medicineName,medicineCost,medicineQuantity)   

#----------------------




#Procedimiento -----------
def createProcedure(procedureName,procedureCost):

    validators.textValidator(procedureName, "procedimiento")

    procedureCost = float(procedureCost)
    
    infoService.createProcedure(procedureName,procedureCost)

def getProcedure(id):
    validators.numberValidator(id, "id del procedimiento")
    return infoService.getProcedure(id)

def getProcedures():
    return infoService.getProcedures()  

def deleteProcedure(id):
    validators.numberValidator(id, "id del procedimiento")
    return infoService.deleteProcedure(id) 


def updateProcedure(id,procedureName,procedureCost):
    validators.numberValidator(id, "id del procedimiento")
    validators.textValidator(procedureName, "procedimiento")

    procedureCost = float(procedureCost)

    return infoService.updateProcedure(id, procedureName,procedureCost) 
#----------------------



#Ayuda diagnostica -----------
def createDiagnosticHelp(diagnosticName,diagnosticCost):
    validators.textValidator(diagnosticName, "procedimiento")
  


    diagnosticCost = float(diagnosticCost)
    
    infoService.createDiagnosticHelp(diagnosticName,diagnosticCost)


def getDiagnosticHelp(id):
    validators.numberValidator(id, "id de la ayuda diagnostica")
    return infoService.getDiagnosticHelp(id)

def getDiagnosticaids():
    return infoService.getDiagnosticaids()  

def deleteDiagnosticHelp(id):
    validators.numberValidator(id, "id de la ayuda diagnostica")
    return infoService.deleteDiagnosticHelp(id) 

def updateDiagnosticHelp(id,diagnosticName,diagnosticCost):
    validators.numberValidator(id, "id de la ayuda diagnostica")
    validators.textValidator(diagnosticName, "procedimiento")

    diagnosticCost = float(diagnosticCost)

    return infoService.updateDiagnosticHelp(id,diagnosticName,diagnosticCost) 
#----------------------


