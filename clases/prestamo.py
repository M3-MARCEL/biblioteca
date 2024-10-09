class Prestamo:
    def __init__(self, isbn, numero_usuario, fecha_prestamo, fecha_entrega):
        self.isbn = isbn  # Atributo privado: ISBN del libro prestado (Encapsulamiento)
        self.numero_usuario = numero_usuario  # Atributo privado: número de usuario (Encapsulamiento)
        self.fecha_prestamo = fecha_prestamo  # Atributo privado: fecha de préstamo (Encapsulamiento)
        self.fecha_entrega = fecha_entrega  # Atributo privado: fecha de entrega (Encapsulamiento)
        self.entregado = False  # Atributo privado: estado de entrega (Encapsulamiento)

    def marcar_entregado(self):
        self.entregado = True  # Método para marcar el préstamo como entregado