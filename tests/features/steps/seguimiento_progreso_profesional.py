from behave import *

from src.Estudiante import Estudiante
from src.Historial import Historial

use_step_matcher("re")

def before_scenario(context):
    context.estudiante = Estudiante(None, [])
    context.historial = Historial(None, {}, None, None)
    context.estudiante.registrar_historial(context.historial)

@step("que el estudiante tiene al menos un historial")
def step_impl(context):
    assert context.estudiante.obtener_cantidad_de_historiales() >= 1;

@step('consulta el progreso del objetivo "(?P<objetivo>.+)" en el historial para el (?P<semestre>.+)')
def step_impl(context):
    """
    :type context: behave.runner.Context
    :type objetivo: str
    :type semestre: str
    """




# Alguna consulta a la DB utilizando el objetivo y el semestre


@step("se mostrará el (?P<porcentaje_de_progreso>.+) en verde por cada objetivo")
def step_impl(context, porcentaje_de_progreso):
    """
    :type context: behave.runner.Context
    :type porcentaje_de_progreso: str
    """
    context.porcentaje_de_progreso = porcentaje_de_progreso
    resultado = "verde" if int(porcentaje_de_progreso) >= 70 else "rojo"

    assert resultado == "verde", f"Se esperaba 'verde', pero fue '{resultado}'"


@step("se mostrará la (?P<media_de_progreso>.+) de estudiantes")
def step_impl(context, media_de_progreso):
    """
    :type context: behave.runner.Context
    :type media_de_progreso: str
    """
