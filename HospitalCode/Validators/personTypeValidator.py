from Validators.TypeValidator import *
import Service.AdminService as adminService

<<<<<<< HEAD
def createUser(hospital,role):
    print("Ingreso a la creacion del rol " + role)
    name=input("ingrese el nombre " + "\n")
    textValidator(name,"nombre de " + role  + "\n")
    id=numberValidator(input("ingrese la cedula  " + "\n"), "cedula de " + role )
    userName=input("ingrese el usuario  " +  "\n")
    textValidator(userName,"usuario de " + role  + "\n" ) 
    genre=input("ingrese el genero " +  "\n")
    textValidator(genre, "genero de " +role  + "\n")
    mail=input("ingrese el correo " +  "\n")
    textValidator(mail, "correo de " +role  + "\n")
    telephone=numberValidator(input("ingrese el numero telefonico " + "\n"),"fecha de nacimiento de" + role  )
    birth=numberValidator(input("ingrese la fecha de nacimiento " + "\n"),"fecha de nacimiento de" + role  )
    address=input("ingrese la direccion " +  "\n")
    textValidator(address, "direccion de  " +role  + "\n")
    role=role
    textValidator(role, "rol de " +role  + "\n")
    password=input("Ingrese la contraseña  " + "\n")
    passwordValidator(password, "contraseña de " + role + "\n")
    adminService.createUser(hospital, name, id, genre, mail, telephone, birth, address, role, userName, password)
    
def showUsers(hospital, role):
    users = adminService.findUsersByRole(hospital, role)
    if users:
        for user in users:
            print(f"Nombre: {user.name}")
            print(f"Cedula: {user.id}")
            print(f"Genero: {user.genre}")
            print(f"Email: {user.mail}")
            print(f"Telefono: {user.telephone}")
            print(f"Fecha de nacimiento: {user.birth}")
            print(f"Direccion: {user.address}")
            print(f"Rol: {user.role}")
            print(f"Usuario: {user.userName}")
            print("")
    else:
        print("No se encontraron usuarios con ese rol.")




def deleteUser(hospital, id):
    id = int(id)
    if adminService.deleteUser(hospital, id):
        deleteUser2(hospital, id)
    else:
        print("No se encontró ningún usuario con esa identificación.")

def deleteUser2(hospital, id):
    for i, user in enumerate(hospital.persons):
        if user.id == id:
            del hospital.persons[i]
            print("Usuario eliminado exitosamente.")
            return

def updateUser(hospital,id):
    id = adminService.updateUser(hospital,id)
    if id:
        print("Usuario encontrado. Introduzca los nuevos datos:")
        new_name = input("Nuevo nombre: ").strip()
        new_genre = input("Nuevo genero: ").strip()
        new_mail = input("Nuevo correo: ").strip()
        new_telephone = input("Nuevo telefono: ").strip()
        new_birth = input("nueva fecha de nacimiento: ").strip()
        new_address= input("Nueva direccion: ").strip()
        new_role= input("Nuevo rol: ").strip()
        new_userName= input("Nuevo usuario: ").strip()
        new_password= input("Nueva contrasena: ").strip()
        
        if new_name:
            id.name = new_name
        if new_genre:
            id.genre = new_genre
        if new_mail:
            id.mail = new_mail
        if new_telephone:
            id.telephone = new_telephone
        if new_birth:
            id.birth = new_birth
        if new_address:
            id.address = new_address
        if new_role:
            id.role = new_role
        if new_userName:
            id.username = new_userName
        if new_password:
            id.password = new_password
        
        print("Usuario actualizado correctamente.")
    else:
        print("No se encontró ningún usuario con esa cedula.")

=======

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
    
>>>>>>> 4029855b1b4d1e4ff7f30c1b56509f54626a495a
