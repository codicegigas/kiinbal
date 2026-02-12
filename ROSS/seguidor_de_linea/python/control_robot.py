import serial
import time
import sys
import tty
import termios

# Configuración del puerto
port = '/dev/ttyUSB0'

try:
    # Aumentamos un poco el timeout para estabilidad en la lectura
    ser = serial.Serial(port, 115200, timeout=0.01)
    print(f"Conectado exitosamente a: {port}")
except Exception as e:
    print(f" Error: No se encontró el ESP32. Verifica el cable. ({e})")
    exit()

def getch():
    """ Lee una tecla del teclado sin necesidad de presionar Enter """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

print("\n========================================")
print("   CONTROL DE ROBOT - MODO CONSOLA")
print("========================================")
print(" [↑][↓][←][→] : Mover Robot")
print(" [+] / [-]     : Ajustar Sensibilidad")
print(" [1] / [2]     : Cambiar Modos")
print(" [Q]           : Salir del programa")
print("========================================\n")

try:
    while True:
        char = getch()

        # Detección de flechas (Secuencias de escape ANSI)
        if char == '\x1b': 
            next1 = getch()
            next2 = getch()
            if next2 == 'A': 
                ser.write(b'U')
                print("  MOVIMIENTO: ARRIBA", end='\r')
            elif next2 == 'B': 
                ser.write(b'D')
                print("  MOVIMIENTO: ABAJO ", end='\r')
            elif next2 == 'C': 
                ser.write(b'R')
                print("  MOVIMIENTO: DERECHA", end='\r')
            elif next2 == 'D': 
                ser.write(b'L')
                print("  MOVIMIENTO: IZQUIERDA", end='\r')
        
        # Ajustes de Paso/Sensibilidad
        elif char == '+': 
            ser.write(b'+')
            print(" SENSIBILIDAD: Aumentando paso...", end='\r')
        elif char == '-': 
            ser.write(b'-')
            print(" SENSIBILIDAD: Reduciendo paso... ", end='\r')
        
        # Modos de operación
        elif char == '1': 
            ser.write(b'1')
            print("\n MODO ACTIVADO: [1] RÁPIDO / AGRESIVO")
        elif char == '2': 
            ser.write(b'2')
            print("\n MODO ACTIVADO: [2] LENTO / DELICADO")
        
        # Salida
        elif char.lower() == 'q':
            print("\n\nCerrando comunicación...")
            break

        # Limpiar el buffer de salida para que se vea en tiempo real
        sys.stdout.flush()

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")

finally:
    ser.close()
    print(" Puerto serial cerrado.")
    
    
    
