class Carrera:
    def __init__(self, nombre, objetivos, umbral_de_aprobacion):
        self.nombre = nombre
        self.objetivos = {obj.name: obj for obj in objetivos}
        self.umbral_de_aprobacion = umbral_de_aprobacion

    def calcular_media_progreso(self, estudiantes, objetivo, semestre):
        progresos = [
            h.obtener_progreso(objetivo)
            for est in estudiantes
            for h in est.historiales
            if h.periodo == semestre and objetivo in h.progreso_por_objetivo
        ]
        return sum(progresos) / len(progresos) if progresos else 0.0

    def obtener_objetivo(self, objetivo):
        try:
            return self.objetivos[objetivo]
        except KeyError:
            return None
