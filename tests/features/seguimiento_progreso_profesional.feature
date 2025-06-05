# Created by Asus at 27/5/2025
  #language: es

Característica: Seguimiento de autoevaluación de progreso profesionalizante
  Como estudiante de la EPN
  quiero conocer mi progreso a lo largo de cada semestre en relación a los objetivos de la carrera
  para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  Esquema del escenario: Seguimiento sin falencias
    Dado que el estudiante tiene al menos un historial
    Cuando consulta la <nota_de_progreso> para el objetivo "<objetivo>" en el historial del semestre <semestre>
    Entonces se indicará que cumple con el objetivo
    Y se mostrará la <media_de_progreso> de los estudiantes

    Ejemplos:
      | objetivo  | nota_de_progreso | media_de_progreso | semestre |
      | APLICAR   | 83                     | 78                | 2024-A   |
      | EMPLEAR   | 87                     | 81                | 2024-A   |
      | EVALUAR   | 93                     | 85                | 2024-A   |

    """
    Esquema del escenario: Seguimiento con falencias
    Dado que el estudiante tiene al menos un historial
    Cuando consulta la <nota_de_progreso> para el objetivo "<objetivo>" en el historial del semestre <semestre>
    Entonces se indicará que no cumple con el objetivo "<objetivo>"
    Y se mostrará la <media_de_progreso> de los estudiantes
    """


