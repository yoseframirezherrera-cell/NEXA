

        
            def nexa():
    print("NEXA: Sistema iniciado.")
    print("NEXA: Hola. Soy NEXA, tu asistente virtual.")

    while True:
        usuario = input("Tú: ").lower().strip()

        if usuario in ["salir", "adios", "adiós"]:
            print("NEXA: Cerrando sistema. Hasta luego.")
            break

        elif "hola" in usuario:
            print("NEXA: Hola. ¿Cómo estás?")

        elif "quien eres" in usuario or "quién eres" in usuario:
            print("NEXA: Soy NEXA, Neural Exploration & eXecution Assistant.")

        elif "ayuda" in usuario:
            print("NEXA: Puedo responder algunos comandos básicos.")
            print("NEXA: Prueba diciendo: hola, quién eres o salir.")

        elif "gracias" in usuario:
            print("NEXA: De nada. Estoy aquí para ayudarte.")

        else:
            print("NEXA: Recibí tu mensaje. Todavía estoy aprendiendo.")


nexa()