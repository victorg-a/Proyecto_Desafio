#include <AccelStepper.h>

// Configuración de pines para los motores paso a paso
#define X_STEP_PIN 54
#define X_DIR_PIN 55

#define Y_STEP_PIN 60
#define Y_DIR_PIN 61

#define Z_STEP_PIN 46
#define Z_DIR_PIN 48

// Configuración de los pasos por revolución y velocidad para cada motor
#define STEPS_PER_REV 200  // Dependiendo del motor, puede ser 200 o 400
#define SPEED_X 1000       // Velocidad en pasos por segundo para el motor X
#define SPEED_Y 1000       // Velocidad en pasos por segundo para el motor Y
#define SPEED_Z 1000       // Velocidad en pasos por segundo para el motor Z

// Crear objetos AccelStepper para cada motor
AccelStepper stepperX(AccelStepper::DRIVER, X_STEP_PIN, X_DIR_PIN);
AccelStepper stepperY(AccelStepper::DRIVER, Y_STEP_PIN, Y_DIR_PIN);
AccelStepper stepperZ(AccelStepper::DRIVER, Z_STEP_PIN, Z_DIR_PIN);

void setup() {
  // Configuración de los motores
  stepperX.setMaxSpeed(SPEED_X);
  stepperY.setMaxSpeed(SPEED_Y);
  stepperZ.setMaxSpeed(SPEED_Z);

  // Iniciar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles desde Python
  if (Serial.available() >= 3) {
    // Leer los datos recibidos desde Python
    int angleX = Serial.read();
    int angleY = Serial.read();
    int angleZ = Serial.read();

    // Convertir los ángulos recibidos en pasos
    int stepsX = map(angleX, -180, 180, -STEPS_PER_REV, STEPS_PER_REV);
    int stepsY = map(angleY, -180, 180, -STEPS_PER_REV, STEPS_PER_REV);
    int stepsZ = map(angleZ, -180, 180, -STEPS_PER_REV, STEPS_PER_REV);

    // Mover los motores a las posiciones deseadas
    stepperX.moveTo(stepsX);
    stepperY.moveTo(stepsY);
    stepperZ.moveTo(stepsZ);

    // Hacer que los motores se muevan
    while (stepperX.distanceToGo() != 0 || stepperY.distanceToGo() != 0 || stepperZ.distanceToGo() != 0) {
      stepperX.run();
      stepperY.run();
      stepperZ.run();
    }
  }
}
