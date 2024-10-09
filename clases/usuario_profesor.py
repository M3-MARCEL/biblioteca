from usuario import Usuario

class UsuarioProfesor(Usuario):  # Herencia: UsuarioProfesor hereda de Usuario
    def __init__(self, nombre, numero_usuario, correo, telefono, departamento):
        super().__init__(nombre, numero_usuario, correo, telefono)  # Inicializa atributos de la clase base
        self.departamento = departamento  # Atributo privado: departamento del profesor (Encapsulamiento)

    def tipo_usuario(self):
        return "Profesor"  # Polimorfismo: redefinición del método tipo_usuario