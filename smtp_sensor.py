import os
import socket
import smtplib
import time


def send_mail_local(from_host, usuario, ip, dominio, puerto, subject, text):
    to_host = usuario + "@" + ip
    tiempo_inicial = int(time.time())

    msg = ("From: {0}\nTo: {1}\nSubject: {2}\n{3}".format(from_host, to_host, subject, text).encode('utf-8').strip())
    server = smtplib.SMTP()
    server.connect(dominio, puerto)
    # server.login ('francisco@redes.ejemplo.com', '')
    # server.set_debuglevel(True)
    try:
        server.sendmail(from_host, to_host, msg)  # from, to, msg
        tiempo_final = int(time.time())

        print("\nTiempo de respuesta: " + str(tiempo_final - tiempo_inicial))

    finally:
        server.quit()

    return


def start_smtp_sensor():
    from_host = "@".join([os.getenv("LOGNAME"), socket.gethostname()])
    usuario = input("Escribe el nombre de usuario destino: ")
    ip = input("Escribe la direccion ip del destino: ")
    dominio = input("Escribe el dominio: ")
    puerto = input("Escribe el puerto del dominio: ")
    sbj = "Comprobando el envío de correo localmente"
    txt = "Si puedes leer esto, tu servidor local SMTP está OK"
    send_mail_local(from_host, usuario, ip, dominio, puerto, sbj, txt)
    print("Comprueba el correo en tu buzón local")
