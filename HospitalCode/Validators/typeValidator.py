import re


def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor es valido")

def numberValidator(string,element):
    textValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")


def passwordValidator(password,element):
    if len(password) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")

    if not any(char.isupper() for char in password):
        raise ValueError("La contraseña debe contener al menos una letra mayúscula")
    
    if not any(char.isdigit() for char in password):
        raise ValueError("La contraseña debe contener al menos un número")

    if not re.search(r"[!@#$%^&*()_+{}[\]:;<>,.?/~`]", password):
        raise ValueError("La contraseña debe contener al menos un caracter especial")

    return password
