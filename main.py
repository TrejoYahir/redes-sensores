from http_sensor import http_request
from twogirlsoneCUPS import getinfoprinter
from smtp_sensor import start_smtp_sensor
from ftp_sensor import make_ftp_connection
from telnet_sensor import make_telnet_connection


def main():
    print('Elige el sensor que quieres usar: ')
    print('1. Sensor SMTP')
    print('2. Sensor HTTP')
    print('3. Sensor FTP')
    print('4. Sensor CUPS')
    print('5. Sensor TELNET')

    opc = int(input('Selecciona tu opcion: '))
    if opc == 1:
        print('SMTP\n')
        start_smtp_sensor()

    elif opc == 2:
        print('HTTP')
        url = input('Introduce la url del sitio web: ')
        [time, bts, speed] = http_request(url)
        print('Tiempo de respuesta: ', time)
        print('Bytes descargados: ', bts)
        print('Ancho de banda: ' + str(speed) + ' bytes por segundo')

    elif opc == 3:
        print('FTP')
        make_ftp_connection()

    elif opc == 4:
        print('CUPS')
        printer = input('Introduce la direccion de tu impresora: ')
        getinfoprinter(printer)

    elif opc == 5:
        print('TELNET')
        make_telnet_connection()
        
    else:
        print('No seleccionaste una opcion valida')


print('Buenas tardes, buenas noches, señoritas y señores')
go_agane = 's'

while go_agane == 's' or go_agane == 'S':
    main()
    go_agane = input('¿Quieres repetir? s/n ')
