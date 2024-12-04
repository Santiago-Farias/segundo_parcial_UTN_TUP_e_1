import pygame
import time
from colores import *
import pygame.mixer as mixer
from funciones import *
from datos import *
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WIN_PATH = os.path.join(BASE_DIR, "win.mp3")
LOSE_PATH = os.path.join(BASE_DIR, "lose.mp3")
BOTON_PATH = os.path.join(BASE_DIR, "boton6.wav")

indice_pregunta_actual = 0

jugador_vidas = 3
jugador_puntos = 0

input_active = False  # Controla si la entrada de texto está activa
jugador_nombre = ""  # Almacena el texto ingresado

DIFICULTAD_FACIL = 1
DIFICULTAD_MEDIA = 3
DIFICULTAD_DIFICIL = 5

preguntas_respuestas = [
  {
    "pregunta": "¿Quién es el máximo goleador histórico de la selección argentina?",
    "respuestas": [
      { "opcion": "A", "texto": "Gabriel Batistuta" },
      { "opcion": "B", "texto": "Lionel Messi" },
      { "opcion": "C", "texto": "Sergio Agüero" },
      { "opcion": "D", "texto": "Diego Maradona" }
    ],
    "respuesta_correcta": "B",
    "dificultad": "F"
  },
  {
    "pregunta": "¿En qué año Argentina ganó su primer Mundial de Fútbol?",
    "respuestas": [
      { "opcion": "A", "texto": "1962" },
      { "opcion": "B", "texto": "1978" },
      { "opcion": "C", "texto": "1986" },
      { "opcion": "D", "texto": "1930" }
    ],
    "respuesta_correcta": "B",
    "dificultad": "M"
  },
  {
    "pregunta": "¿Qué club argentino ha ganado más títulos de la Copa Libertadores?",
    "respuestas": [
      { "opcion": "A", "texto": "Boca Juniors" },
      { "opcion": "B", "texto": "River Plate" },
      { "opcion": "C", "texto": "Independiente" },
      { "opcion": "D", "texto": "Racing Club" }
    ],
    "respuesta_correcta": "C",
    "dificultad": "F"
  },
  {
    "pregunta": "¿Quién fue el técnico de la selección argentina durante la Copa del Mundo de 1986?",
    "respuestas": [
      { "opcion": "A", "texto": "Carlos Bilardo" },
      { "opcion": "B", "texto": "César Luis Menotti" },
      { "opcion": "C", "texto": "Alfio Basile" },
      { "opcion": "D", "texto": "Daniel Passarella" }
    ],
    "respuesta_correcta": "A",
    "dificultad": "D"
  },
  {
    "pregunta": "¿Qué jugador argentino jugó en el Barcelona y el Real Madrid?",
    "respuestas": [
      { "opcion": "A", "texto": "Javier Saviola" },
      { "opcion": "B", "texto": "Gonzalo Higuaín" },
      { "opcion": "C", "texto": "Ángel Di María" },
      { "opcion": "D", "texto": "Claudio Caniggia" }
    ],
    "respuesta_correcta": "A",
    "dificultad": "M"
  },
  {
    "pregunta": "¿En qué año Diego Maradona anotó el famoso 'Gol del Siglo' contra Inglaterra?",
    "respuestas": [
      { "opcion": "A", "texto": "1986" },
      { "opcion": "B", "texto": "1982" },
      { "opcion": "C", "texto": "1990" },
      { "opcion": "D", "texto": "1994" }
    ],
    "respuesta_correcta": "A",
    "dificultad": "M"
  },
  {
    "pregunta": "¿Quién es el entrenador de la selección argentina en el Mundial de 2022?",
    "respuestas": [
      { "opcion": "A", "texto": "Jorge Sampaoli" },
      { "opcion": "B", "texto": "Alejandro Sabella" },
      { "opcion": "C", "texto": "Lionel Scaloni" },
      { "opcion": "D", "texto": "Ricardo Gareca" }
    ],
    "respuesta_correcta": "C",
    "dificultad": "D"
  },
  {
    "pregunta": "¿Qué equipo argentino fue el primero en ganar la Copa Intercontinental?",
    "respuestas": [
      { "opcion": "A", "texto": "Independiente" },
      { "opcion": "B", "texto": "Boca Juniors" },
      { "opcion": "C", "texto": "River Plate" },
      { "opcion": "D", "texto": "Racing Club" }
    ],
    "respuesta_correcta": "D",
    "dificultad": "F"
  },
  {
    "pregunta": "¿En qué estadio se jugó la final del Mundial de 1978, donde Argentina se consagró campeón?",
    "respuestas": [
      { "opcion": "A", "texto": "Estadio Monumental" },
      { "opcion": "B", "texto": "Estadio de La Bombonera" },
      { "opcion": "C", "texto": "Estadio José María Minella" },
      { "opcion": "D", "texto": "Estadio Antonio Vespucio Liberti" }
    ],
    "respuesta_correcta": "A",
    "dificultad": "D"
  },
  {
    "pregunta": "¿Qué jugador argentino es conocido como 'El Pibe de Oro'?",
    "respuestas": [
      { "opcion": "A", "texto": "Carlos Tevez" },
      { "opcion": "B", "texto": "Sergio Agüero" },
      { "opcion": "C", "texto": "Diego Maradona" },
      { "opcion": "D", "texto": "Juan Román Riquelme" }
    ],
    "respuesta_correcta": "C",
    "dificultad": "D"
  }
]

