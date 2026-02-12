#include <SCServo.h>

SMS_STS st;
// Pines para los servos (ajusta si usas otros en tu shield)
#define S_RXD 18
#define S_TXD 19

int Y_MIN = 2500, Y_MAX = 4000;
int X_MIN = 500,  X_MAX = 3500;
int posX, posY;

// Parámetros iniciales de suavidad
int paso = 60;
int velocidad = 800;
int aceleracion = 20; 

void setup() {
    // La Jetson y el ESP32 deben hablar a la misma velocidad
    Serial.begin(115200); 
    
    // Comunicación con servos STS
    Serial2.begin(1000000, SERIAL_8N1, S_RXD, S_TXD);
    st.pSerial = &Serial2;

    delay(1000);
    
    // Sincronizar posición actual de los servos
    posY = st.ReadPos(2); if(posY == -1) posY = 3468;
    posX = st.ReadPos(1); if(posX == -1) posX = 2048;
}

void loop() {
    if (Serial.available()) {
        char c = Serial.read();

        // Movimiento (Comandos desde Python)
        if (c == 'U')      posY = constrain(posY + paso, Y_MIN, Y_MAX);
        else if (c == 'D') posY = constrain(posY - paso, Y_MIN, Y_MAX);
        else if (c == 'L') posX = constrain(posX + paso, X_MIN, X_MAX);
        else if (c == 'R') posX = constrain(posX - paso, X_MIN, X_MAX);
        
        // Ajustes de Sensibilidad (Nuevos casos)
        else if (c == '+') paso = min(paso + 15, 250);
        else if (c == '-') paso = max(paso - 15, 5);
        
        // Modalidades (1=Rápido, 2=Delicado/Pocos)
        else if (c == '1') { velocidad = 1200; aceleracion = 60; paso = 100; }
        else if (c == '2') { velocidad = 400;  aceleracion = 10; paso = 25; }

        // Ejecutar movimiento con los parámetros actuales
        st.WritePosEx(1, posX, velocidad, aceleracion);
        st.WritePosEx(2, posY, velocidad, aceleracion);
    }
}