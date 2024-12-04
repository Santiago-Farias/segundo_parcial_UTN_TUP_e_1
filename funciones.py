import pygame
from colores import *

def draw_ranking_screen(jugadores_ranking: list, pantalla: pygame.surface, boton_rect_salir: pygame.rect, fuente: pygame.font) -> None:
    """
    Qué hace?
        - Dibuja el ranking en la pantalla.
    Qué recibe?
        - La lista de los jugadores (aunque no haya nada), el tamaño de la pantalla, el boton para volver al menú principal y la fuente de texto.
    Qué retorna?
        Nada.
    """
    pantalla.fill(SILVER)
    dibujar_boton(GREY1, WHITE2, pantalla, boton_rect_salir, "Volver", fuente)
    index_ranks = fuente.render(" Puesto                      Jugador                               Puntos               Druación (sec)", True, BLACK)
    pantalla.blit(index_ranks, (225, 70))
    for i, (nombre, puntaje, duracion_partida) in enumerate(jugadores_ranking):
        ranks = fuente.render(f"{i + 1}                    -                    {nombre}                    -                    {puntaje}              {duracion_partida}", True, BLACK)
        pantalla.blit(ranks, (225, 100 + i * 40))

def guardar_ranking(jugador_nombre: str, jugador_puntos: int, jugadores_ranking: list, duracion_partida: float) -> list:
    '''
    Qué hace?
        - Guarda en una lista de listas el ranking de los jugadores
    Qué recibe?
        - El nombre del jugador, la cantidad de puntos, y la lista en donde guardar el ranking
    Qué retorna?
        - La lista con los datos actualizados del jugador
        '''
    for i in range(0, len(jugadores_ranking)):
        if jugadores_ranking[i][1] == 0 and jugadores_ranking[i][0] == "":
            jugadores_ranking[i][0] = jugador_nombre
            jugadores_ranking[i][1] = jugador_puntos
            jugadores_ranking[i][2] = duracion_partida
            break
    return jugadores_ranking

def ordenar_ranking(ranking_puntos: list) -> list:
    '''
    Qué hace?
        - Ordena una lista de jugadores y sus puntajes de forma descendente
    Qué recibe?
        - Una lista de listas 'ranking_puntos' donde cada sublista contiene el nombre del jugador
    Qué retorna?
        - La misma lista 'ranking_puntos' pero ordenada de mayor a menor puntaje
    '''
    for i in range(len(ranking_puntos)):
        for j in range(0, len(ranking_puntos) -i -1):
            if ranking_puntos[j][1] < ranking_puntos[j+1][1]:
                ranking_puntos[j], ranking_puntos[j+1] = ranking_puntos[j+1], ranking_puntos[j]
    return ranking_puntos


def dibujar_boton(color_frame: tuple, color_text: tuple, screen: pygame.surface.Surface, btn: pygame.Rect, text: str, fuente: pygame.font) -> None:
    '''
    Qué hace?
        - Crea un botón.
    Qué recibe?
        - El color de fondo, color de texto, la pantalla principal, el boton, el texto y la fuente del texto..
    Qué retorna?
        - Nada.
    '''
    pygame.draw.rect(screen, color_frame, btn)
    text_surface = fuente.render(text, True, color_text)
    text_rect = text_surface.get_rect(center=btn.center)
    screen.blit(text_surface, text_rect)

def draw_time_left(pantalla: pygame.surface, fuente: pygame.font, tiempo_restante: float) -> None:
    '''
    Qué hace?
        - Dibuja el tiempo restanto contando desde lo indicado por el parámetro tiempo_restane.
    Qué recibe?
        - El tamaño de la pantalla, la fuente del texto, y el tiempo restante.
    Qué retorna?
        - Nada.
    '''
    texto_tiempo = fuente.render(f"Tiempo restante: {int(tiempo_restante)} segundos", True, BLACK)
    pantalla.blit(texto_tiempo, (20, 20))

