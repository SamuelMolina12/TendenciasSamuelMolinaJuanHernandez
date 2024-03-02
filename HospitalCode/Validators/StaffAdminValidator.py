from Validators.TypeValidator import *
import Service.StaffAdminService as staffAdminService

def createPatient(hospital):
    id=numberValidator(input("ingrese la cedula" + "\n"), "cedula de")
    name=input("ingrese el nombre de " + str(id) +"\n")
    textValidator(name,"nombre  " + "\n")
    genre=input("ingrese el genero  " +  "\n")
    textValidator(genre, "genero de " + "\n")
    mail=input("ingrese el correo " +  "\n")
    textValidator(mail, "correo  " + "\n")
    telephone=numberValidator(input("ingrese el numero telefonico " + "\n"),"telefono"  )
    birth=numberValidator(input("ingrese la fecha de nacimiento " + "\n"),"fecha de nacimiento "  )
    address=input("ingrese la direccion " +  "\n")
    textValidator(address, "direccion   " + "\n")
    emergencyContact=input("ingrese el contacto de emergencia  " +  "\n")  
    textValidator(emergencyContact,"contacto de emergencia" +   "\n" ) 
    policy=input("ingrese la poliza  " +  "\n")  
    textValidator(policy,"poliza " +   "\n" )
    clinicHistory=input("historial clinico\n")  
    textValidator(clinicHistory,"historial clinico " +   "\n" )
    print("cumple las validaciones de tipo de dato")
    return staffAdminService.createPatient(hospital,id,name, genre, mail, telephone, birth, address, emergencyContact,policy,clinicHistory)

def showPatient(hospital, id):
    patient = staffAdminService.findPatient(hospital, id)
    if patient:
        print(f"Cedula: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Genero: {patient.genre}")
        print(f"Email: {patient.mail}")
        print(f"Telefono: {patient.telephone}")
        print(f"Fecha de nacimiento: {patient.birth}")
        print(f"Direccion: {patient.address}")
        print(f"Contacto de Emergencia: {patient.emergencyContact}")
        print(f"Poliza: {patient.policy}")
        print(f"Historial Clinico: {patient.clinicHistory}")
        print()
    else:
        print("Paciente no encontrado.")

