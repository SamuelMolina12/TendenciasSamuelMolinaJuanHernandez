from Validators.TypeValidator import *
import Service.AdminService as adminService


def createUser(hospital,role):

    name=input("ingrese nombre del " + role + "\n")
    TextValidator(name,"nombre de " + role  + "\n")
    id=NumberValidator(input("ingrese la cedula de " + role + "\n"), "cedula de " + role )
    username=input("ingrese usuario del " + role  + "\n")
    TextValidator(name,"usuario de " + role  + "\n" ) 
    genre=input("ingrese el genero " + role  + "\n")
    TextValidator(name, "genero de " +role  + "\n")
    mail=input("ingrese el correo " + role  + "\n")
    TextValidator(name, "correo de " +role  + "\n")
    telephone=input("ingrese el telefono " + role  + "\n")
    TextValidator(name, "telefono  de " +role  + "\n")
    birth=NumberValidator(input("ingrese la fecha de nacimiento " + role + "\n"),"fecha de nacimiento de" + role  )
    address=input("ingrese la direccion " + role  + "\n")
    TextValidator(name, "direccion de  " +role  + "\n")
    role=input("ingrese el rol " + role  + "\n")
    TextValidator(name, "genero de " +role  + "\n")
    password=input("Ingrese contraseña del " + role + "\n")
    PasswordValidator(password, "contraseña de " + role + "\n")
    adminService.createAdmin(hospital, name, id, genre, mail, telephone, birth, address, role, username, password)
    