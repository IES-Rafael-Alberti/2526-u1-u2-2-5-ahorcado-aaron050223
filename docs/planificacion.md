# Planificación del Juego del Ahorcado

## Análisis del Problema

### Entrada
- Palabra a adivinar (jugador 1)
- Letras para adivinar (jugador 2)

### Salida
- Estado actual de la palabra (con _ y letras adivinadas)
- Intentos restantes
- Letras ya usadas
- Mensajes de retroalimentación
- Mensaje de victoria o derrota

### Proceso
1. Solicitar y validar palabra
2. Inicializar el estado del juego
3. Mientras haya intentos y no se haya ganado:
   - Mostrar estado
   - Solicitar letra
   - Verificar letra
   - Actualizar estado
4. Mostrar resultado final

## Pseudocódigo

```
INICIO
    ESCRIBIR "=== JUEGO DEL AHORCADO ==="
    
    // Solicitar palabra
    REPETIR
        LEER palabra
        SI longitud(palabra) < 5 ENTONCES
            ESCRIBIR "Error: mínimo 5 caracteres"
        FIN SI
        SI NO es_solo_letras(palabra) ENTONCES
            ESCRIBIR "Error: solo letras"
        FIN SI
    HASTA QUE longitud(palabra) >= 5 Y es_solo_letras(palabra)
    
    palabra = a_mayusculas(palabra)
    limpiar_pantalla()
    
    // Inicializar juego
    intentos = 5
    letras_usadas = []
    palabra_oculta = crear_palabra_oculta(palabra)  // "_ _ _ _ _"
    ganado = FALSO
    
    // Bucle principal
    MIENTRAS intentos > 0 Y NO ganado HACER
        mostrar_estado(palabra_oculta, intentos, letras_usadas)
        
        // Solicitar letra
        REPETIR
            LEER letra
            SI longitud(letra) != 1 O NO es_letra(letra) ENTONCES
                ESCRIBIR "Error: introduce una sola letra"
            FIN SI
            SI letra ESTÁ_EN letras_usadas ENTONCES
                ESCRIBIR "Error: letra ya usada"
            FIN SI
        HASTA QUE longitud(letra) == 1 Y es_letra(letra) Y letra NO_ESTÁ_EN letras_usadas
        
        letra = a_mayusculas(letra)
        AÑADIR letra A letras_usadas
        
        // Verificar letra
        SI letra ESTÁ_EN palabra ENTONCES
            ESCRIBIR "¡Bien! La letra está en la palabra"
            actualizar_palabra_oculta(palabra, palabra_oculta, letra)
            
            SI "_" NO_ESTÁ_EN palabra_oculta ENTONCES
                ganado = VERDADERO
            FIN SI
        SINO
            ESCRIBIR "¡Letra incorrecta!"
            intentos = intentos - 1
        FIN SI
    FIN MIENTRAS
    
    // Mensaje final
    SI ganado ENTONCES
        ESCRIBIR "¡FELICIDADES! Has adivinado la palabra:", palabra
    SINO
        ESCRIBIR "¡GAME OVER! La palabra era:", palabra
    FIN SI
FIN
```

## Variables Necesarias

| Variable | Tipo | Propósito |
|----------|------|-----------|
| palabra | str | Palabra a adivinar (mayúsculas) |
| palabra_oculta | str | Estado actual con _ y letras adivinadas |
| letra | str | Letra introducida por el jugador |
| letras_usadas | list | Lista de letras ya usadas |
| intentos | int | Número de intentos restantes |
| ganado | bool | Indica si se ha ganado el juego |
| INTENTOS_MAXIMOS | int | Constante con el número inicial de intentos |

## Estructuras de Control Necesarias

### Bucles While
1. **Validación de palabra**: Repetir hasta que sea válida
2. **Validación de letra**: Repetir hasta que sea válida
3. **Bucle principal**: Mientras haya intentos y no se haya ganado

### Bucles For
1. **Recorrer palabra**: Para actualizar palabra_oculta con las letras adivinadas

### Condicionales If
1. Validar longitud de palabra
2. Validar que solo contenga letras
3. Validar letra única
4. Comprobar si letra está en letras_usadas
5. Comprobar si letra está en palabra
6. Comprobar si se ha ganado (no hay '_' en palabra_oculta)
7. Mostrar mensaje final según resultado

## Funciones Útiles de Python

### String
- `upper()`: Convertir a mayúsculas
- `isalpha()`: Verificar si es letra
- `len()`: Obtener longitud
- `in`: Verificar si carácter está en string
- `replace()`: Reemplazar caracteres

### List
- `[]`: Crear lista vacía
- `append()`: Añadir elemento
- `in`: Verificar si elemento está en lista

### Built-in
- `enumerate()`: Obtener índice y valor en bucle for
- `input()`: Leer entrada del usuario
- `print()`: Mostrar salida

## Consejos para la Implementación

1. **Empezar simple**: Implementar primero la lógica básica sin validaciones
2. **Probar frecuentemente**: Ejecutar el código después de cada función
3. **Validar paso a paso**: Añadir validaciones una vez que la lógica básica funcione
4. **Usar funciones**: Dividir el código en funciones pequeñas y reutilizables
5. **Comentar el código**: Explicar qué hace cada parte

## Posibles Mejoras (Opcional)

- Permitir frases con espacios
- Mantener puntuación del jugador
- Jugar varias partidas
- Dibujar el ahorcado con ASCII art
- Añadir categorías de palabras
- Mostrar pistas
- Sistema de dificultad (más o menos intentos)
