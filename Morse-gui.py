from tkinter import *
import tkinter.font
import time
from gpiozero import LED
import RPi.GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)
window = Tk()
window.title("Morse code")
myFont= tkinter.font.Font(family = 'Helvetica', size = 12)
morse= ""
led= LED(16)


#Dot
def LedDot():
    led.on()
    time.sleep(0.25)
    led.off()
    time.sleep(0.6)
#Dash      
def LedDash():
    led.on()
    time.sleep(0.4)
    led.off()
    time.sleep(0.6)
#
def executeMorse():
    morse = morseEntry.get()
    letters = list(morse)
    for let in letters:
        led.off()
        if (let=="_"):
            time.sleep(1)
        if (let=="a" or let=="A"):
            LedDot()
            LedDash()
            time.sleep(1)
        if (let=="b" or let=="B"):
            LedDash()
            LedDot()
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="c" or let=="C"):
            LedDash()
            LedDot()
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="d" or let=="D"):
            LedDash()
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="e" or let=="E"):
            LedDot()
            time.sleep(1)
        if (let=="f" or let=="F"):
            LedDot()
            LedDot()
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="g" or let=="G"):
            LedDash()
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="h" or let=="H"):
            LedDot()
            LedDot()
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="i" or let=="I"):
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="j" or let=="J"):
            LedDot()
            LedDash()
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="k" or let=="K"):
            LedDash()
            LedDot()
            LedDash()
            time.sleep(1)
        if (let=="l" or let=="L"):
            LedDot()
            LedDash()
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="m" or let=="M"):
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="n" or let=="M"):
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="o" or let=="O"):
            LedDash()
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="p" or let=="P"):
            LedDot()
            LedDash()
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="q" or let=="Q"):
            LedDash()
            LedDash()
            LedDot()
            LedDash()
            time.sleep(1)
        if (let=="r" or let=="R"):
            LedDot()
            LedDash()
            LedDot()
            time.sleep(1)
        if (let=="s" or let=="S"):
            LedDot()
            LedDot()
            LedDot()
            time.sleep(1)
        if (let=="t" or let=="T"):
            LedDash()
            time.sleep(1)
        if (let=="u" or let=="U"):
            LedDot()
            LedDot()
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="v" or let=="V"):
            LedDot()
            LedDot()
            LedDot()
            LedDash()
            time.sleep(1)
        if (let=="W" or let=="W"):
            LedDot()
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="x" or let=="X"):
            LedDash()
            LedDot()
            LedDot()
            LedDash()
            time.sleep(1)
        if (let=="y" or let=="Y"):
            LedDash()
            LedDot()
            LedDash()
            LedDash()
            time.sleep(1)
        if (let=="z" or let=="Z"):
            LedDash()
            LedDash()
            LedDot()
            LedDot()
            time.sleep(1)            
    
LEDbutton = Button(window, text = "Run Morse",bg='Gray', font = myFont,height=2, width =8, command = executeMorse)
LEDbutton.grid(row=0 , column = 1)

morseEntry = Entry(window)
morseEntry.grid(row=0, column = 0)

def quitLEDS():
    RPi.GPIO.cleanup()
    window.destroy()

exitbutton = Button(window, text = "QUIT",bg='White', font = myFont,height=2, width =6, command = quitLEDS)
exitbutton.grid(row=0 , column = 2)

window.protocol("Delete Window", quitLEDS)

mainloop()
