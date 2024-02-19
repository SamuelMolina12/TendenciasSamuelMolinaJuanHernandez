from Validators.typeValidator import *
import Service.AdminService as adminService


def createAdmin(hospital,role):
    name=input("ingrese nombre del " + role)
    TextValidator(name,"nombre de " + role)
    id=NumberValidator(input("ingrese la cedula de " + role), "cedula de " + role)
    username=input("ingrese usuario del " + role)
    TextValidator(name,"usuario de " + role) 
    genre=input("ingrese el genero" + role)
    TextValidator(name, "genero de " +role)
    mail=input("ingrese el correo" + role)
    TextValidator(name, "correo de " +role)
    telephone=input("ingrese el telefono" + role)
    TextValidator(name, "telefono  de " +role)
    birth=NumberValidator(input("ingrese la fecha de nacimiento" + role),"fecha de nacimiento de" + role)
    address=input("ingrese la direccion" + role)
    TextValidator(name, "direccion de  " +role)
    role=input("ingrese el genero" + role)
    TextValidator(name, "genero de " +role)
    password=input("ingrese contraseña del " + role)
    PasswordValidator(name,"contraseña de " + role)
    adminService.createAdmin(hospital,name,id,genre,mail,telephone,birth,address,role,username,password)
    