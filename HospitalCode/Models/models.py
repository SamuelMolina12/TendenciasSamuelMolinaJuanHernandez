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
       

# class HistoryVisits():
#     def __init__(self,patientId,patientName,nurse,bloodPressure,temperature,pulse,oxygenBlood):
#         self.patient=patientId
#         self.patientName=patientName
#         self.nurse = nurse
#         self.bloodPreasurre=bloodPressure
#         self.temperature=temperature
#         self.pulse=pulse
#         self.oxygenBlood=oxygenBlood
       


                  




class Hospital():
    def __init__(self):
        self.persons = [] 
        self.patient = [] 
        self.emergencyContact = []  
        self.diagnostic = []  
        self.diagnosticHelp = []  
        self.procedure = []  
        self.historyVisits = {}
        self.billing = []  
        self.policy = []  
        self.clinicHistory = {}