from funciones import crear_contra_aleatoria

class Cuenta:
    def __init__(self, nombre_usuario, url, sitio_web, contrasena):
        self._nombre_usuario = nombre_usuario
        self._url = url
        self._sitio_web = sitio_web
        self._contrasena = contrasena

    # Setter para el nombre de usuario
    def set_nombre_usuario(self, nuevo_nombre):
        self._nombre_usuario = nuevo_nombre

    # Getter para el nombre de usuario
    def get_nombre_usuario(self):
        return self._nombre_usuario

    # Setter para la URL
    def set_url(self, nueva_url):
        self._url = nueva_url

    # Getter para la URL
    def get_url(self):
        return self._url

    # Setter para el sitio web
    def set_sitio_web(self, nuevo_sitio):
        self._sitio_web = nuevo_sitio

    # Getter para el sitio web
    def get_sitio_web(self):
        return self._sitio_web

    # Setter para la contraseña
    def set_contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena

    # Getter para la contraseña
    def get_contrasena(self):
        return self._contrasena

    def __str__(self):
        return f"Nombre de usuario: {self._nombre_usuario}\nURL: {self._url}\nSitio web: {self._sitio_web}\nContraseña: {self._contrasena}"


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
def main():
    print("Elige una de las opciones para gestioanr tus contraseñas:\n"
          + "   1. Generar contraseña\n"
          + "   2. Recuperar contraseñas")
    elecion = int(input())
    
    if elecion == 1:
        generar_contra()
    elif elecion == 2:
        print("sin desarrollar")

main()