import tkinter as tk
import time

def change_lights():
    # Turn off all lights
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(orange_light, fill="gray")
    canvas.itemconfig(green_light, fill="gray")
    root.update()

    time.sleep(1)

    # Turn on red light
    canvas.itemconfig(red_light, fill="red")
    root.update()
    time.sleep(5)

    # Turn off red light and turn on orange light
    canvas.itemconfig(red_light, fill="gray")
    canvas.itemconfig(orange_light, fill="orange")
    root.update()
    time.sleep(1)

    # Turn off orange light and turn on green light
    canvas.itemconfig(orange_light, fill="gray")
    canvas.itemconfig(green_light, fill="green")
    root.update()
    time.sleep(10)

    # Repeat the cycle
    change_lights()

root = tk.Tk()
root.title("Traffic Lights")

canvas = tk.Canvas(root, width=200, height=500, bg="white")
canvas.pack()

# Draw traffic lights
red_light = canvas.create_oval(50, 50, 150, 150, fill="gray")
orange_light = canvas.create_oval(50, 200, 150, 300, fill="gray")
green_light = canvas.create_oval(50, 350, 150, 450, fill="gray")

# Start the automatic light change cycle
change_lights()

root.mainloop()
