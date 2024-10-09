class Usuario:
    def __init__(self, nombre, numero_usuario, correo, telefono):
        self.nombre = nombre  # Atributo privado: nombre del usuario (Encapsulamiento)
        self.numero_usuario = numero_usuario  # Atributo privado: número de usuario (Encapsulamiento)
        self.correo = correo  # Atributo privado: correo del usuario (Encapsulamiento)
        self.telefono = telefono  # Atributo privado: teléfono del usuario (Encapsulamiento)
        self.habilitado = True  # Atributo privado: estado de habilitación del usuario (Encapsulamiento)

    def habilitar(self):
        self.habilitado = True  # Método para habilitar al usuario

    def deshabilitar(self):
        self.habilitado = False  # Método para deshabilitar al usuario

    def tipo_usuario(self):
        return "Usuario base"  # Método que devuelve el tipo de usuario (Polimorfismo)