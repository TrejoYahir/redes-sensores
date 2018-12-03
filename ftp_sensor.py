from ftplib import FTP
import time


def test_connection(ip, user, password, folder):
    start_time = int(time.time())
    ftp = FTP()
    try:
        ftp.connect(ip, 21)
        ftp.login(user, password)
        print(ftp.getwelcome())
        if folder is not None:
            try:
                print('Directorio ' + folder)
                ftp.cwd(folder)
            except Exception as e:
                print(e)
        else:
            print('Directorio ' + ftp.pwd())
        print("Lista de archivos: ")
        ftp.retrlines('LIST')
        ftp.quit()
    except Exception as e:
        print(e)
    final_time = int(time.time())
    print("\nTiempo de respuesta: " + str(final_time - start_time))


def make_ftp_connection():
    selected_ip = input("Ingresa la dirección del servidor: ")
    user = input("Ingresa el usuario: ")
    password = input("Ingresa la contraseña: ")
    try:
        folder = input("Si deseas ver un directorio en particular escribelo aquí: ")
    except SyntaxError:
        folder = None
    test_connection(selected_ip, user, password, folder)
