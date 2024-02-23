from Models import models
from Service import LoginService
from Menus import AdminMenu
from Validators import typeValidator


hospital=models.Hospital()

admin=models.Employer("samuel",1,"masculino","samuelgmail.com","30004399", "22/09/2002","calle 64A", "admin","samuelito","mini")
hospital.persons.append(admin)

initialMenu="1. iniciar sesion\n0. cerrar programa\n"




while True:
    option=input(initialMenu)
    if option=="1":
        print("ingrese su usuario:")
        userName=input()
        password=input("ingrese la contraseña:\n")
        user=loginService.searchUser(hospital,userName)
        if user==None:
            print("usuario no encontrado")
            continue
        if user.password!=password:
            print("error de usuario o contraseña")
            continue
        loginRouter(hospital,user)
    if option == "0":
        
        break
