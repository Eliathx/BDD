class Historial:
    def __init__(self, periodo, progreso_por_objetivo, nota_evaluacion_psicologica=None, nota_autoevaluacion=None):
        self.periodo = periodo
        self.progreso_por_objetivo = progreso_por_objetivo
        self.nota_evaluacion_psicologica = nota_evaluacion_psicologica
        self.nota_autoevaluacion = nota_autoevaluacion

    def obtener_progreso(self, objetivo):
        return self.progreso_por_objetivo.get(objetivo, 0)

    def validar_aprobacion_de_objetivo(self, objetivo, umbral):
        return self.obtener_progreso(objetivo) >= umbral

