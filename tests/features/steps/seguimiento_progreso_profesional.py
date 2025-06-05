from behave import *
from src.Carrera import Carrera
from src.ObjetivoProfesionalizante import ObjetivoProfesionalizante
from src.Estudiante import Estudiante
from src.Historial import Historial

use_step_matcher("re")


@given("que el estudiante tiene al menos un historial")
def step_impl(context):
    objetivos = list(ObjetivoProfesionalizante)
    carrera = Carrera("Software", objetivos, 70)

    estudiante = Estudiante("Diana", carrera)
    historial = Historial("2024-A", {
        ObjetivoProfesionalizante.APLICAR: 83,
        ObjetivoProfesionalizante.EMPLEAR: 87,
        ObjetivoProfesionalizante.EVALUAR: 93
    })
    # se añade un segundo para el cálculo de la media
    estudiante2 = Estudiante("Sebastián", carrera)
    estudiante2.registrar_historial(Historial("2024-A", {
        ObjetivoProfesionalizante.APLICAR: 73,
        ObjetivoProfesionalizante.EMPLEAR: 75,
        ObjetivoProfesionalizante.EVALUAR: 77
    }))
    estudiante.registrar_historial(historial)

    context.carrera = carrera
    context.estudiante = estudiante

    # Para simular la media
    context.estudiantes = [estudiante, estudiante2]

    assert estudiante.obtener_cantidad_de_historiales() >= 1


@step('consulta la (?P<nota_de_progreso>.+) para el objetivo "(?P<objetivo>.+)" en el historial del semestre (?P<semestre>.+)')
def step_impl(context, nota_de_progreso, objetivo, semestre):

    historial = context.estudiante.obtener_historial_por_semestre(semestre)
    assert historial is not None # debe encontrarse el historial para el semestre

    objetivo_enum = context.carrera.obtener_objetivo(objetivo)
    assert objetivo_enum is not None # validar que el objetivo pertenece a la carrera

    progreso_obtenido = historial.obtener_progreso(objetivo_enum)

    assert float(nota_de_progreso) == progreso_obtenido

    context.objetivo = objetivo_enum
    context.semestre = semestre
    context.progreso_obtenido = progreso_obtenido
    context.historial = historial

@step("se indicará que cumple con el objetivo")
def step_impl(context):
    historial = context.historial
    objetivo = context.objetivo
    umbral_de_aprobacion = context.carrera.umbral_de_aprobacion

    assert historial.validar_aprobacion_de_objetivo(objetivo, umbral_de_aprobacion)


@step("se mostrará la (?P<media_de_progreso>.+) de los estudiantes")
def step_impl(context, media_de_progreso):
    media_de_progreso_esperado = float(media_de_progreso)
    objetivo = context.objetivo
    semestre = context.semestre
    estudiantes = context.estudiantes

    carrera = context.carrera
    media_calculada = carrera.calcular_media_progreso(estudiantes, objetivo, semestre)

    assert media_calculada == media_de_progreso_esperado
