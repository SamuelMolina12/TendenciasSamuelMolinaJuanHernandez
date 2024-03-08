from Validators.TypeValidator import *
import Service.AdminService as adminService

def createUser(hospital,role):
    print("Ingreso a la creacion del rol " + role)
    name=input("ingrese el nombre \n")
    textValidator(name,"nombre  \n")
    id=numberValidator(input("ingrese la cedula  \n"), "cedula de " + role )
    userName=input("ingrese el usuario  " + "máximo 15 caracteres, solo debe contener letras y numeros \n")
    textValidator(userName,"usuario de   \n" )
    usernameValidator(userName,"usuario de    \n" )
    genre=input("ingrese el genero: masculino o femenino \n")
    textValidator(genre, "genero de    \n")
    genreValidator(genre, "genero de    \n")
    mail=input("ingrese el correo " + " dominio y el @ \n")
    textValidator(mail, "correo de   \n")
    emailValidator(mail, "correo de    \n")
    telephone=phoneValidator(input("ingrese el numero telefonico " + "Debe contener entre 1 y 10 dígitos\n"), "numero telefono")
    birth=dateValidator(input("ingrese la fecha de nacimiento " + "Formato DD/MM/YYYY, max 150 años\n"),"fecha de nacimiento de")
    address=input("ingrese la direccion " + "Máximo 30 caracteres  \n")
    textValidator(address, "direccion de    \n")
    addressValidator(address, "direccion de  \n")
    role=role
    textValidator(role, "rol de \n")
    password=input("Ingrese la contraseña  " + "8 caracteres, un numero, 1 letra Mayuscula y 1 caracter especial \n")
    passwordValidator(password, "contraseña de \n")
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
        new_name =input("ingrese el nuevo nombre \n")
        textValidator(new_name,"el nuevo nombre \n")
        new_genre = input("¿Desea actualizar el género? Ingrese el nuevo género o presione Enter para mantener el mismo: ")
        new_mail = input("ingrese el nuevo correo " + " dominio y el @ \n")
        emailValidator( new_mail,"correo \n")
        new_telephone = input("Nuevo telefono: " + "Debe contener entre 1 y 10 dígitos") 
        phoneValidator(new_telephone, "nuevo numero de telefo\n")
        new_birth = input("nueva fecha de nacimiento: " + "Formato DD/MM/YYYY")
        dateValidator(new_birth, "nuevo fecha de nacimiento\n")
        new_address= input("ingrese la nueva direccion " + "Máximo 30 caracteres\n")
        textValidator(new_address, "direccion  \n")
        addressValidator(new_address, "direccion \n")
        new_userName= input("ingrese el nuevo usuario  " + "máximo 15 caracteres, solo debe contener letras y numeros\n")
        textValidatorU(new_userName,"usuario \n" )
        usernameValidator(new_userName,"usuario  \n" )
        new_password= input("Ingrese la nueva contraseña  " + "8 caracteres, un numero, 1 letra Mayuscula y 1 caracter especial\n")
        passwordValidator(new_password, "contraseña \n")
        
        if new_name:
            id.name = new_name
        if new_genre:
           genreValidator(new_genre)
           id.genre = new_genre
        if new_mail:
            id.mail = new_mail
        if new_telephone:
            id.telephone = new_telephone
        if new_birth:
            id.birth = new_birth
        if new_address:
            id.address = new_address
        if new_userName:
            id.username = new_userName
        if new_password:
            id.password = new_password
        
        print("Usuario actualizado correctamente.")
    else:
        print("No se encontró ningún usuario con esa cedula.")

