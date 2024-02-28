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
     def __init__(self,name,id,mail,telephone,birth,address,emergencyContact,clinicHistory):
        self.name=name
        self.id=id
        self.mail=mail
        self.telephone=telephone
        self.birth=birth
        self.address=address
        self.emergencyContact=emergencyContact
        self.clinicHistory=clinicHistory

class EmergencyContact():
    def __init__(self,name,relationship,telephone):
        self.name=name
        self.relationship=relationship
        self.telephone=telephone

        
class Policy():
    def __init__(self,insuranceCompany,policynumber,statePolicy,termPolicy):
        
        self.insuaranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.termPolicy=termPolicy

        
class Billing():
    def __init__(self,name,age, id,doctor,insuranceCompany,policynumber,statePolicy,termPolicy):
        self.name=name
        self.age=age
        self.id=id
        self.doctor=doctor
        self.insuaranceCompany=insuranceCompany
        self.policynumber=policynumber
        self.statePolicy=statePolicy
        self.termPolicy=termPolicy


class HistoryVisits():
    def __init__(self,pacient,bloodPressure,temperature,pulse,oxygenBlood):
        self.pacient=pacient
        self.bloodPreasurre=bloodPressure
        self.temperature=temperature
        self.pulse=pulse
        self.oxygenBlood=oxygenBlood
        self.date=datetime.datetime.now


                  




class Hospital():
    def __init__(self):
        self.persons = []  
        self.clinicHistory = []  
        self.diagnostic = []  
        self.diagnosticHelp = []  
        self.procedure = []  
        self.historyVisits = [] 
        self.billing = []  
        self.policy = []  
      