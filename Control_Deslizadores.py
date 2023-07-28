#declaramos librerias
import serial       #Comunicacion arduino + python /pip install serial
import time         #Establecer un tiempo de espera
import tkinter as tk #Interfaz GUI 

#Controlar el brillo de los led
def update_led_brightness():
    brillo_rojo = red_slider.get() #deslizador del led rojo 1
    brillo_rojo2 = red2_slider.get() #deslizador del led rojo 2
    brillo_verde = green_slider.get() #deslizador del led verde

    # Preparamos el mensaje a ser transmitido
    message_to_serial = f"{brillo_rojo},{brillo_rojo2},{brillo_verde}"  # Enviaremos el valor de brillo para los 3 LEDs
 
    # Enviamos al puerto
    serialport.write(message_to_serial.encode())

    # Procesamos la respuesta
    message_from_serial = serialport.readline().decode().strip()
  
    # Imprimir los valores de brillo en pantalla
    print(f'Intensidad establecida Rojo: {brillo_rojo}')
    print(f'Intensidad establecida Rojo secundario: {brillo_rojo2}')
    print(f'Intensidad establecida Verde: {brillo_verde}')

def increase_brightness(slider):
    current_value = slider.get()
    if current_value < slider.cget("to"):
        slider.set(current_value + 5) #Cantidad de aumento del valor/coordenada

def decrease_brightness(slider):
    current_value = slider.get()
    if current_value > slider.cget("from"):
        slider.set(current_value - 5) #Cantidad de reducción del valor/coordenada

# Configuración del puerto serie
serialport = serial.Serial('COM4', 9600)#Comunicacion con el puerto serial y su taza de baudios
time.sleep(0.1)   # tiempo de espera recomendado: 100 ms

#creación de la ventana
root = tk.Tk() 
root.title("Control de LEDs") #Creamos el titulo de la ventana
root.geometry("700x450") #Establecemos el tamaño de la ventana

# Slider y botones para el brillo del LED rojo (0-255)
frame_red = tk.Frame(root)
frame_red.pack(pady=20)
red_decrease_button = tk.Button(frame_red, text="-", command=lambda: decrease_brightness(red_slider))
red_decrease_button.pack(side=tk.LEFT)
red_slider = tk.Scale(frame_red, from_=0, to=255, orient="horizontal",label="Brillo LED rojo")
red_slider.pack(side=tk.LEFT, padx=10)
red_increase_button = tk.Button(frame_red, text="+", command=lambda: increase_brightness(red_slider))
red_increase_button.pack(side=tk.LEFT)


# Slider y botones para el brillo del LED rojo secundario (0-255)
frame_red2 = tk.Frame(root)
frame_red2.pack(pady=20)
red2_decrease_button = tk.Button(frame_red2, text="-", command=lambda: decrease_brightness(red2_slider))
red2_decrease_button.pack(side=tk.LEFT)
red2_slider = tk.Scale(frame_red2, from_=0, to=255, orient="horizontal",label="Brillo LED rojo secundario")
red2_slider.pack(side=tk.LEFT, padx=10)
red2_increase_button = tk.Button(frame_red2, text="+", command=lambda: increase_brightness(red2_slider))
red2_increase_button.pack(side=tk.LEFT)

# Slider y botones para el brillo del LED verde (0-255)
frame_green = tk.Frame(root)
frame_green.pack(pady=20)
green_decrease_button = tk.Button(frame_green, text="-", command=lambda: decrease_brightness(green_slider))
green_decrease_button.pack(side=tk.LEFT)
green_slider = tk.Scale(frame_green, from_=0, to=255, orient="horizontal",label="Brillo LED verde")
green_slider.pack(side=tk.LEFT, padx=10)
green_increase_button = tk.Button(frame_green, text="+", command=lambda: increase_brightness(green_slider))
green_increase_button.pack(side=tk.LEFT)

# Botón para actualizar el brillo de los LEDs
update_button = tk.Button(root, text="Actualizar", command=update_led_brightness)
update_button.pack(pady=10)

# Bucle principal de la aplicación
root.mainloop()

# Cerrar el puerto serial al cerrar la ventana de Tkinter
serialport.close()
print('El puerto se ha cerrado correctamente')# se imprime un mensaje por pantalla