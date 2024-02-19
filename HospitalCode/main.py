from Models import models

hospital=models.hospital()



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
