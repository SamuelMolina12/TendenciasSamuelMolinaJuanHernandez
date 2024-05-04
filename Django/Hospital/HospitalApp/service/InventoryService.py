import HospitalApp.models as models



#Medicina ---------------
def createMedicine(medicineName,medicineCost,medicineQuantity):
    dose = models.Medicine.objects.filter(medicineQuantity=medicineQuantity,medicineName=medicineName)
    if dose:
        raise Exception("Ya existe una medicina con esa cantidad")
   
    medicine = models.Medicine(medicineName=medicineName,medicineQuantity=medicineQuantity,medicineCost=medicineCost)
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

def updateMedicine(id, medicineName,medicineCost,medicineQuantity):
    medicine = models.Medicine.objects.filter(id=id).first()
    if medicine:
        medicine.medicineName = medicineName
        medicine.medicineCost = medicineCost
        medicine.medicineQuantity = medicineQuantity        
        medicine.save()
    else:
        raise Exception("medicina no encontrada")

#----------------------

#Procedimiento -----------

def createProcedure(procedureName,procedureCost):

       
    procedure = models.Procedure(procedureName=procedureName, procedureCost=procedureCost)
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

def updateProcedure(id, procedureName, procedureCost, ):

    procedure = models.Procedure.objects.filter(id=id).first()
    if procedure:
        procedure.procedureName = procedureName
        procedure.procedureCost = procedureCost
        procedure.save()
    else:
        raise Exception("Procedimiento no encontrado")

#-------------

#Diagnostico de ayuda -----------

def createDiagnosticHelp(diagnosticName,diagnosticCost):
    prodecure = models.DiagnosticHelp.objects.filter(diagnosticName=diagnosticName,diagnosticCost=diagnosticCost).first()
    if prodecure:
        raise Exception("Ya existe una ayuda diagnostica con ese nombre y costo")

    diagnosticHelp = models.DiagnosticHelp(diagnosticName=diagnosticName,diagnosticCost=diagnosticCost)
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

def updateDiagnosticHelp(id, diagnosticName,  diagnosticCost ):
    prodecure = models.DiagnosticHelp.objects.filter(diagnosticName=diagnosticName,diagnosticCost=diagnosticCost).exclude(id=id).first()
    if prodecure:
        raise Exception("Ya existe una ayuda diagnostica con ese nombre y costo")
    
    diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
    if diagnostic:
        diagnostic.diagnosticName = diagnosticName
        diagnostic.diagnosticCost = diagnosticCost
  
        diagnostic.save()
    else:
        raise Exception("Ayuda diagnostica no encontrada")
    
#-------------