def draw_points_submit(pantalla: pygame.surface, fuente: pygame.font, jugador_nombre: str|None) -> None:
    '''
    Qué hace?
        - Dibuja un recuedro en donde el usuario debe ingresar un texto. El usuario podrá ver lo que ingresa.
    Qué recibe?
        - El tamaño de la pantalla, la fuente del texto, y el texto ingresado.
    Qué retorna?
        - Nada.
    '''
    pantalla.fill(SILVER)  # Limpia la pantalla con un fondo blanco
    submit_space = pygame.Rect(150, 500, 500, 50)
    indicacion_enter = pygame.Rect(250, 600, 300, 50)
    pygame.draw.rect(pantalla, GREY1, submit_space)
    pygame.draw.rect(pantalla, BLACK, submit_space, 3)

    # Dibujar el texto ingresado
    pygame.draw.rect(pantalla, GRAY38, submit_space)
    text_surface = fuente.render(jugador_nombre, True, BLACK)
    text_rect = text_surface.get_rect(center=submit_space.center)
    pantalla.blit(text_surface, text_rect)

    # Dibujar botón de confirmar
    pygame.draw.rect(pantalla, GRAY46, indicacion_enter)
    text_surface_ie = fuente.render("Presione enter para continuar...", True, BLACK)
    text_rect_ie = text_surface_ie.get_rect(center=indicacion_enter.center)
    pantalla.blit(text_surface_ie, text_rect_ie)


def draw_pregunta_screen(preguntas_respuestas: list, indice_pregunta: int, pantalla: pygame.surface, boton_rect_salir: pygame.rect, fuente: pygame.font) -> list:
    '''
    Qué hace?
        - Dada una lista de preguntas con 4 posibles respuesta cada una, ésta función muestra tanto la pregunta como sus posibles respuestas. 
    Qué recibe?
        - La lista de preguntas y respuestas, índice para iterar de preguntas, el tamaño de la pantalla, el botón de salir y la fuente del texto.
    Qué retorna?
        - Devuelve los Rect con las opciones.
    '''
    pantalla.fill(SILVER)
    dibujar_boton(GREY1, WHITE2, pantalla, boton_rect_salir, "Volver", fuente)

    recuadro_p = pygame.Rect(125, 100, 550, 50)
    recuadros_opciones = [
        pygame.Rect(150, 200, 500, 50),
        pygame.Rect(150, 300, 500, 50),
        pygame.Rect(150, 400, 500, 50),
        pygame.Rect(150, 500, 500, 50),
    ]

    # Dibujar la pregunta
    pygame.draw.rect(pantalla, GREY1, recuadro_p)
    pygame.draw.rect(pantalla, BLACK, recuadro_p, 3)
    texto = fuente.render(preguntas_respuestas[indice_pregunta]['pregunta'], True, WHITE2)
    texto_rect = texto.get_rect(center=recuadro_p.center)
    pantalla.blit(texto, texto_rect)

    # Dibujar opciones
    for i, recuadro in enumerate(recuadros_opciones):
        pygame.draw.rect(pantalla, GREY1, recuadro)
        pygame.draw.rect(pantalla, BLACK, recuadro, 3)
        texto_opcion = preguntas_respuestas[indice_pregunta]['respuestas'][i]['texto']
        opcion = preguntas_respuestas[indice_pregunta]['respuestas'][i]['opcion']
        texto = fuente.render(f"{opcion} - {texto_opcion}", True, WHITE2)
        texto_rect = texto.get_rect(center=recuadro.center)
        pantalla.blit(texto, texto_rect)

    return recuadros_opciones

def draw_main_menu(pantalla: pygame.surface, boton_jugar: pygame.rect, boton_ranking: pygame.rect, boton_rect_salir: pygame.rect, fuente: pygame.font) -> None:
    '''
    Qué hace?
        - Dibuja el menú principal. 
    Qué recibe?
        - El tamaño de la pantalla, los botones y la fuente de texto.
    Qué retorna?
        - Nada.
    '''
    pantalla.fill(GREY2)

    dibujar_boton(GREY1, WHITE2, pantalla, boton_jugar, "Jugar", fuente)
    dibujar_boton(GREY1, WHITE2, pantalla, boton_ranking, "Ranking", fuente)
    dibujar_boton(GREY1, WHITE2, pantalla, boton_rect_salir, "Salir", fuente)