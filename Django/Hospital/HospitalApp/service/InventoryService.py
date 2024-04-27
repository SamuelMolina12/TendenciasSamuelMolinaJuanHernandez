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

def updateDiagnosticHelp(id, diagnosticName, quantity, diagnosticCost, requiresSpecialistD, specialist_id):
    if specialist_id is not None:
        specialist = models.Specialist.objects.filter(id=specialist_id).first()
        if not specialist:
            raise Exception("No existe un especialista con ese id")
    else:
        specialist = None

    diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
    if diagnostic:
        diagnostic.diagnosticName = diagnosticName
        diagnostic.quantity = quantity
        diagnostic.diagnosticCost = diagnosticCost
        diagnostic.requiresSpecialistD = requiresSpecialistD
        diagnostic.specialist = specialist  
        diagnostic.save()
    else:
        raise Exception("Ayuda diagnostica no encontrada")
    
#-------------


# def createMedicine(medicineName,medicineCost,medicineQuantity):
#     dose = models.Medicine.objects.filter(medicineQuantity=medicineQuantity,medicineName=medicineName)
#     if dose:
#         raise Exception("Ya existe una medicina con esa cantidad")
   
#     medicine = models.Medicine(medicineName=medicineName,medicineQuantity=medicineQuantity,medicineCost=medicineCost)
#     medicine.save()

# def getMedicines():
#     medicine = models.Medicine.objects.all()
#     if medicine:
#         return medicine
#     else:
#         raise Exception("No hay medicinas para mostrar")


# def getMedicine(id):
#     medicine = models.Medicine.objects.filter(id=id).first()
#     if medicine:
#         return medicine
#     else:
#         raise Exception("No hay una medicina con ese id")

# def deleteMedicine(id):
#     medicine = models.Medicine.objects.filter(id=id).first()
#     if medicine:
#         medicine.delete()
#     else:
#         raise Exception("Medicina no encontrada")

# def updateMedicine(id, medicineName,medicineCost,medicineQuantity):
#     medicine = models.Medicine.objects.filter(id=id).first()
#     if medicine:
#         medicine.medicineName = medicineName
#         medicine.medicineCost = medicineCost
#         medicine.medicineQuantity = medicineQuantity        
#         medicine.save()
#     else:
#         raise Exception("medicina no encontrada")

# #----------------------

# #Procedimiento -----------

# def createProcedure(procedureName,procedureCost,requiresSpecialistP,specialist_id):
#     if not specialist_id  is None:
#         procedure = models.Specialist.objects.filter(id=specialist_id)
#         if not procedure:
#            raise Exception("No existe un especialista con ese id") 
       
#     procedure = models.Procedure(procedureName=procedureName, numberRepeated=numberRepeated, frequencyRepeated=frequencyRepeated, procedureCost=procedureCost, requiresSpecialistP=requiresSpecialistP, specialist_id=specialist_id)
#     procedure.save()

# def getProcedures():
#     procedure = models.Procedure.objects.all()
#     if procedure:
#         return procedure
#     else:
#         raise Exception("No hay procedimientos para mostrar")


# def getProcedure(id):
#     procedure = models.Procedure.objects.filter(id=id).first()
#     if procedure:
#         return procedure
#     else:
#         raise Exception("No hay una procediemiento con ese id")
    
# def deleteProcedure(id):
#     procedure = models.Procedure.objects.filter(id=id).first()
#     if procedure:
#         procedure.delete()
#     else:
#         raise Exception("procedimiento no encontrado")

# def updateProcedure(id, procedureName, numberRepeated, frequencyRepeated, procedureCost, requiresSpecialistP, specialist_id):
#     if specialist_id is not None:
#         specialist = models.Specialist.objects.filter(id=specialist_id).first()
#         if not specialist:
#             raise Exception("No existe un especialista con ese id")
#     else:
#         specialist = None

#     procedure = models.Procedure.objects.filter(id=id).first()
#     if procedure:
#         procedure.procedureName = procedureName
#         procedure.numberRepeated = numberRepeated
#         procedure.frequencyRepeated = frequencyRepeated
#         procedure.procedureCost = procedureCost
#         procedure.requiresSpecialistP = requiresSpecialistP
#         procedure.specialist = specialist 
#         procedure.save()
#     else:
#         raise Exception("Procedimiento no encontrado")

# #-------------

# #Diagnostico de ayuda -----------

# def createDiagnosticHelp(diagnosticName,quantity,diagnosticCost,requiresSpecialistD,specialist_id):
#     if not specialist_id  is None:
#         diagnosticHelp = models.Specialist.objects.filter(id=specialist_id)
#         if not diagnosticHelp:
#            raise Exception("No existe un especialista con ese id")
#     diagnosticHelp = models.DiagnosticHelp(diagnosticName=diagnosticName,quantity=quantity,diagnosticCost=diagnosticCost,requiresSpecialistD=requiresSpecialistD,specialist_id=specialist_id)
#     diagnosticHelp.save()

# def getDiagnosticaids():
#     Diagnostic = models.DiagnosticHelp.objects.all()
#     if Diagnostic:
#         return Diagnostic
#     else:
#         raise Exception("No hay ayudas diagnosticas para mostrar")


# def getDiagnosticHelp(id):
#     Diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
#     if Diagnostic:
#         return Diagnostic
#     else:
#         raise Exception("No hay ayuda diagnostica con ese id")
    
# def deleteDiagnosticHelp(id):
#     diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
#     if diagnostic:
#         diagnostic.delete()
#     else:
#         raise Exception("Ayuda diagnostica no encontrada")

# def updateDiagnosticHelp(id, diagnosticName, quantity, diagnosticCost, requiresSpecialistD, specialist_id):
#     if specialist_id is not None:
#         specialist = models.Specialist.objects.filter(id=specialist_id).first()
#         if not specialist:
#             raise Exception("No existe un especialista con ese id")
#     else:
#         specialist = None

#     diagnostic = models.DiagnosticHelp.objects.filter(id=id).first()
#     if diagnostic:
#         diagnostic.diagnosticName = diagnosticName
#         diagnostic.quantity = quantity
#         diagnostic.diagnosticCost = diagnosticCost
#         diagnostic.requiresSpecialistD = requiresSpecialistD
#         diagnostic.specialist = specialist  
#         diagnostic.save()
#     else:
#         raise Exception("Ayuda diagnostica no encontrada")