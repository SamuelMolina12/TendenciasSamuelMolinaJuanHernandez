import HospitalApp.models as models



#Medicina ---------------
def createMedicine(medicineName, medicineDose, durationMedication, medicineCost):
    dose = models.Medicine.objects.filter(medicineDose=medicineDose,medicineName=medicineName)
    if dose:
        raise Exception("Ya existe una medicina con esa dosis")
   
    medicine = models.Medicine(medicineName=medicineName,medicineDose=medicineDose,durationMedication=durationMedication,medicineCost=medicineCost)
    medicine.save()

def getMedicines():
    medicine = models.Medicine.objects.all()
    if medicine:
        return medicine
    else:
        raise Exception("No hay medicinas para mostrar")


def getMedicine(id):
    medicine = models.Medicine.objects.filter(id=id).first()
    if medicine:
        return medicine
    else:
        raise Exception("No hay una medicina con ese id")

def deleteMedicine(id):
    medicine = models.Medicine.objects.filter(id=id).first()
    if medicine:
        medicine.delete()
    else:
        raise Exception("Medicina no encontrada")

def updateMedicine(id, medicineName, medicineDose, durationMedication, medicineCost):
    medicine = models.Medicine.objects.filter(id=id).first()
    if medicine:
        medicine.medicineName = medicineName
        medicine.medicineDose = medicineDose
        medicine.durationMedication = durationMedication
        medicine.medicineCost = medicineCost
        medicine.save()
    else:
        raise Exception("medicina no encontrada")

#----------------------

#Procedimiento -----------

def createProcedure(procedureName,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):

    procedure = models.Procedure(procedureName=procedureName, numberRepeated=numberRepeated, frequencyRepeated=frequencyRepeated, procedureCost=procedureCost, requiresSpecialistP=requiresSpecialistP, specialistId=specialistId)
    procedure.save()

def getProcedures():
    procedure = models.Procedure.objects.all()
    if procedure:
        return procedure
    else:
        raise Exception("No hay procedimientos para mostrar")


def getProcedure(id):
    procedure = models.Procedure.objects.filter(id=id).first()
    if procedure:
        return procedure
    else:
        raise Exception("No hay una procediemiento con ese id")
    
def deleteProcedure(id):
    procedure = models.Procedure.objects.filter(id=id).first()
    if procedure:
        procedure.delete()
    else:
        raise Exception("procedimiento no encontrado")

def updateProcedure(id,procedureName,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
    procedure = models.Procedure.objects.filter(id=id).first()
    if procedure:
        procedure.procedureName = procedureName
        procedure.numberRepeated = numberRepeated
        procedure.frequencyRepeated = frequencyRepeated
        procedure.procedureCost = procedureCost
        procedure.requiresSpecialistP = requiresSpecialistP
        procedure.specialistId = specialistId        
        procedure.save()
    else:
        raise Exception("procedimiento no encontrado")
#-------------

#Diagnostico de ayuda -----------

def createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialistId):

    diagnosticHelp = models.DiagnosticHelp(diagnosticName=diagnosticName,quantity=quantity,diagnosticCost=diagnosticCost,requiresSpecialistD=requiresSpecialistD,specialistId=specialistId)
    diagnosticHelp.save()

def getDiagnosticaids():
    Diagnostic = models.DiagnosticHelp.objects.all()
    if Diagnostic:
        return Diagnostic
    else:
        raise Exception("No hay ayudas diagnosticas para mostrar")


def getDiagnosticHelp(id):
    Diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
    if Diagnostic:
        return Diagnostic
    else:
        raise Exception("No hay ayuda diagnostica con ese id")
    
def deleteDiagnosticHelp(id):
    diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
    if diagnostic:
        diagnostic.delete()
    else:
        raise Exception("Ayuda diagnostica no encontrada")

def updateDiagnosticHelp(id,diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialistId):
    diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
    if diagnostic:
        diagnostic.diagnosticName = diagnosticName
        diagnostic.quantity = quantity
        diagnostic.diagnosticCost = diagnosticCost
        diagnostic.requiresSpecialistD = requiresSpecialistD
        diagnostic.specialistId = specialistId        
        diagnostic.save()
    else:
        raise Exception("Ayuda diagnostica no encontrada")    
#-------------