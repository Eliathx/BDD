class Estudiante:
    def __init__(self, name, historiales):
        self.name = name
        self.historiales = historiales

    def obtener_cantidad_de_historiales(self):
        return len(self.historiales)

    def registrar_historial(self, historial):
        self.historiales.append(historial)

