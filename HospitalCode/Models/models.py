import datetime

class Employer():
     def __init__(self,name,id,genre,mail,telephone,birth,address,role,username,password):
        self.name=name
        self.id=id
        self.genre=genre
        self.mail=mail
        self.telephone=telephone
        self.birth=birth
        self.address=address
        self.role=role
        self.username=username
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

class Diagnostic():
    def __init__(self,patient,description,medicine,cost,dose,procedure,exam):
       self.patient=patient
       self.description=description
       self.medicine=medicine
       self.cost=cost
       self.dose=dose
       self.procedure=procedure
       self.exam=exam 

class HistoryVisits():
    def __init__(self,pacient,bloodPressure,temperature,pulse,oxygenBlood):
        self.pacient=pacient
        self.bloodPreasurre=bloodPressure
        self.temperature=temperature
        self.pulse=pulse
        self.oxygenBlood=oxygenBlood
        self.date=datetime.datetime.now

class ClinicHistory():
    def __init__(self,doctorId,reason,symptoms,billing):
        self.date=datetime.datetime.now
        self.doctorId=doctorId
        self.reason=reason
        self.symptoms=symptoms
        self.billing=billing
                  
class Procedure():
    def __init__ (self,orderNumber,id,quantity,frequency,assistance,specialistId,item):
        self.orderNumber=orderNumber
        self.id=id
        self.quantity=quantity
        self.frequency=frequency
        self.assistance=assistance
        self.specialistId=specialistId
        self.item=item

class  DiagnosticHelp():
    def __init__(self,orderNumber,id,quantity,assistance,specialistId,item):
        self.orderNumber=orderNumber
        self.id=id
        self.quantity=quantity
        self.assistance=assistance
        self.specialistId=specialistId
        self.item=item


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
      