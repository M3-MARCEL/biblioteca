from usuario import Usuario

class UsuarioEstudiante(Usuario):  # Herencia: UsuarioEstudiante hereda de Usuario
    def __init__(self, nombre, numero_usuario, correo, telefono, curso):
        super().__init__(nombre, numero_usuario, correo, telefono)  # Inicializa atributos de la clase base
        self.curso = curso  # Atributo privado: curso del estudiante (Encapsulamiento)

    def tipo_usuario(self):
        return "Estudiante"  # Polimorfismo: redefinición del método tipo_usuario