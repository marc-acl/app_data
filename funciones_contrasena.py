def usuario(user):

    if not user.isalnum():

        return "El usuario solo puede contener letras y números"
    
    elif len(user) < 5:

        return "El usuario debe tener más de 5 caracteres y menos de 15"
    
    elif len(user) > 15:

        return "El usuario debe tener más de 5 caracteres y menos de 15"
    
    else:
        return "True"
    


def contrasena(password):

    if len(password) < 10:

        return "La contraseña debe tener más de 10 caracteres"
    
    elif password.isalnum():

        return "La contraseña debe contener un carácter que no sea ni letra ni número"
    
    else:
        return minMayEsp(password)
    



def minMayEsp(password):

    min = False
    may = False

    for i in password:

        if i.islower():
            min = True

        elif i.isupper():
            may = True
            
        elif i == " ":
            return "La contraseña no puede contener espacios en blanco"
        
    if min and may:
        return True
    
    else:
        return "La contraseña no es segura"

    


    
    

