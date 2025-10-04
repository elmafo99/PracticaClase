print("Hola , soy Aisha")
import random

print("🎲 Bienvenido al juego de dados 🎲")
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
        print("\nGracias por jugar. ¡Hasta pronto! 👋")
        break
