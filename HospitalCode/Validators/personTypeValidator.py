from Validators.typeValidator import *
import Service.AdminService as adminService

def createUser(hospital,role):
    print("Ingreso a la creacion del rol " + role)
    name=input("ingrese el nombre " + "\n")
    TextValidator(name,"nombre de " + role  + "\n")
    id=NumberValidator(input("ingrese la cedula  " + "\n"), "cedula de " + role )
    username=input("ingrese el usuario  " +  "\n")
    TextValidator(name,"usuario de " + role  + "\n" ) 
    genre=input("ingrese el genero " +  "\n")
    TextValidator(name, "genero de " +role  + "\n")
    mail=input("ingrese el correo " +  "\n")
    TextValidator(name, "correo de " +role  + "\n")
    telephone=input("ingrese el numero tlefonico "   + "\n")
    TextValidator(name, "telefono  de " +role  + "\n")
    birth=NumberValidator(input("ingrese la fecha de nacimiento " + "\n"),"fecha de nacimiento de" + role  )
    address=input("ingrese la direccion " +  "\n")
    TextValidator(name, "direccion de  " +role  + "\n")
    role=role
    TextValidator(name, "genero de " +role  + "\n")
    password=input("Ingrese la contraseña  " + "\n")
    PasswordValidator(password, "contraseña de " + role + "\n")
    adminService.createAdmin(hospital, name, id, genre, mail, telephone, birth, address, role, username, password)
    
def ShowUsers(hospital,role):
    allUsers = hospital.persons
    for user in allUsers:
        if user.role == role:
            print(f"Nombre: {user.name}")
            print(f"Cedula: {user.id}")
            print(f"genero: {user.genre}")
            print(f"Email: {user.mail}")
            print(f"Telefono: {user.telephone}")
            print(f"Fecha de nacimiento: {user.birth}")
            print(f"Direccion: {user.address}")
            print(f"Rol: {user.role}")
            print(f"Usuario: {user.username}")
            print(f"")

           
def DeleteUser(hospital, id):
    id = int(id)  
    if adminService.DeleteUser(hospital, id):
        for i, user in enumerate(hospital.persons):
            if user.id == id:
                del hospital.persons[i]
                print("Usuario eliminado exitosamente.")
                return
    else:
        print("No se encontró ningún usuario con esa identificación.")