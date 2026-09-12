def nexa():
    print("NEXA: Sistema iniciado.")
    print("NEXA: Hola. Soy NEXA, tu asistente virtual.")
    
    while True:
        usuario = input("Tú: ")

        if usuario.lower() in ["salir", "adios", "adiós"]:
            print("NEXA: Cerrando sistema. Hasta luego.")
            break

        elif "hola" in usuario.lower():
            print("NEXA: Hola. ¿Cómo estás?")

        elif "quien eres" in usuario.lower() or "quién eres" in usuario.lower():
            print("NEXA: Soy NEXA, Neural Exploration & eXecution Assistant.")

        else:
            print("NEXA: Recibí tu mensaje. Todavía estoy aprendiendo.")


nexa()