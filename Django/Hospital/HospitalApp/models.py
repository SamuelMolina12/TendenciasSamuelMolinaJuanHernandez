
from django.db import models

class Employer(models.Model):
    id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    telephone=models.IntegerField()
    birth=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    role=models.CharField(max_length=30)
    userName=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
class Specialist(models.Model):
    id = models.AutoField(primary_key=True)
    nameSpecialist = models.CharField(max_length=30)

class Patient(models.Model):
    id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    mail=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    telephone=models.IntegerField()
    birth=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    # emergencyContact=[]
    # policy=[]

class EmergencyContact(models.Model):
    id=models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    name=models.CharField(max_length=30)
    relationship=models.CharField(max_length=30)
    telephone=models.CharField(max_length=30)
    

class Policy(models.Model):
    id=models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    insuranceCompany=models.CharField(max_length=30)
    policyNumber=models.CharField(max_length=30)
    statePolicy=models.CharField(max_length=30)
    termPolicy=models.CharField(max_length=30)

class ClinicalAppointment(models.Model):
    id = models.AutoField(primary_key=True)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    date = models.CharField(max_length=30)
    hour = models.CharField(max_length=30)
    doctor = models.CharField(max_length=30)
    appointmentType = models.CharField(max_length=30)

class Order(models.Model):
    
    orderId = models.AutoField(primary_key=True, default=1)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Employer,on_delete=models.CASCADE)
    date = models.DateTimeField()


class Billing(models.Model):
    id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    # patient_name = patientName
    # patient = patient_id
    # patientBirth = patient_birth
    doctorName = models.ForeignKey(Employer,on_delete=models.CASCADE)
    policy =  models.ForeignKey(Policy,on_delete=models.CASCADE)
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    cost = models.FloatField()



class Medicine(models.Model):  
    id= models.AutoField(primary_key=True)   
    # order =models.ForeignKey(Order,on_delete=models.CASCADE)
    # itemMedicine = models.IntegerField()
    medicineName = models.CharField(max_length=30)
    medicineDose = models.CharField(max_length=30)
    durationMedication = models.CharField(max_length=30)
    medicineCost = models.FloatField()


class Procedure(models.Model):
    id=models.AutoField(primary_key=True)
    # order = models.ForeignKey(Order,on_delete=models.CASCADE)
    # itemProcedure = models.IntegerField()
    procedureName =  models.CharField(max_length=30)
    numberRepeated =  models.CharField(max_length=30)
    frequencyRepeated =  models.CharField(max_length=30)
    procedureCost =  models.FloatField()
    requiresSpecialistP = models.BooleanField()
    specialist = models.ForeignKey(Specialist,on_delete=models.CASCADE,null=True)                    


class DiagnosticHelp(models.Model):
    id = models.AutoField(primary_key=True)
    # order = models.ForeignKey(Order,on_delete=models.CASCADE)
    # itemDiagnostic = models.IntegerField()
    diagnosticName = models.CharField(max_length=30)
    quantity = models.CharField(max_length=30)
    diagnosticCost = models.FloatField()
    requiresSpecialistD = models.BooleanField()
    specialist = models.ForeignKey(Specialist,on_delete=models.CASCADE,null=True)  

class Session(models.Model):
    id=models.AutoField(primary_key=True)
    token=models.CharField(max_length=200)
    user=models.ForeignKey(Employer, on_delete=models.CASCADE)
    
    



