from Models import models
from Service import LoginService
from Menus import AdminMenu
from Validators import TypeValidator


hospital=models.Hospital()

admin=models.Employer("samuel",1,"masculino","samuelgmail.com","30004399", "22/09/2002","calle 64A", "admin","sam","12")
hospital.persons.append(admin)
doctor=models.Employer("juan",2,"masculino","juangmail.com","20004399", "24/89/2004","calle 64A", "doctor","ju","13")
hospital.persons.append(doctor)
nurse=models.Employer("soto",3,"masculino","juanmigmail.com","33004399", "24/30/2005","carrera 64A", "enfermera","sot","14")
hospital.persons.append(nurse)
suport=models.Employer("julia",4,"femenino","juliagmail.com","10002343", "21/89/2006","calle 53A", "soporte","soporte","15")
hospital.persons.append(suport)
initialMenu="1. iniciar sesion\n0. cerrar programa\n"








def loginRouter(hospital,user):
    if user.role=="admin":
        AdminMenu.adminMenu(hospital,user)
    elif user.role=="doctor":
          print("enfermera")
        # doctorMenu(hospital,user)
    elif user.role=="nurse":
        print("enfermera")
        # nurseMenu(hospital,user)
    else:
        print("el usuario no tiene un rol valido")



while True:
    option=input(initialMenu)
    if option=="1":
        print("ingrese su usuario:")
        userName=input()
        password=input("ingrese la contraseña:\n")
        user=LoginService.searchUser(hospital,userName)
        if user==None:
            print("usuario no encontrado")
            continue
        if user.password!=password:
            print("error de usuario o contraseña")
            continue
        loginRouter(hospital,user)
    if option == "0":
        
        break


