import random

def juego_dados(dinero):
    print("\n🎲 Bienvenido al juego de dados 🎲")
    print("Intenta sacar un número mayor que la máquina.\n")

    while True:
        print(f"💰 Dinero actual: {dinero} €")
        try:
            apuesta = int(input("¿Cuánto quieres apostar? (0 para volver al menú): "))
        except ValueError:
            print("❌ Por favor, escribe un número válido.\n")
            continue

        if apuesta == 0:
            break
        if apuesta < 0:
            print("❌ No puedes apostar una cantidad negativa.\n")
            continue
        if apuesta > dinero:
            print("❌ No tienes suficiente dinero.\n")
            continue

        input("Pulsa ENTER para lanzar los dados...")

        jugador = random.randint(1, 6)
        maquina = random.randint(1, 6)

        print(f"\nTú sacaste: 🎯 {jugador}")
        print(f"La máquina sacó: 🤖 {maquina}")

        if jugador > maquina:
            dinero += apuesta
            print(f"🏆 ¡Ganaste! Ganas {apuesta} €. Nuevo saldo: {dinero} €\n")
        elif jugador < maquina:
            dinero -= apuesta
            print(f"😢 Perdiste {apuesta} €. Nuevo saldo: {dinero} €\n")
        else:
            print("🤝 ¡Empate! Nadie gana ni pierde dinero.\n")

        if dinero <= 0:
            print("💸 Te has quedado sin dinero... Fin del juego 😢\n")
            break

    return dinero


def juego_adivinar(dinero):
    print("\n🔮 Bienvenido al juego de adivinar el número 🔮")
    print("Adivina un número entre 1 y 10.\n")

    while True:
        print(f"💰 Dinero actual: {dinero} €")
        try:
            apuesta = int(input("¿Cuánto quieres apostar? (0 para volver al menú): "))
        except ValueError:
            print("❌ Por favor, escribe un número válido.\n")
            continue

        if apuesta == 0:
            break
        if apuesta < 0:
            print("❌ No puedes apostar una cantidad negativa.\n")
            continue
        if apuesta > dinero:
            print("❌ No tienes suficiente dinero.\n")
            continue

        numero_secreto = random.randint(1, 10)
        intentos = 0
        exito = False

        while True:
            try:
                intento = int(input("👉 Adivina el número (1-10): "))
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
                print(f"Lo lograste en {intentos} intentos 👏")
                exito = True
                break

            if intentos == 3:
                print(f"❌ Te quedaste sin intentos. El número era {numero_secreto}.\n")
                break

        if exito:
            ganancia = apuesta * 2
            dinero += ganancia
            print(f"🏆 ¡Ganaste {ganancia} €! Nuevo saldo: {dinero} €\n")
        else:
            dinero -= apuesta
            print(f"😢 Perdiste {apuesta} €. Nuevo saldo: {dinero} €\n")

        if dinero <= 0:
            print("💸 Te has quedado sin dinero... Fin del juego 😢\n")
            break

    return dinero


# --- MENÚ PRINCIPAL ---
dinero = 100  # saldo inicial
print("💵 Bienvenido al Casino Python 💵\n")
print(f"Comienzas con {dinero} €.\n")

while True:
    if dinero <= 0:
        print("No te queda dinero. El juego ha terminado. 😞")
        break

    print("✨ MENÚ DE JUEGOS ✨")
    print("1️⃣  Juego de Dados")
    print("2️⃣  Adivinar el Número")
    print("3️⃣  Salir")

    opcion = input("\nElige una opción (1-3): ")

    if opcion == '1':
        dinero = juego_dados(dinero)
    elif opcion == '2':
        dinero = juego_adivinar(dinero)
    elif opcion == '3':
        print(f"\nTe vas con {dinero} €. ¡Gracias por jugar! 👋")
        break
    else:
        print("\n❌ Opción no válida. Intenta otra vez.\n")
