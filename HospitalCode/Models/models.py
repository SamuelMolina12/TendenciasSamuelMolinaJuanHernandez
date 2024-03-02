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
     def __init__(self,id,name,genre,mail,telephone,birth,address,emergencyContact,policy,clinicHistory):
        self.id=id
        self.name=name
        self.mail=mail
        self.genre=genre
        self.telephone=telephone
        self.birth=birth
        self.address=address
        self.emergencyContact=emergencyContact
        self.policy=policy
        self.clinicHistory=clinicHistory

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
    def __init__(self,name,age, patientId,doctor,insuranceCompany,policynumber,statePolicy,termPolicy):
        self.name=name
        self.age=age
        self.patientId=patientId
        self.doctor=doctor
        self.insuaranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.termPolicy=termPolicy


class HistoryVisits():
    def __init__(self,patient,bloodPressure,temperature,pulse,oxygenBlood):
        self.patient=patient
        self.bloodPreasurre=bloodPressure
        self.temperature=temperature
        self.pulse=pulse
        self.oxygenBlood=oxygenBlood
        self.date=datetime.datetime.now


                  




class Hospital():
    def __init__(self):
        self.persons = [] 
        self.patient = [] 
        self.clinicHistory = []  
        self.diagnostic = []  
        self.diagnosticHelp = []  
        self.procedure = []  
        self.historyVisits = [] 
        self.billing = []  
        self.policy = []  
      