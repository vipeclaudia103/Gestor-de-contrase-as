from funciones import crear_contra_aleatoria

historico = []

class Cuenta:
    def __init__(self, nombre_usuario, url, sitio_web, contrasena):
        self.nombre_usuario = nombre_usuario
        self.url = url
        self.sitio_web = sitio_web
        self.contrasena = contrasena

    # Setter para el nombre de usuario
    def setnombre_usuario(self, nuevo_nombre):
        self.nombre_usuario = nuevo_nombre

    # Getter para el nombre de usuario
    def getnombre_usuario(self):
        return self.nombre_usuario

    # Setter para la URL
    def seturl(self, nuevaurl):
        self.url = nuevaurl

    # Getter para la URL
    def geturl(self):
        return self.url

    # Setter para el sitio web
    def setsitio_web(self, nuevo_sitio):
        self.sitio_web = nuevo_sitio

    # Getter para el sitio web
    def getsitio_web(self):
        return self.sitio_web

    # Setter para la contraseña
    def setcontrasena(self, nuevacontrasena):
        self.contrasena = nuevacontrasena

    # Getter para la contraseña
    def getcontrasena(self):
        return self.contrasena

    def __str__(self):
        return f"Nombre de usuario: {self.nombre_usuario}\nURL: {self.url}\nSitio web: {self.sitio_web}\nContraseña: {self.contrasena}"

def imprimir_lista_cuentas(lista_cuentas):
    for cuenta in lista_cuentas:
        print(cuenta)
        print(' + '*40)  # División visual entre cada objeto

def generar_contra():
    print("Nombre del sitio web:")
    sito_web = str(input())
    print("Nombre de usuario")
    n_usu = str(input())
    print("Contraseña:")
    contra = crear_contra_aleatoria()
    print("Tu contraseña es: " + contra)
    print("Url:")
    url = str(input())
    obj = Cuenta(n_usu, url, sito_web, contra)
    historico.append(obj)

def buscar_contra():
    print("De qué sitio web quieres obtener las contraseñas: ")
    sitio = str(input())
    resultados = []
    for i in historico:
        if i.sitio_web == sitio:
            resultados.append(i)
    if len(resultados) == 0:
        print("No hay contraseñas de ese sito web")
    else:
        imprimir_lista_cuentas(resultados)



def main():
    print("Elige una de las opciones para gestionar tus contraseñas:\n"
          + "   1. Generar contraseña\n"
          + "   2. Recuperar contraseñas\n"
          + "   3. Buscar contraseñas\nRespuesta: ")
    try:
        elecion = int(input())
        print('-'*40) 
    except ValueError:
        print("Error: Debes ingresar un número válido.")
    if elecion == 1:
        generar_contra()
    elif elecion == 2:
        if len(historico) > 0:
            imprimir_lista_cuentas(historico)
        else:
            print("Aun no hay registros")
    elif elecion == 3:
        buscar_contra()




while True:
    main()