class Biblioteca:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre  # Atributo privado: nombre de la biblioteca (Encapsulamiento)
        self.direccion = direccion  # Atributo privado: dirección de la biblioteca (Encapsulamiento)
        self.telefono = telefono  # Atributo privado: teléfono de la biblioteca (Encapsulamiento)

    def buscar_libro(self, isbn):
        pass  # Método para buscar un libro por ISBN

    def prestar_libro(self, usuario, libro):
        pass  # Método para prestar un libro a un usuario

    def devolver_libro(self, usuario, libro):
        pass  # Método para devolver un libro de un usuario