import datetime

class Employer():
     def __init__(self,name,id,genre,mail,telephone,birth,address,role,userName,password):
        self.name=name
        self.id=id
        self.genre=genre
        self.mail=mail
        self.telephone=telephone
        self.birth=birth
        self.address=address
        self.role=role
        self.userName=userName
        self.password=password

class Patient():
     def __init__(self,id,name,genre,mail,telephone,birth,address):
        self.id=id
        self.name=name
        self.mail=mail
        self.genre=genre
        self.telephone=telephone
        self.birth=birth
        self.address=address
        self.emergencyContact=EmergencyContact
        self.policy=Policy
      

class EmergencyContact():
    def __init__(self,patientId,name,relationship,telephone):
        self.patientId=patientId
        self.name=name
        self.relationship=relationship
        self.telephone=telephone

        
class Policy():
    def __init__(self,patientId,insuranceCompany,policynumber,statePolicy,termPolicy):
        self.patientId=patientId
        self.insuaranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.termPolicy=termPolicy

        
class Billing():
    def __init__(self,patientId):
        self.patientId=patientId
        self.Poliicy=Policy
       

class Medicine():
    def __init__(self,numberOrderM,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost):       
        self.numberOrderM = numberOrderM
        self.itemMedicine = itemMedicine
        self.medicineName = medicineName
        self.medicineDose = medicineDose
        self.durationMedication = durationMedication
        self.medicineCost = medicineCost


class Procedure():
    def __init__(self,numberOrderP,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
        self.numberOrderP = numberOrderP
        self.itemProcedure = itemProcedure
        self.nameProcedure = nameProcedure
        self.numberRepeated = numberRepeated
        self.frequencyRepeated = frequencyRepeated
        self.procedureCost = procedureCost
        self.requiresSpecialistP = requiresSpecialistP
        self.specialistId = specialistId                    


class DiagnosticHelp():
    def __init__(self, numberOrderD, itemDiagnostic, nameDiagnostic,quantity, diagnosticCost, requiresSpecialistD, specialistId):
        self.numberOrderD = numberOrderD
        self.itemDiagnostic = itemDiagnostic
        self.nameDiagnostic = nameDiagnostic
        self.quantity = quantity
        self.diagnosticCost = diagnosticCost
        self.requiresSpecialistD = requiresSpecialistD
        self.specialistId = specialistId


class Order():
    def __init__(self, orderId, patientId, doctorId):
        self.orderId = orderId
        self.patientId = patientId
        self.doctorId = doctorId
        self.date = datetime.datetime.now()
        self.Medicines = []
        self.Procedure = []
        self.DiagnosticHelp = []



class Hospital():
    def __init__(self):
        self.persons = [] 
        self.patient = [] 
        self.orders = []       
        self.historyVisits = {}   
        self.historyClinic = {}