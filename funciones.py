import random
import string

def crear_contra_aleatoria():
    caracteres_especiales = string.punctuation
    letras_mayusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    digitos = string.digits
    
    # Seleccionar al menos un carácter de cada categoría
    contraseña = (random.choice(caracteres_especiales) +
                  random.choice(letras_mayusculas) +
                  random.choice(letras_minusculas) +
                  random.choice(digitos))
    
    # Determinar posiciones aleatorias para los caracteres especiales
    num_caracteres_especiales = random.randint(1, 2)
    posiciones_especiales = random.sample(range(len(contraseña)), num_caracteres_especiales)
    
    # Insertar los caracteres especiales en las posiciones aleatorias
    for pos in posiciones_especiales:
        contraseña = contraseña[:pos] + random.choice(caracteres_especiales) + contraseña[pos:]
    
    # Rellenar el resto de la contraseña con caracteres aleatorios
    longitud_restante = 8 - len(contraseña)
    caracteres_totales = letras_mayusculas + letras_minusculas + digitos + caracteres_especiales
    contraseña += ''.join(random.choice(caracteres_totales) for _ in range(longitud_restante))
    
    # Mezclar los caracteres para obtener una contraseña aleatoria
    contraseña = ''.join(random.sample(contraseña, len(contraseña)))
    
    return contraseña
