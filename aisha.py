print("Hola , soy Aisha")
import random

def juego_dados():
    print("\n🎲 Bienvenido al juego de dados 🎲")
    print("Intenta sacar un número mayor que la máquina.\n")

    while True:
        input("Pulsa ENTER para lanzar los dados...")

        jugador = random.randint(1, 6)
        maquina = random.randint(1, 6)

        print(f"\nTú sacaste: 🎯 {jugador}")
        print(f"La máquina sacó: 🤖 {maquina}")

        if jugador > maquina:
            print("🏆 ¡Ganaste esta ronda!\n")
        elif jugador < maquina:
            print("😢 La máquina gana esta ronda.\n")
        else:
            print("🤝 ¡Empate!\n")

        continuar = input("¿Quieres jugar otra ronda? (s/n): ").lower()
        if continuar != 's':
            print("\nGracias por jugar al juego de dados 👋\n")
            break


def juego_adivinar():
    print("\n🔮 Bienvenido al juego de adivinar el número 🔮")
    print("Tienes que adivinar un número entre 1 y 10.\n")

    numero_secreto = random.randint(1, 10)
    intentos = 0

    while True:
        try:
            intento = int(input("👉 Escribe tu número: "))
        except ValueError:
            print("Por favor, escribe un número válido.")
            continue

        intentos += 1

        if intento < numero_secreto:
            print("🔼 El número secreto es mayor.\n")
        elif intento > numero_secreto:
            print("🔽 El número secreto es menor.\n")
        else:
            print(f"🎉 ¡Correcto! El número era {numero_secreto}.")
            print(f"Lo lograste en {intentos} intentos 👏\n")
            break

    print("Gracias por jugar al juego de adivinar el número 👋\n")


# --- MENÚ PRINCIPAL ---
while True:
    print("✨ MENÚ DE JUEGOS ✨")
    print("1️⃣  Juego de Dados")
    print("2️⃣  Adivinar el Número")
    print("3️⃣  Salir")

    opcion = input("\nElige una opción (1-3): ")

    if opcion == '1':
        juego_dados()
    elif opcion == '2':
        juego_adivinar()
    elif opcion == '3':
        print("\nGracias por jugar. ¡Hasta pronto! 👋")
        break
    else:
        print("\n❌ Opción no válida. Intenta otra vez.\n")
