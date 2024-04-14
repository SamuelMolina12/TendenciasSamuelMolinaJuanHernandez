import HospitalApp.validators.TypeValidator as validators
import HospitalApp.service.InfoSupportService as infoService



#Medicina ---------------
def createMedicine(medicineName,medicineDose,durationMedication,medicineCost):
   

    validators.textValidator(medicineName,"medicina\n")

    validators.textValidator(medicineDose,"usuario de   \n" )

    validators.textValidator(durationMedication, "genero de    \n")
    medicineCost = float(medicineCost)
    # validators.costValidator(medicineCost,"costo")
    
    infoService.createMedicine(medicineName,medicineDose,durationMedication,medicineCost)

#----------------------




#Procedimiento -----------
def createProcedure(nameProcedure, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialistId):
    validators.textValidator(nameProcedure, "procedimiento")
    validators.textValidator(numberRepeated, "numero")
    validators.textValidator(frequencyRepeated, "frecuencia ")  

    if requiresSpecialistP:
        validators.numberValidator(specialistId, "id especialista")
    else:  
        specialistId = "N/A"

    procedureCost = float(procedureCost)
    
    infoService.createProcedure(nameProcedure, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialistId)




#----------------------



#Ayuda diagnostica -----------
def createDiagnosticHelp(nameDiagnostic,quantity,diagnosticCost,requiresSpecialistD,specialistId):
    validators.textValidator(nameDiagnostic, "procedimiento")
    validators.textValidator(quantity, "numero") 

    if requiresSpecialistD:
 
        validators.numberValidator(specialistId, "id especialista")
    else:      
        specialistId = "N/A"

    diagnosticCost = float(diagnosticCost)
    
    infoService.createDiagnosticHelp(nameDiagnostic,quantity,diagnosticCost,requiresSpecialistD,specialistId)




#----------------------