# Videogame-project

# Ping Pong Game by Pau Codina
This is a simple Ping Pong game created using Python's **tkinter** library.

 The game features a moving ball that bounces off the walls and a user-controlled platform on the left side of the screen. The objective is to keep the ball in play by moving the platform up and down.

## How to Run the Game
- Downolad the folder.

  ![image](https://github.com/Pauxavier/APA-TF_Pau_Codina/assets/130084912/910a853b-26df-454f-aede-502ac5f4c46b)

- Unzip the folder.

  ![image](https://github.com/Pauxavier/APA-TF_Pau_Codina/assets/130084912/41bc2a9b-9fb1-4c81-9005-e9777b8155d4)

- Run the file "Ping Pong UPC.exe".

  ![image](https://github.com/Pauxavier/APA-TF_Pau_Codina/assets/130084912/8bad2432-2eab-4860-a374-5cbdc9ec6fcb)

- The game now should look like this:

  ![image](https://github.com/Pauxavier/APA-TF_Pau_Codina/assets/130084912/472a0f4f-e2fb-4212-9bdd-aa7046ffe3e5)

## Code Overview

### Importing the Library

    import tkinter as tk


The tkinter library is imported to create the graphical user interface for the game.

### Creating the Game Window

    root = tk.Tk()
    root.title("Ping Pong UPC")

    canvas_width, canvas_height = 800, 600
    canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="black")
    canvas.pack()

A tkinter window (root) is created with a title **"Ping Pong UPC"**. A canvas is added to the window with dimensions 800x600 pixels and a black background.

### Ball Properties

    ball_radius = 20
    ball_color = "red"
    ball_pos = [canvas_width // 2, canvas_height // 2]
    ball_vel = [5, 5]  

The ball is defined with a radius of 20 pixels and red color. It starts at the center of the canvas and moves with a velocity of 5 pixels per frame in both x and y directions.

### Platform Properties

    platform_width = 20
    platform_height = 100
    platform_color = "blue"
    platform_x = 50  # Distance from the left wall
    platform_y = canvas_height // 2 - platform_height // 2
    platform_speed = 30

The platform is defined with a width of 20 pixels, height of 100 pixels, and blue color. It is positioned 50 pixels from the left wall and vertically centered. The platform moves at a speed of 30 pixels per frame.

### Creating the Ball and Platform

    ball = canvas.create_oval(ball_pos[0] - ball_radius, ball_pos[1] - ball_radius,
                          ball_pos[0] + ball_radius, ball_pos[1] + ball_radius,
                          fill=ball_color)

    platform = canvas.create_rectangle(platform_x, platform_y,
                                   platform_x + platform_width, platform_y + platform_height,
                                   fill=platform_color)

The ball and platform are drawn on the canvas using the defined properties.

### Score Counter

    score = 0

    score_label = tk.Label(root, text=f"FCB:4 RMA: {score}", fg="black", bg="white", font=("Helvetica", 16))
    score_label.pack()

A score counter is initialized and displayed on the window, showing the current score.

### Increment Velocity Function

    def increment_velocity():
        global ball_vel
        ball_vel[0] *= 1.3
        ball_vel[1] *= 1.3

The **increment_velocity** function increases the ball's velocity by 30% each time it is called.

### Ball Movement Function

    def move_ball():
    global ball_pos, ball_vel

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[0] <= ball_radius or ball_pos[0] >= canvas_width - ball_radius:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] <= ball_radius or ball_pos[1] >= canvas_height - ball_radius:
        ball_vel[1] = -ball_vel[1]

    canvas.coords(ball, ball_pos[0] - ball_radius, ball_pos[1] - ball_radius,
                  ball_pos[0] + ball_radius, ball_pos[1] + ball_radius)

    root.after(30, move_ball)

The **move_ball** function updates the ball's position based on its velocity. It checks for collisions with the walls and reverses the ball's direction if a collision occurs. If the ball hits the left wall, it resets to the starting position, increases the score, and updates the score display. The ball's new position is updated on the canvas, and the function is called again after 30 milliseconds. If the ball collides with the platform, its direction is reversed, and its speed increases by 30%.

### Platform Movement Functions

    def move_platform_up(event):
    global platform_y
    if platform_y > 0:
        platform_y -= platform_speed
        canvas.coords(platform, platform_x, platform_y,
                      platform_x + platform_width, platform_y + platform_height)

    def move_platform_down(event):
    global platform_y
    if platform_y < canvas_height - platform_height:
        platform_y += platform_speed
        canvas.coords(platform, platform_x, platform_y,
                      platform_x + platform_width, platform_y + platform_height)

These functions move the platform up or down when the up or down arrow keys are pressed. The platform's position is updated on the canvas.

### Key Bindings

    root.bind("<Up>", move_platform_up)
    root.bind("<Down>", move_platform_down)

The up and down arrow keys are bound to the **move_platform_up** and **move_platform_down** functions, respectively.

### Starting the Game

    move_ball()
    root.mainloop()

The **move_ball** function is called to start the ball's movement, and **root.mainloop()** starts the Tkinter main loop to run the game.
