from easysnmp import Session
import telnetlib
import time


def make_telnet_connection():
    host = input("Ingresa la dirección del servidor TELNET: ")
    user = input("Ingresa el usuario: ")
    password = input("Ingresa la contraseña: ")

    start_time = int(time.time())
    try:
        tn = telnetlib.Telnet(host)
        tn.read_until(b"User: ")
        tn.write(user.encode('ascii') + b"\n")
        if password:
            tn.read_until(b"Password: ")
            tn.write(password.encode('ascii') + b"\n")

        tn.interact()

        print(tn.read_all().decode('ascii'))
    except Exception as e:
        print(e)

    final_time = int(time.time())
    print("\nTiempo de interacción: " + str(final_time - start_time))

    session = Session(hostname='localhost', community="MacCommunity", version=2)
    trafico_recibido = session.walk('1.3.6.1.2.1.2.2.1.10')
    trafico_enviado = session.walk('1.3.6.1.2.1.2.2.1.16')
    print("Trafico recibido: " + str(trafico_recibido))
    print("Trafico enviado: " + str(trafico_enviado))

