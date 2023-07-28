import tkinter as tk
import serial
import time

# Configuración del puerto serie
arduino_port = 'COM1'  # Ajustar según el puerto en el que está conectado el Arduino
baud_rate = 9600

# Abrir la conexión con Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Esperar un momento para que Arduino se inicialice

def update_robot_movement():
    # Obtener los valores de los sliders y campos de entrada
    angle_x = angle_slider_x.get()
    angle_y = angle_slider_y.get()
    angle_z = angle_slider_z.get()

    coord_x = coord_entry_x.get()
    coord_y = coord_entry_y.get()
    coord_z = coord_entry_z.get()

    # Aquí puedes agregar la lógica para mover tus motores X, Y y Z según los valores de ángulo y coordenadas
    print(f"Ángulo X: {angle_x}, Ángulo Y: {angle_y}, Ángulo Z: {angle_z}")
    print(f"Coordenada X: {coord_x}, Coordenada Y: {coord_y}, Coordenada Z: {coord_z}")

def reset_sliders():
    angle_slider_x.set(0)
    angle_slider_y.set(0)
    angle_slider_z.set(0)

    coord_entry_x.delete(0, tk.END)
    coord_entry_y.delete(0, tk.END)
    coord_entry_z.delete(0, tk.END)

# Crear la ventana
root = tk.Tk()
root.title("Control de Robot")

# Ajustar el tamaño de la ventana
root.geometry("700x500")

# Slider para el ángulo X de giro (-180 a 180 grados)
angle_slider_x = tk.Scale(root, from_=-180, to=180, orient="horizontal", label="Ángulo X")
angle_slider_x.grid(row=0, column=0, padx=10, pady=5)

# Slider para el ángulo Y de giro (-180 a 180 grados)
angle_slider_y = tk.Scale(root, from_=-180, to=180, orient="horizontal", label="Ángulo Y")
angle_slider_y.grid(row=1, column=0, padx=10, pady=5)
##
# Slider para el ángulo Z de giro (-180 a 180 grados)
angle_slider_z = tk.Scale(root, from_=-180, to=180, orient="horizontal", label="Ángulo Z")
angle_slider_z.grid(row=2, column=0, padx=10, pady=5)

# Campo de entrada para la coordenada X
coord_label_x = tk.Label(root, text="Coordenada X:")
coord_label_x.grid(row=0, column=1, padx=10, pady=5)
coord_entry_x = tk.Entry(root)
coord_entry_x.grid(row=0, column=2, padx=10, pady=5)

# Campo de entrada para la coordenada Y
coord_label_y = tk.Label(root, text="Coordenada Y:")
coord_label_y.grid(row=1, column=1, padx=10, pady=5)
coord_entry_y = tk.Entry(root)
coord_entry_y.grid(row=1, column=2, padx=10, pady=5)

# Campo de entrada para la coordenada Z
coord_label_z = tk.Label(root, text="Coordenada Z:")
coord_label_z.grid(row=2, column=1, padx=10, pady=5)
coord_entry_z = tk.Entry(root)
coord_entry_z.grid(row=2, column=2, padx=10, pady=5)

# Botones para reiniciar sliders
reset_button_x = tk.Button(root, text="Reiniciar Ángulo X", command=lambda: angle_slider_x.set(0))
reset_button_x.grid(row=0, column=3, padx=10, pady=5)

reset_button_y = tk.Button(root, text="Reiniciar Ángulo Y", command=lambda: angle_slider_y.set(0))
reset_button_y.grid(row=1, column=3, padx=10, pady=5)

reset_button_z = tk.Button(root, text="Reiniciar Ángulo Z", command=lambda: angle_slider_z.set(0))
reset_button_z.grid(row=2, column=3, padx=10, pady=5)

reset_button_coord_x = tk.Button(root, text="Reiniciar Coordenada X", command=lambda: coord_entry_x.delete(0, tk.END))
reset_button_coord_x.grid(row=0, column=4, padx=10, pady=5)

reset_button_coord_y = tk.Button(root, text="Reiniciar Coordenada Y", command=lambda: coord_entry_y.delete(0, tk.END))
reset_button_coord_y.grid(row=1, column=4, padx=10, pady=5)

reset_button_coord_z = tk.Button(root, text="Reiniciar Coordenada Z", command=lambda: coord_entry_z.delete(0, tk.END))
reset_button_coord_z.grid(row=2, column=4, padx=10, pady=5)

# Botón para actualizar el movimiento de los motores
update_button = tk.Button(root, text="Actualizar", command=update_robot_movement)
update_button.grid(row=3, column=0, columnspan=5, padx=10, pady=20)

# Leer los valores de los sliders o coordenadas desde el usuario
angle_x = 45  # Ángulo de giro para el motor X
angle_y = -90  # Ángulo de giro para el motor Y
angle_z = 0  # Ángulo de giro para el motor Z

# Enviar los datos al Arduino
ser.write(chr(angle_x).encode())
ser.write(chr(angle_y).encode())
ser.write(chr(angle_z).encode())

# Cerrar la conexión
ser.close()

# Bucle principal de la aplicación
root.mainloop()