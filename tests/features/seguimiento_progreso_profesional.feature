# Created by Asus at 27/5/2025
  #language: es

Característica: Seguimiento de autoevaluación de progreso profesionalizante
  Como estudiante de la EPN
  quiero conocer mi progreso a lo largo de cada semestre en relación a los objetivos de la carrera
  para determinar posibles falencias en mi proceso académico y tomar acciones correctivas

  Esquema del escenario: Seguimiento sin falencias
    Dado que el estudiante tiene al menos un historial
    Cuando consulta el progreso del objetivo "<objetivo>" en el historial para el <semestre>
    Entonces se mostrará el <porcentaje_de_progreso> en verde por cada objetivo
    Y se mostrará la <media_de_progreso> de estudiantes

    Ejemplos:
      | objetivo                                                                                                                                                                                                      | cantidad_de_historiales | porcentaje_de_progreso | media_de_progreso | semestre |
      | Aplicar teorías, metodologías, estándares y tecnologías apropiadas, para crear soluciones de software, mediante el análisis, diseño, desarrollo, implementación, verificación, documentación, y gestión.      | 1                       | 83                     | 78                | 2025-A   |
      | Emplear principios y herramientas de investigación, para generar nuevas formas de aplicación de la Ingeniería de Software en los sectores industriales y académicos estratégicos del país.                    | 4                       | 87                     | 81                | 2024-A   |
      | Evaluar aspectos interdisciplinares de infraestructuras tecnológicas existentes: tecnologías emergentes, legales, éticos, económicos, ambientales y sociales, para diseñar soluciones de Software de Calidad. | 7                       | 93                     | 80                | 2024-A   |




