class Estudiante:
    def __init__(self, nombre, carrera):
        self.nombre = nombre
        self.carrera = carrera
        self.historiales = []

    def registrar_historial(self, historial):
        self.historiales.append(historial)

    def obtener_historial_por_semestre(self, semestre):
        for h in self.historiales:
            if h.periodo == semestre:
                return h
        return None

    def obtener_cantidad_de_historiales(self):
        return len(self.historiales)