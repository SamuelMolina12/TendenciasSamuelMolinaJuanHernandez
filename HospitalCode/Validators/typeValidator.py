import re
from datetime import datetime, timedelta

def textValidator(string, element):
    if string is None or string.strip() == "":
        raise ValueError(element + " no es un valor válido.")


# def textValidatorU(string,element):
#     if string==None:
#         raise Exception(element + "no es un valor valido")

def numberValidator(string,element):
    
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


def usernameValidator(userName, element):
    
    if not re.match(r"^[a-zA-Z0-9]{1,15}$", userName):
        print("Error: El campo " + element + " debe contener solo letras y números y tener entre 1 y 15 caracteres.")
        return False
    return userName


def emailValidator(mail, element):
   
    
    if not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail):
        print("Error: El campo " + element + " no es un correo electrónico válido.")
        
        return False
    
    return mail


def validateYesNo(input_str):
    while True:
        userInput = input(input_str).lower()
        if userInput == 'si' or userInput == 'no':
            return userInput
        else:
            print("Por favor, responda con 'si' o 'no'.")


def phoneValidator(thelephone, element):
    if thelephone.strip() == "":
        print("El campo " + element + " está vacío.")
        return False
    
    if not (1 <= len(thelephone) <= 10 and thelephone.isdigit()):
        print("Error: El campo " + element + " debe contener entre 1 y 10 dígitos.")
        return False
    return thelephone


def genreValidator(genre,element):
    
    
    genreValid = ["masculino", "femenino"]
    if genre.lower() not in genreValid:
        raise ValueError("Género inválido. Por favor, ingrese 'masculino', 'femenino'")
    return True

# def genreValidatorU(genre):
#     genreValid = ["masculino", "femenino"]
#     if genre.lower() not in genreValid:
#         raise ValueError("Género inválido. Por favor, ingrese 'masculino', 'femenino'")
#     return True



def addressValidator(address, element):
    if len(address) > 30:
        print("Error: El campo " + element + " no puede tener más de 30 caracteres.")
        return False
    return address


def dateValidator(birth, element):
    if birth is None or birth.strip() == "":
        print(" El campo " + element + " está vacío.")
        return False
    try:
        date = datetime.strptime(birth, '%d/%m/%Y')
        if date > datetime.now() or date < datetime.now() - timedelta(days=365*150):
            raise ValueError
    except ValueError:
        print("Error: El campo " + element + " no está en el formato DD/MM/YYYY o no es una fecha válida.")
        return False
    return birth
