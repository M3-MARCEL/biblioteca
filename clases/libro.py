class Libro:
    def __init__(self, isbn, titulo, autor, numero_copias, anio):
        self.isbn = isbn  # Atributo privado: ISBN del libro (Encapsulamiento)
        self.titulo = titulo  # Atributo privado: título del libro (Encapsulamiento)
        self.autor = autor  # Atributo privado: autor del libro (Encapsulamiento)
        self.numero_copias = numero_copias  # Atributo privado: número de copias (Encapsulamiento)
        self.anio = anio  # Atributo privado: año de publicación (Encapsulamiento)

    def mostrar_info(self):
        return f"{self.titulo} por {self.autor}, {self.anio}, Copias: {self.numero_copias}"