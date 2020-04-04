import tkinter as tk 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False) 
Red = 21
Blue = 20
Green = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(Red,GPIO.OUT)
GPIO.setup(Blue,GPIO.OUT)
GPIO.setup(Green,GPIO.OUT)

root = tk.Tk()
root.title("GUI GPIO Control")

def TurnOff():
    GPIO.output(Red, GPIO.LOW)
    GPIO.output(Blue, GPIO.LOW)
    GPIO.output(Green, GPIO.LOW)
    
def TurnOn():
    TurnOff()
    GPIO.output(r.get(),GPIO.HIGH)
    
r = tk.IntVar()

R1 = tk.Radiobutton(root, text="Red", variable=r,value=20, command=TurnOn).pack()
R2 = tk.Radiobutton(root, text="Blue", variable=r,value=21, command=TurnOn).pack()
R3 = tk.Radiobutton(root, text="Green", variable=r,value=16, command=TurnOn).pack()
tk.Exitbutton = tk.Button(root, text="Exit",bg="red", command=root.destroy).pack()

root.mainloop()

GPIO.cleanup()
