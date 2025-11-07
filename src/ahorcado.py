"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Aarón Gallardo Canto
Fecha: 6/11/2025
"""

import random 
import requests
import json

def limpiar_pantalla(): # COMPLETA
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra(): # COMPLETA
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    :returns: La palabra a adivinar en mayúsculas
    :rtype: str
    """

    # ESTA FUNCIÓN LA HE HECHO CON AYUDA DE IA

    palabra_valida = None
    min_letras = 5

    while palabra_valida is None:
        url = "https://random-word-api.herokuapp.com/word?lang=es&number=15"
        
        response = requests.get(url)
        palabras = response.json()

        palabras_filtradas = [
            palabra for palabra in palabras 
            if len(palabra) >= min_letras
        ]

        if palabras_filtradas:
            palabra_valida = random.choice(palabras_filtradas)
    
    lista_palabra_adivinar = list(palabra_valida)
    
    for indice,letra in enumerate(palabra_valida.upper()):
        if letra == "Á":
            lista_palabra_adivinar[indice] = "A"
        elif letra == "É":
            lista_palabra_adivinar[indice] = "E"
        elif letra == "Í":
            lista_palabra_adivinar[indice] = "I"
        elif letra == "Ó":
            lista_palabra_adivinar[indice] = "O"
        elif letra == "Ú":
            lista_palabra_adivinar[indice] = "U"

    return "".join(lista_palabra_adivinar).upper()

def solicitar_letra(letras_usadas): # COMPLETA
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    :param letras_usadas: Lista de letras ya introducidas
    :type letras_usadas: list
    :returns: La letra introducida en mayúsculas
    :rtype: str
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida X
    # - Verificar que sea solo un carácter (len() == 1) X
    # - Verificar que sea una letra (isalpha()) X
    # - Verificar que no esté en letras_usadas (operador 'in') X
    # - Convertir a mayúsculas (upper()) X

    bucle = None
    while bucle == None:
        letra = str(input("\nIntroduce una letra >> "))
        if not letra.isalpha() or len(letra) != 1:
            print("\nPor favor, introduce una letra")
        else:
            if not letra in letras_usadas:
                letras_usadas.append(letra)
                return letra.upper()
            else:
                print("\nYa has probado con esa letra. Por favor, introduce otra letra")

def mostrar_estado(palabra_oculta, intentos, letras_usadas): # COMPLETA
    """
    Muestra el estado actual del juego
    
    :param palabra_oculta: La palabra con _ y letras adivinadas
    :type palabra_oculta: str
    :param intentos: Número de intentos restantes
    :type intentos: int
    :param letras_usadas: Lista de letras ya usadas
    :type letras_usadas: list
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes X
    # - Imprimir la palabra con espacios entre caracteres X
    # - Imprimir las letras usadas X

    # INTENTOS RESTANTES
    print(f"\nIntentos restantes >> {intentos}")

    # PALABRA CON ESPACIOS ENTRE CARACTERES
    print("\nPalabra:")
    for i in palabra_oculta:
        print(i, end =" ")

    # LETRAS USADAS HASTA EL MOMENTO
    if not letras_usadas:
        print("\n\nDe momento no has usado ninguna letra")
    else:
        print("\n\nLetras usadas:\n")
        for i in letras_usadas:
            if i == letras_usadas[-1]:
                print(i)
            else:
                print(i, end =" ")

def actualizar_palabra_oculta(palabra, palabra_oculta, letra): # COMPLETA
    """Actualiza la palabra oculta revelando las apariciones de la letra

    :param palabra: La palabra completa a adivinar
    :type palabra: str
    :param palabra_oculta: La palabra actual con _ y letras adivinadas
    :type palabra_oculta: str
    :param letra: La letra que se ha adivinado
    :type letra: str
    :returns: La palabra oculta actualizada
    :rtype: str
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string
    
    lista_palabra_oculta = []
    for i in palabra_oculta:
        lista_palabra_oculta.append(i)

    for indice, letra_for in enumerate(palabra):
        if letra_for == letra:
            lista_palabra_oculta.pop(indice)
            lista_palabra_oculta.insert(indice, letra)
    
    palabra_oculta_nueva = ""
    for i in lista_palabra_oculta:
        palabra_oculta_nueva += i
    
    return palabra_oculta_nueva


def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    limpiar_pantalla()
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    INTENTOS_MAXIMOS = 5
    
    # TODO: Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()
    
    # TODO: Inicializar variables del juego
    palabra_oculta = ""
    for i in palabra:
        palabra_oculta += "_"
    
    intentos = INTENTOS_MAXIMOS
    letras_usadas = []
    juego_terminado = False
    
    
    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo
    
    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta
    
    while not juego_terminado and intentos > 0:
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        letra = solicitar_letra(letras_usadas)
        if letra in palabra:
            palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            print("\n¡Has acertado!")
            if not "_" in palabra_oculta:
                juego_terminado = True
        else:
            intentos -= 1
            print("\n¡Has fallado!")
        limpiar_pantalla()
    
    if intentos > 0:
        print(f"\n¡Has ganado! La palabra era >> {palabra}")
    else:
        print(f"\n¡Has perdido! La palabra era >> {palabra}")


def main():
    """
    Punto de entrada del programa
    """
    jugar()
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()

    jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    if jugar_otra_vez.lower() == 's':
        main()
    else:
        print("Saliendo...")

if __name__ == "__main__":
    main()
