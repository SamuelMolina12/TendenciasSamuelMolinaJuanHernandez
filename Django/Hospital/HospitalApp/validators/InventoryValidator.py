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
    return infoService.getMedicine(id)

def getMedicines():
    return infoService.getMedicines()

def deleteMedicine(id):
    return infoService.deleteMedicine(id) 

def updateMedicine(id,medicineName,medicineCost,medicineQuantity):
    
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
    return infoService.getProcedure(id)

def getProcedures():
    return infoService.getProcedures()  

def deleteProcedure(id):
    return infoService.deleteProcedure(id) 


def updateProcedure(id,procedureName,procedureCost):
    validators.textValidator(procedureName, "procedimiento")

    procedureCost = float(procedureCost)

    return infoService.updateProcedure(id, procedureName,procedureCost) 
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


# def createMedicine(medicineName,medicineCost,medicineQuantity):
#     validators.textValidator(medicineName,"medicina\n")
  
#     medicineCost = float(medicineCost)
#     # validators.costValidator(medicineCost,"costo")

#     validators.textValidator(medicineQuantity, "cantidad de la medicina ") 

#     infoService.createMedicine(medicineName,medicineCost,medicineQuantity)

# def getMedicine(id):
#     return infoService.getMedicine(id)

# def getMedicines():
#     return infoService.getMedicines()

# def deleteMedicine(id):
#     return infoService.deleteMedicine(id) 

# def updateMedicine(id,medicineName,medicineCost,medicineQuantity):
    
#     validators.textValidator(medicineName,"medicina\n")
  
#     medicineCost = float(medicineCost)
#     # validators.costValidator(medicineCost,"costo")

#     validators.textValidator(medicineQuantity, "cantidad de la medicina ") 

#     return infoService.updateMedicine(id, medicineName,medicineCost,medicineQuantity)   

# #----------------------




# #Procedimiento -----------
# def createProcedure(procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id):
#     validators.textValidator(procedureName, "procedimiento")
#     validators.textValidator(numberRepeated, "numero")
#     validators.textValidator(frequencyRepeated, "frecuencia ")  

#     if requiresSpecialistP:
#         validators.numberValidator(specialist_id, "id especialista")
#     else:  
#         specialist_id = None

#     procedureCost = float(procedureCost)
    
#     infoService.createProcedure(procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id)

# def getProcedure(id):
#     return infoService.getProcedure(id)

# def getProcedures():
#     return infoService.getProcedures()  

# def deleteProcedure(id):
#     return infoService.deleteProcedure(id) 


# def updateProcedure(id,procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id):
#     validators.textValidator(procedureName, "procedimiento")
#     validators.textValidator(numberRepeated, "numero")
#     validators.textValidator(frequencyRepeated, "frecuencia ")  

#     if requiresSpecialistP:
#         validators.numberValidator(specialist_id, "id especialista")
#     else:  
#         specialist_id = None

#     procedureCost = float(procedureCost)

#     return infoService.updateProcedure(id, procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id) 
# #----------------------



# # #Ayuda diagnostica -----------
# # def createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id):
# #     validators.textValidator(diagnosticName, "procedimiento")
# #     validators.textValidator(quantity, "cantidad") 

# #     if requiresSpecialistD:
# #         validators.numberValidator(specialist_id, "id especialista")
# #     else:  
# #         specialist_id = None

# #     diagnosticCost = float(diagnosticCost)
    
# #     infoService.createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id)


# # def getDiagnosticHelp(id):
# #     return infoService.getDiagnosticHelp(id)

# # def getDiagnosticaids():
# #     return infoService.getDiagnosticaids()  

# # def deleteDiagnosticHelp(id):
# #     return infoService.deleteDiagnosticHelp(id) 

# # def updateDiagnosticHelp(id,diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id):
# #     validators.textValidator(diagnosticName, "procedimiento")
# #     validators.textValidator(quantity, "cantidad") 

# #     if requiresSpecialistD:
# #         validators.numberValidator(specialist_id, "id especialista")
# #     else:  
# #         specialist_id = None

# #     diagnosticCost = float(diagnosticCost)

# #     return infoService.updateDiagnosticHelp(id,diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id)