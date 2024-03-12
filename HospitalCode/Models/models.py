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
        self.emergencyContact=[]
        self.policy=[]
      

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

class ClinicalAppointment():
    def __init__(self,id, date, hour, doctor,appointmentType):
        self.id = id
        self.date = date
        self.hour = hour
        self.doctor = doctor
        self.appointmentType = appointmentType

        
class Billing():
    def __init__(self, patientId, patientName, patient_id, patient_birth, doctorName, policy, order, cost):
        self.patientId = patientId
        self.patient_name = patientName
        self.patient_id = patient_id
        self.patient_birth = patient_birth
        self.doctorName = doctorName
        self.policy = policy
        self.order = order
        self.cost = cost


class Medicine():
    def __init__(self,orderId,itemMedicine,medicineName,medicineDose,durationMedication,medicineCost):       
        self.orderId = orderId
        self.itemMedicine = itemMedicine
        self.medicineName = medicineName
        self.medicineDose = medicineDose
        self.durationMedication = durationMedication
        self.medicineCost = medicineCost


class Procedure():
    def __init__(self,orderId,itemProcedure,nameProcedure,numberRepeated,frequencyRepeated,procedureCost,requiresSpecialistP,specialistId):
        self.orderId = orderId
        self.itemProcedure = itemProcedure
        self.nameProcedure = nameProcedure
        self.numberRepeated = numberRepeated
        self.frequencyRepeated = frequencyRepeated
        self.procedureCost = procedureCost
        self.requiresSpecialistP = requiresSpecialistP
        self.specialistId = specialistId                    


class DiagnosticHelp():
    def __init__(self, orderId, itemDiagnostic, nameDiagnostic,quantity, diagnosticCost, requiresSpecialistD, specialistId):
        self.orderId = orderId
        self.itemDiagnostic = itemDiagnostic
        self.nameDiagnostic = nameDiagnostic
        self.quantity = quantity
        self.diagnosticCost = diagnosticCost
        self.requiresSpecialistD = requiresSpecialistD
        self.specialistId = specialistId


class Order():
    def __init__(self, orderId, patientId, doctorId,date,diagnosticHelp,medicines,procedure):
        self.orderId = orderId
        self.patientId = patientId
        self.doctorId = doctorId
        self.date = date
        self.medicines = medicines
        self.procedure = procedure
        self.diagnosticHelp = diagnosticHelp
        



class Hospital():
    def __init__(self):
        self.persons = [] 
        self.patient = [] 
        self.orders = []
        self.clinicalAppointment= []   
        self.emergencyContact=[]
        self.policy = []   
        self.historyVisits = {}   
        self.historyClinic = {}
        self.medicines = []
        self.diagnosticHelp = []
        self.procedures = []