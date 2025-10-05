import random

# Leer palabras desde el archivo palabras_rae.txt
with open('palabras_rae.txt', encoding='utf-8') as f:
    palabras = [line.strip() for line in f if line.strip()]

palabra = random.choice(palabras)
letras_adivinadas = []
intentos = 6
print(palabra)  # Para pruebas, se puede comentar en producción

# Dibujo del ahorcado según los intentos restantes
def mostrar_ahorcado(intentos):
    estados = [
      """
  +---+
  |   |
    |
    |
    |
    |
=========""",
      """
  +---+
  |   |
  O   |
    |
    |
    |
=========""",
      """
  +---+
  |   |
  O   |
  |   |
    |
    |
=========""",
      """
  +---+
  |   |
  O   |
 /|   |
    |
    |
=========""",
      """
  +---+
  |   |
  O   |
 /|\  |
    |
    |
=========""",
      """
  +---+
  |   |
  O   |
 /|\  |
 /    |
    |
=========""",
      """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
    |
========="""
    ]
    print(estados[6 - intentos])

print("¡Bienvenido al juego del ahorcado!")
print(f"La palabra tiene {len(palabra)} letras.")
print(f"Tienes {intentos} intentos para adivinar la palabra.")
# print(palabra)  # Quitar para no mostrar la palabra al inicio

while intentos > 0:
    mostrar_ahorcado(intentos)
    mostrar = ''
    for letra in palabra:
        if letra in letras_adivinadas:
            mostrar += letra
        else:
            mostrar += '_'
    print(mostrar)

    if mostrar == palabra:
        print("¡Felicidades! Has adivinado la palabra.")
        break

    intento = input("Adivina una letra: ").lower()
    if intento in letras_adivinadas:
        print("Ya has adivinado esa letra.")
        continue

    if intento in palabra:
        letras_adivinadas.append(intento)
        print("¡Bien hecho!")
    else:
        letras_adivinadas.append(intento)
        intentos -= 1
        print(f"Letra incorrecta. Te quedan {intentos} intentos.")

if intentos == 0:
    mostrar_ahorcado(intentos)
    print(f"Has perdido. La palabra era: {palabra}")