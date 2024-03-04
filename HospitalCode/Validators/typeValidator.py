import re

<<<<<<< HEAD

def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor es valido")

def numberValidator(string,element):
    textValidator(string,element)
=======
def TextValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor es valido")

def NumberValidator(string,element):
    TextValidator(string,element)
>>>>>>> 4029855b1b4d1e4ff7f30c1b56509f54626a495a
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")


<<<<<<< HEAD
def passwordValidator(password,element):
=======
def PasswordValidator(password,element):
>>>>>>> 4029855b1b4d1e4ff7f30c1b56509f54626a495a
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")

    if not any(char.isupper() for char in password):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula")
    
    if not any(char.isdigit() for char in password):
        raise ValueError("La contraseña debe contener al menos un número")

    if not re.search(r"[!@#$%^&*()_+{}[\]:;<>,.?/~`]", password):
        raise ValueError("La contraseña debe contener al menos un caracter especial")

    return password
<<<<<<< HEAD
=======

>>>>>>> 4029855b1b4d1e4ff7f30c1b56509f54626a495a
