
#define LED_GREEN_PIN 3
#define LED_RED_PIN 6
#define LED_RED2_PIN 9

void setup() {
  // Configurar el pin del LED rojo como salida
  pinMode(LED_RED_PIN, OUTPUT);
  pinMode(LED_RED2_PIN, OUTPUT);  
  pinMode(LED_GREEN_PIN, OUTPUT);
  // Iniciar comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Verificar si hay datos disponibles desde Python
  if (Serial.available() >= 3) {
    // Leer los datos recibidos desde Python
    int led_rojo = Serial.parseInt(); // Leer el valor de brillo para el LED rojo
    int led_rojo2 = Serial.parseInt(); // Leer el valor de brillo para el LED rojo2
    int led_verde = Serial.parseInt(); // Leer el valor de brillo para el LED verde

    // Establecer el brillo del LED rojo utilizando PWM
    analogWrite(LED_RED_PIN, led_rojo);
    analogWrite(LED_RED2_PIN, led_rojo2);
    analogWrite(LED_GREEN_PIN, led_verde);        
    // Enviar una respuesta de confirmación a Python (opcional)
    Serial.print("Brillo LED Rojo recibido: ");
    Serial.println(led_rojo);
    Serial.print("Brillo segundo LED Rojo recibido: ");
    Serial.println(led_rojo2);
    Serial.print("Brillo LED Verde recibido: ");
    Serial.println(led_verde);
  }
}
