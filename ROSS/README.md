# 🤖 Seguidor de Línea - Etapa 1: Control Manual de Precisión

Este repositorio contiene la implementación técnica de la **Etapa 1** del proyecto de visión por computadora. El objetivo es permitir el manejo manual de una mira robótica mediante servos de alta precisión para realizar pruebas de seguimiento antes de la automatización total.

---

### 🧠 1. Planeación y Lógica del Sistema
El sistema establece un control robusto y flexible de servos conectados a un ESP32 mediante comunicación TTL, recibiendo comandos desde una NVIDIA Jetson Nano.

**Puntos Clave:**
* **Sincronización:** El sistema lee la posición real de los servos al iniciar para evitar saltos bruscos.
* **Control en 2 Ejes:** Movimientos en X (Pan) y Y (Tilt) de forma suave y parametrizable.
* **Modos de Operación:** Selección entre modo **Rápido/Agresivo** para agilidad y **Lento/Delicado** para precisión en la mira.



---

### 💻 2. Código de Implementación

#### A. Control Maestro (Python)
Interfaz en consola que abre el puerto `/dev/ttyUSB0` y captura teclas en tiempo real (flechas, números y signos) sin necesidad de presionar "Enter".

```python
# Ubicación: python/control_robot.py
# Captura secuencias de escape ANSI para las flechas del teclado.

```
## 🤖 B. Firmware del Controlador (Arduino/ESP32)

Este módulo se encarga de traducir los caracteres recibidos por el puerto serial en movimientos específicos para los servos **STS3215**.

* **Lenguaje:** `C++`
* **Ubicación:** `arduino/Arduinoesp32GDFR.ino`
* **Configuración:** Comunicación Half-duplex a **1,000,000 bps** con los servos.

---

## 🛠️ 3. Hardware Utilizado

Se utiliza la placa **General Driver for Robots** de Waveshare, optimizada para el protocolo de comunicación de los servos de la misma marca.

* **Controlador:** ESP32 General Driver (Waveshare).
* **Servos:** STS3215 (Control por bus serial TTL).
* **Chasis:** Rover Waveshare para estabilidad mecánica.

### Mapeo de Comandos (Control Serial)

| Tecla / Comando | Acción en Hardware | Descripción |
| :---: | :--- | :--- |
| `↑` / `↓` | **Movimiento Eje Y** | Incrementa/Decrementa posición vertical. |
| `←` / `→` | **Movimiento Eje X** | Incrementa/Decrementa posición horizontal. |
| `+` / `-` | **Ajuste de Sensibilidad** | Cambia el tamaño del paso del servo. |
| `1` / `2` | **Cambio de Modo** | Alterna velocidad y aceleración predefinida. |

---

## 📋 4. Guía de Preparación

Según la documentación técnica, los pasos para preparar el entorno son:

1.  **Arduino IDE:** Instalar y agregar URL de tarjetas ESP32 en *Archivo > Preferencias*:  
    `https://espressif.github.io/arduino-esp32/package_esp32_index.json`
2.  **Drivers:** Instalar los controladores **USB to UART Bridge VCP** de Silicon Labs.
3.  **Librerías:** Instalar `SCServo.h` para habilitar la comunicación con los servos STS.

---

## 📄 5. Documentación Completa (PDF)

Para más detalles sobre la instalación de drivers en Windows/Linux y resultados detallados, consulta el archivo original en la carpeta de documentación:

 [Ver Informe Técnico: Sistema de control remoto de servos.pdf](./ROSS/seguidor_de_linea/documentacion/Sistema%20de%20control%20remoto%20de%20servos%20con%20el%20Rover%20para%20mover%20la%20camara.pdf)
