import HospitalApp.models as models



#Medicina ---------------
def createMedicine(medicineName, medicineDose, durationMedication, medicineCost):
    dose = models.Medicine.objects.filter(medicineDose=medicineDose,medicineName=medicineName)
    if dose:
        raise Exception("Ya existe una medicina con esa dosis")
   
    medicine = models.Medicine(medicineName=medicineName,medicineDose=medicineDose,durationMedication=durationMedication,medicineCost=medicineCost)
    medicine.save()


#----------------------

#Procedimiento -----------

def createProcedure(nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):

    procedure = models.Procedure(nameProcedure=nameProcedure, numberRepeated=numberRepeated, frequencyRepeated=frequencyRepeated, procedureCost=procedureCost, requiresSpecialistP=requiresSpecialistP, specialistId=specialistId)
    procedure.save()




#-------------

#Diagnostico de ayuda -----------

def createDiagnosticHelp(nameDiagnostic,quantity,diagnosticCost,requiresSpecialistD,specialistId):

    diagnosticHelp = models.DiagnosticHelp(nameDiagnostic=nameDiagnostic,quantity=quantity,diagnosticCost=diagnosticCost,requiresSpecialistD=requiresSpecialistD,specialistId=specialistId)
    diagnosticHelp.save()


#-------------