jugadores_ranking = [
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0],
    ["", 0, 0]
]

ranking_ordenado = None

pygame.init()

# Definir la pantalla.
pantalla = pygame.display.set_mode((800, 800))
pygame.display.set_caption("pygame.group.load('Santi, Mati, Lauty')")

# Definir botones y la fuente del texto.
boton_rect_salir = pygame.Rect(325, 600, 150, 50)
boton_ranking = pygame.Rect(325, 500, 150, 50)
boton_jugar = pygame.Rect(325, 400, 150, 50)
fuente = pygame.font.Font(None, 24)

# Definir sonido de los botones.
sonido_opcion = mixer.Sound(BOTON_PATH) # PROBANDO LO DEL AUDIO, BORRAR Y HACERLO MEJOR.
sonido_opcion.set_volume(0.1)

sonido_win = mixer.Sound(WIN_PATH)
sonido_win.set_volume(0.3)

sonido_lose = mixer.Sound(LOSE_PATH)
sonido_lose.set_volume(0.1)

texto_a_mostrar = "falopa"

current_screen = "menu principal"

while True:
    mouse = pygame.mouse.get_pos()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if current_screen == "menu principal":
                if boton_jugar.collidepoint(evento.pos):
                    sonido_opcion.play()
                    current_screen = "pregunta"
                    tiempo_inicial = time.time()
                    inicio_partida_tiempo = time.time()
                elif boton_ranking.collidepoint(evento.pos):
                    sonido_opcion.play()
                    time.sleep(0.5)
                    current_screen = "ranking"
                elif boton_rect_salir.collidepoint(evento.pos):
                    print("Boton presionado")
                    sonido_opcion.play()
                    time.sleep(0.5)
                    pygame.quit()
                    quit()
            elif current_screen == "pregunta":
                if jugador_vidas > 0:
                    for i, recuadro in enumerate(recuadros_opciones):
                        if recuadro.collidepoint(evento.pos):
                            opcion_seleccionada = preguntas_respuestas[indice_pregunta_actual]['respuestas'][i]['opcion']
                            respuesta_correcta = preguntas_respuestas[indice_pregunta_actual]['respuesta_correcta']
                            if opcion_seleccionada == respuesta_correcta:
                                pygame.draw.rect(pantalla, GREEN, recuadro, 3)
                                if preguntas_respuestas[indice_pregunta_actual]['dificultad'] == "F":
                                    jugador_puntos += DIFICULTAD_FACIL
                                elif preguntas_respuestas[indice_pregunta_actual]['dificultad'] == "M":
                                    jugador_puntos += DIFICULTAD_MEDIA
                                else:
                                    jugador_puntos += DIFICULTAD_DIFICIL
                                print("Correcto")
                                sonido_win.play()
                            else:
                                pygame.draw.rect(pantalla, RED1, recuadro, 3)
                                jugador_vidas -= 1
                                indice_pregunta_actual += 1
                                print("Respuesta incorrecta")
                                sonido_lose.play()
                                print("vidas", jugador_vidas)
                                print("puntos", jugador_puntos)
                            pygame.display.flip()
                            time.sleep(1)    
                            indice_pregunta_actual += 1
                            tiempo_inicial = time.time()
                            if indice_pregunta_actual >= len(preguntas_respuestas):
                                current_screen = "submit_name"
                                indice_pregunta_actual = 0
                                print("¡Has completado el cuestionario!")
                    if boton_rect_salir.collidepoint(evento.pos):
                        current_screen = "menu principal"
                elif jugador_vidas == 0:
                    fin_partida_tiempo = time.time()
                    duracion_partida = round(fin_partida_tiempo - inicio_partida_tiempo, 2)
                    print(duracion_partida)
                    current_screen = "submit_name"
                    indice_pregunta_actual = 0
                    print("Partida terminada, te quedaste sin vidas")
                    break
            elif current_screen == "submit_name":
                if boton_rect_salir.collidepoint(evento.pos):  # Confirmar texto con botón
                    pass
            elif current_screen == "ranking":
                if boton_rect_salir.collidepoint(evento.pos):
                        sonido_opcion.play()
                        time.sleep(0.5)
                        current_screen = "menu principal"
        elif evento.type == pygame.KEYDOWN and current_screen == "submit_name":
            if evento.key == pygame.K_RETURN:  # Confirmar texto con Enter
                sonido_opcion.play()
                time.sleep(0.5)
                print("Texto confirmado:", jugador_nombre)
                fin_partida_tiempo = time.time()
                duracion_partida = round(fin_partida_tiempo - inicio_partida_tiempo, 2)
                ranking = guardar_ranking(jugador_nombre, jugador_puntos, jugadores_ranking, duracion_partida)
                print("test", duracion_partida)
                print(ranking)
                ranking_ordenado = ordenar_ranking(ranking)
                jugador_vidas = 3
                jugador_puntos = 0
                current_screen = "menu principal"
                jugador_nombre = ""  # Limpia el texto después de confirmar
            elif evento.key == pygame.K_BACKSPACE:  # Eliminar último carácter
                jugador_nombre = jugador_nombre[:-1]
            else:  # Agregar el carácter presionado
                jugador_nombre += evento.unicode
        
    
    if current_screen == "menu principal":
        draw_main_menu(pantalla, boton_jugar, boton_ranking, boton_rect_salir, fuente)
    elif current_screen == "pregunta":
        recuadros_opciones = draw_pregunta_screen(preguntas_respuestas, indice_pregunta_actual, pantalla, boton_rect_salir, fuente)
        tiempo_actual = time.time()
        tiempo_restante = max(0, 6 - (tiempo_actual - tiempo_inicial))  # Tiempo máximo es 5 segundos

        # Dibuja las opciones de la pregunta y el tiempo restante
        recuadros_opciones = draw_pregunta_screen(preguntas_respuestas, indice_pregunta_actual, pantalla, boton_rect_salir, fuente)
        draw_time_left(pantalla, fuente, tiempo_restante)

        # Si el tiempo se acaba, pasa automáticamente a la siguiente pregunta
        if tiempo_restante == 0:
            sonido_lose.play()
            jugador_vidas -= 1  # Penalización por no responder
            indice_pregunta_actual += 1

            # Reinicia o vuelve al menú principal si ya no hay preguntas
            if indice_pregunta_actual >= len(preguntas_respuestas) or jugador_vidas == 0:
                current_screen = "menu principal"
                indice_pregunta_actual = 0
                current_screen = "submit_name"
                fin_partida_tiempo = time.time()
                duracion_partida = round(fin_partida_tiempo - inicio_partida_tiempo, 2)
                print(duracion_partida)
                print("Tiempo agotado, volvemos al menú principal")
            else:
                tiempo_inicial = time.time()
    elif current_screen == "submit_name":
        jugador_vidas = 3
        draw_points_submit(pantalla, fuente, jugador_nombre)
    elif current_screen == "ranking":
        if ranking_ordenado != None:
            draw_ranking_screen(ranking_ordenado, pantalla, boton_rect_salir, fuente)
        else:
            draw_ranking_screen(jugadores_ranking, pantalla, boton_rect_salir, fuente)

    # Efecto hover para los botones.
    if current_screen == "menu principal":
        if (mouse[0] >= 325 and mouse[0] <= 475) and (mouse[1] >= 600 and mouse[1] <= 650):
            dibujar_boton(WHITE2, GREY1, pantalla, boton_rect_salir, "Salir", fuente)
        elif (mouse[0] >= 325 and mouse[0] <= 475) and (mouse[1] >= 500 and mouse[1] <= 550):
            dibujar_boton(WHITE2, GREY1, pantalla, boton_ranking, "Ranking", fuente)
        elif (mouse[0] >= 325 and mouse[0] <= 475) and (mouse[1] >= 400 and mouse[1] <= 450):
            dibujar_boton(WHITE2, GREY1, pantalla, boton_jugar, "Jugar", fuente)
    elif current_screen == "menu secundario":
        if boton_rect_salir.collidepoint(mouse):
            dibujar_boton(WHITE2, GREY1, pantalla, boton_rect_salir, "Volver", fuente)
    elif current_screen == "ranking":
        if boton_rect_salir.collidepoint(mouse):
            dibujar_boton(WHITE2, GREY1, pantalla, boton_rect_salir, "Volver", fuente)
    
        pygame.display.flip()

    pygame.display.update()