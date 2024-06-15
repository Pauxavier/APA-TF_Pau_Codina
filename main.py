# Ping Pong creado por Pau Codina 

import tkinter as tk

# Creamos la ventana donde se ejecutará el videojuego
root = tk.Tk()
root.title("Ping Pong UPC")

# Modificamos el tamaño y el color del fondo de la ventana
canvas_width, canvas_height = 800, 600
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="green")
canvas.pack()

# Creamos las propiedades de la pelota
ball_radius = 20
ball_color = "white"
start_pos = [canvas_width // 2, canvas_height // 2]
ball_pos = start_pos.copy()
initial_vel = 5
ball_vel = [initial_vel, initial_vel]  # Velocidad en ambas direcciones (x, y)

# Creamos las propiedades de la plataforma
platform_width = 20
platform_height = 100
platform_color = "blue"
platform_x = 50  # Distáncia con la pared izquierda
platform_y = canvas_height // 2 - platform_height // 2
platform_speed = 20

# Creamos la pelota
ball = canvas.create_oval(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius,
                          ball_pos[0] + ball_radius, ball_pos[1] + ball_radius,
                          fill=ball_color)

# Creamos la plataforma
platform = canvas.create_rectangle(platform_x, platform_y,
                                   platform_x + platform_width, platform_y + platform_height,
                                   fill=platform_color)

# Inicializamos el contador para el marcador
score = 0

# Mostramos el marcador en la ventana
score_label = tk.Label(root, text=f"FCB:4 RMA: {score}", fg="black", bg="white", font=("Helvetica", 16))
score_label.pack()

# Función para incrementar la velocidad de la pelota
def increment_velocity():
    global ball_vel
    ball_vel[0] *= 1.3
    ball_vel[1] *= 1.3

# Creamos la función que permite el movimiento de la pelota
def move_ball():
    global ball_pos, ball_vel, score

    # Actualizamos el movimiento de la pelota
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Miramos si la pelota toca el lado izquierdo
    if ball_pos[0] <= ball_radius:
        ball_pos = start_pos.copy()
        ball_vel = [initial_vel, initial_vel]
        score += 1
        score_label.config(text=f"FCB:4 RMA: {score}")  

    # Miramos si la pelota toca el lado derecho
    if ball_pos[0] >= canvas_width - ball_radius:
        ball_vel[0] = -ball_vel[0]

    # Generamos físicas en las paredes para que la pelota rebote
    if ball_pos[1] <= ball_radius or ball_pos[1] >= canvas_height - ball_radius:
        ball_vel[1] = -ball_vel[1]

    # Verificamos colisión con la plataforma
    platform_coords = canvas.coords(platform)
    if (platform_coords[0] <= ball_pos[0] - ball_radius <= platform_coords[2] and
        platform_coords[1] <= ball_pos[1] <= platform_coords[3]):
        ball_vel[0] = -ball_vel[0]
        increment_velocity()

    # Damos la orden de que se prepare el siguiente movimiento
    canvas.coords(ball, ball_pos[0] - ball_radius, ball_pos[1] - ball_radius,
                  ball_pos[0] + ball_radius, ball_pos[1] + ball_radius)
    root.after(30, move_ball)

# Creamos el movimiento hacia arriba de la plataforma
def move_platform_up(event):
    global platform_y
    if platform_y > 0:
        platform_y -= platform_speed
        canvas.coords(platform, platform_x, platform_y,
                      platform_x + platform_width, platform_y + platform_height)

# Creamos el movimiento hacia abajo de la plataforma
def move_platform_down(event):
    global platform_y
    if platform_y < canvas_height - platform_height:
        platform_y += platform_speed
        canvas.coords(platform, platform_x, platform_y,
                      platform_x + platform_width, platform_y + platform_height)

# Designamos las teclas encargadas del movimiento de la plataforma
root.bind("<Up>", move_platform_up)
root.bind("<Down>", move_platform_down)

# Empezamos el movimiento de la pelota
move_ball()

# Loop principal del tkinter
root.mainloop()

