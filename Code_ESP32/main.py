import time
import network
import socket
import esp
import os
import _thread as thread
from machine import Pin, PWM, ADC
esp.osdebug(None)

# Configuration du premier servomoteur
# L'auriculaire
servo1_pin = 14
servo1_pwm = PWM(Pin(servo1_pin), freq=50)
servo1_min = 40
servo1_max = 100

# Configuration du deuxième servomoteur
# L'Annulaire
servo2_pin = 12
servo2_pwm = PWM(Pin(servo2_pin), freq=50)
servo2_min = 40
servo2_max = 100

# Configuration du troisième servomoteur
# Le Majeur
servo3_pin = 13
servo3_pwm = PWM(Pin(servo3_pin), freq=50)
servo3_min = 40
servo3_max = 100

# Configuration du quatrième servomoteur
# L'Index
servo4_pin = 27
servo4_pwm = PWM(Pin(servo4_pin), freq=50)
servo4_min = 40
servo4_max = 100

# Configuration du cinquième servomoteur
# Le Pouce
servo5_pin = 26
servo5_pwm = PWM(Pin(servo5_pin), freq=50)
servo5_min = 40
servo5_max = 100

# Configuration du point d'accès WiFi
ssid = 'Mon réseau chelou'
password = ''

# Fonction pour contrôler le servo-moteur
def control_servo1(angle):
    servo1_pwm.duty(angle)
def control_servo2(angle):
    servo2_pwm.duty(angle)
def control_servo3(angle):
    servo3_pwm.duty(angle)
def control_servo4(angle):
    servo4_pwm.duty(angle)
def control_servo5(angle):
    servo5_pwm.duty(angle)

# Configuration du WiFi en point d'accès
def setup_wifi():        
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=ssid, password=password)
    print('Point d\'accès WiFi créé avec succès')
    print(ap.ifconfig())

# Fonction pour gérer les requêtes HTTP
def http_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('', 80))
    sock.listen(5)
    sock.settimeout(10)  # Définir un délai d'attente de 10 secondes
    print("Serveur HTTP démarré.")
    while True:
        try:
            client, addr = sock.accept()
            print('Nouvelle connexion depuis:', addr)
            request = client.recv(1024)
            request = str(request)
            print("Requête reçue:", request)

            # page 
            if 'GET /index' in request:
                print("Requête pour la page index.")
                with open('/templates/index.html', 'r') as f:
                    response = f.read()
            # Fonction
            # Servo 1
            elif 'GET /servo1/on' in request:
                print("Requête pour déplacer le servo à 40 degrés.")
                control_servo1(servo1_min)
                response = 'Servo moved to 40 degrees'
            elif 'GET /servo1/off' in request:
                print("Requête pour déplacer le servo à 100 degrés.")
                control_servo1(servo1_max)
                response = 'Servo moved to 100 degrees'
            # Servo 2
            elif 'GET /servo2/on' in request:
                print("Requête pour déplacer le servo à 40 degrés.")
                control_servo2(servo2_min)
                response = 'Servo moved to 40 degrees'
            elif 'GET /servo2/off' in request:
                print("Requête pour déplacer le servo à 100 degrés.")
                control_servo2(servo2_max)
                response = 'Servo moved to 100 degrees'
            # Servo 3
            elif 'GET /servo3/on' in request:
                print("Requête pour déplacer le servo à 40 degrés.")
                control_servo3(servo3_min)
                response = 'Servo moved to 40 degrees'
            elif 'GET /servo3/off' in request:
                print("Requête pour déplacer le servo à 100 degrés.")
                control_servo3(servo3_max)
                response = 'Servo moved to 100 degrees'
            # Servo 4
            elif 'GET /servo4/on' in request:
                print("Requête pour déplacer le servo à 40 degrés.")
                control_servo4(servo4_min)
                response = 'Servo moved to 40 degrees'
            elif 'GET /servo4/off' in request:
                print("Requête pour déplacer le servo à 100 degrés.")
                control_servo4(servo4_max)
                response = 'Servo moved to 100 degrees'
            # Servo 5
            elif 'GET /servo5/on' in request:
                print("Requête pour déplacer le servo à 40 degrés.")
                control_servo5(servo5_min)
                response = 'Servo moved to 40 degrees'
            elif 'GET /servo5/off' in request:
                print("Requête pour déplacer le servo à 100 degrés.")
                control_servo5(servo5_max)
                response = 'Servo moved to 100 degrees'
            else:
                response = ''

            client.send('HTTP/1.1 200 OK\n')
            client.send('Content-Type: text/html\n')
            client.send('Connection: close\n\n')
            client.sendall(response.encode())
            client.close()
        except OSError as e:
            if e.args[0] == 116:
                print("La connexion a expiré.")
            else:
                print("Erreur lors de l'acceptation de la connexion:", e)

# Fonction principale
def main():
    setup_wifi()
    # Lancer le serveur HTTP dans un thread séparé
    thread.start_new_thread(http_server, ())
    print("Serveur HTTP démarré.")

if __name__ == "__main__":
    main()
